import json
import pandas as pd
import re
import sqlite3
from sqlalchemy import create_engine, inspect
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
db_url = "sqlite:///amazon.db"
def extract_schema(db_url):
    engine = create_engine(db_url)
    inspector = inspect(engine)
    schema = {}
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema[table_name] = [col["name"] for col in columns]
    return json.dumps(schema)
def text_to_sql(schema, prompt):
    SYSTEM_PROMPT = """
    You are an expert SQL generator. Given a database schema and a user prompt, generate a valid SQL query that answers the prompt. 
    Only use the tables and columns provided in the schema. ALWAYS ensure the SQL syntax is correct.
    Output only the SQL as your response will be directly used to query data from the database. No preamble please. Do not use <think> tags.

    Here are a few examples of how you should write queries based on the schema:
    
    Example 1:
    User Question: Top 3 customers by total spending?
    SQL Query: SELECT c.name, SUM(o.total_amount) as total_spent FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.customer_id ORDER BY total_spent DESC LIMIT 3;

    Example 2:
    User Question: Which products are most popular based on quantity sold?
    SQL Query: SELECT p.name, SUM(oi.quantity) as total_qty FROM products p JOIN order_items oi ON p.product_id = oi.product_id GROUP BY p.product_id ORDER BY total_qty DESC LIMIT 1;

    Example 3:
    User Question: Show me orders from Lahore city.
    SQL Query: SELECT o.order_id, c.name, o.total_amount FROM orders o JOIN customers c ON o.customer_id = c.customer_id WHERE c.city = 'Lahore';
    """
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", "Schema:\n{schema}\n\nQuestion: {user_prompt}\n\nSQL Query:")
    ])
    model = OllamaLLM(model="qwen2.5-coder:7b", temperature=0)
    chain = prompt_template | model
    raw_response = chain.invoke({"schema": schema, "user_prompt": prompt})
    cleaned_response = re.sub(r"<think>.*?</think>", "", raw_response, flags=re.DOTALL)
    return cleaned_response.strip()
def get_data_from_database(prompt):
    schema = extract_schema(db_url)
    sql_query = text_to_sql(schema, prompt)
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
    forbidden_keywords = ["drop", "delete", "truncate", "update", "insert", "alter", "grant"]
    query_lower = sql_query.lower()
    for keyword in forbidden_keywords:
        if re.search(r'\b' + keyword + r'\b', query_lower):
            return pd.DataFrame({"Security Alert !": ["Action not allowed. Read-Only mode active!"]})
    try:
        conn = sqlite3.connect("file:amazon.db?mode=ro", uri=True)
        cursor = conn.cursor()
        res = cursor.execute(sql_query)
        results = res.fetchall()
        if results:
            column_names = [description[0] for description in res.description]
            df = pd.DataFrame(results, columns=column_names)
            conn.close()
            return df
        else:
            conn.close()
            return pd.DataFrame({"Status": ["Query executed successfully, but no data found."]})    
    except sqlite3.OperationalError as e:
        return pd.DataFrame({"Database Error!": [str(e)]})