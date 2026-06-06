# 🤖 ChatWithDB: AI-Powered Text-to-SQL Engine

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Integration-FFBA08)](https://www.langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📋 Overview

**ChatWithDB** is an innovative AI-powered application that bridges the gap between natural language and SQL databases. Users can ask questions in plain English, and the system automatically generates optimized SQL queries, retrieves data, and presents results in an intuitive interface—all with built-in security safeguards.

### 🎯 Key Innovation

This project eliminates the need for SQL expertise, making database querying accessible to business analysts, stakeholders, and non-technical users while maintaining strict security protocols to prevent malicious operations.

---

## ✨ Features

- **🗣️ Natural Language Processing**: Convert plain English questions into precise SQL queries using AI
- **⚡ Intelligent Query Generation**: Powered by Qwen 2.5 Coder LLM with optimized prompting
- **🔒 Security-First Design**: Built-in protection against SQL injection and destructive commands
- **📊 Real-Time Results**: Instant data retrieval and visualization in tabular format
- **🎨 User-Friendly Interface**: Streamlit-powered dashboard for seamless interaction
- **📈 Dynamic Schema Extraction**: Automatic database structure detection and analysis
- **🛡️ Read-Only Mode**: Enforces query safety with forbidden keyword blocking

---

## 🏗️ Architecture & Workflow

```
User Question (Streamlit UI)
       ↓
get_data_from_database() [main.py]
       ↓
extract_schema() → Database Structure (JSON Format)
       ↓
text_to_sql() → AI Model Generates SQL Query
       ↓
Security Validation → Blocks Dangerous Commands
       ↓
Execute SQLite Query → Retrieve Data
       ↓
Pandas DataFrame → Format as Table
       ↓
Display Results (Streamlit Interface)
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **Backend** | Python 3.8+ |
| **Database** | SQLite |
| **AI/ML** | LangChain + Ollama (Qwen 2.5 Coder 7B) |
| **Data Processing** | Pandas, SQLAlchemy |
| **ORM** | SQLAlchemy |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Ollama installed and running locally ([Download Ollama](https://ollama.ai))

### Step 1: Clone the Repository
```bash
git clone https://github.com/Furqan-Ahmed2006/Text-_To_SQL_Agent.git
cd Text-_To_SQL_Agent
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Initialize the Database
```bash
python Database_Creation.py
```

This will create `amazon.db` with sample e-commerce data (customers, products, orders, order items).

### Step 5: Pull the Required LLM Model
```bash
ollama pull qwen2.5-coder:7b
ollama serve
```

Keep the Ollama server running in a separate terminal.

### Step 6: Launch the Application
```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

---

## 🚀 Usage

1. **Start the Application**: Run `streamlit run app.py`
2. **Enter Your Question**: Type any business question in natural language
   - Example: *"What are the top 3 customers by total spending?"*
   - Example: *"Show me all orders from Lahore city"*
   - Example: *"Which products are most popular based on quantity sold?"*
3. **Click Analyze**: The AI processes your query and generates SQL
4. **View Results**: Results are displayed in an organized table format

### 🔐 Security Features
- **Forbidden Keywords Detection**: Blocks `DROP`, `DELETE`, `TRUNCATE`, `UPDATE`, `INSERT`, `ALTER`, `GRANT`
- **Read-Only Database Connection**: Queries execute in read-only mode
- **Input Validation**: Regex-based pattern matching for dangerous SQL patterns

---

## 📂 Project Structure

```
Text-_To_SQL_Agent/
├── app.py                      # Streamlit frontend interface
├── main.py                     # Core business logic & query processing
├── Database_Creation.py        # Sample database setup script
├── requirements.txt            # Python dependencies
├── amazon.db                   # SQLite database (auto-generated)
└── README.md                   # Project documentation
```

### File Descriptions

| File | Purpose |
|------|---------|
| **app.py** | Streamlit UI with text input, query submission, and result display |
| **main.py** | Core functions: `extract_schema()`, `text_to_sql()`, `get_data_from_database()` |
| **Database_Creation.py** | Creates and populates sample Amazon e-commerce database |
| **requirements.txt** | Project dependencies (Streamlit, LangChain, SQLAlchemy, Pandas) |

---

## 🔑 How It Works

### 1. **Schema Extraction** (`extract_schema()`)
- Introspects SQLite database using SQLAlchemy
- Extracts table names and column information
- Returns structured JSON representation of database schema

### 2. **SQL Generation** (`text_to_sql()`)
- Uses Qwen 2.5 Coder LLM via LangChain
- Provides few-shot examples to guide query generation
- Cleans AI response to ensure valid SQL syntax

### 3. **Security Validation**
- Scans generated queries for forbidden SQL keywords
- Operates in read-only mode to prevent data modification
- Returns security alert if dangerous operation detected

### 4. **Query Execution** (`get_data_from_database()`)
- Connects to SQLite database
- Executes validated SQL query
- Converts results to Pandas DataFrame for display

---

## 📊 Sample Database Schema

### Tables
- **customers**: Customer information (ID, name, email, city, join_date)
- **products**: Product catalog (ID, name, category, price)
- **orders**: Order records (ID, customer_id, order_date, total_amount)
- **order_items**: Order line items (ID, order_id, product_id, quantity, subtotal)

---

## 🎓 Example Queries

Try these questions to explore the system:

```
1. "Total products sold in 2025?"
2. "Top 3 customers by total spending?"
3. "Which products are most popular based on quantity sold?"
4. "Show me orders from Lahore city"
5. "List all customers who made purchases in July 2024"
6. "Average order value by customer"
7. "Products in Electronics category with price > 50"
```

---

## ⚙️ Configuration

### Model Configuration (in `main.py`)
```python
model = OllamaLLM(model="qwen2.5-coder:7b", temperature=0)
```

- **Model**: Qwen 2.5 Coder 7B (optimized for code generation)
- **Temperature**: 0 (deterministic responses for consistency)
- **Ollama Endpoint**: `http://localhost:11434` (default)

### Database Connection
```python
db_url = "sqlite:///amazon.db"
```

---

## 🚨 Security Considerations

✅ **Implemented**
- Read-only database connections
- Forbidden keyword detection
- Input validation with regex patterns
- Parameterized query execution

⚠️ **Recommendations for Production**
- Add user authentication and authorization
- Implement query logging and auditing
- Add rate limiting
- Use more sophisticated SQL injection detection
- Encrypt sensitive database credentials

---

## 🐛 Error Handling

The application gracefully handles:
- Invalid SQL syntax
- Database connection errors
- Empty result sets
- Malicious query attempts

All errors are displayed to the user in a user-friendly format.

---

## 📱 LinkedIn Demo

**[View Project Demo on LinkedIn](YOUR_LINKEDIN_POST_URL_HERE)**

> Click the link above to see a walkthrough of ChatWithDB in action, including:
> - Real-time query generation
> - Results visualization
> - Security features demonstration

---

## 🔄 Potential Enhancements

- [ ] Support for multiple database types (MySQL, PostgreSQL, SQL Server)
- [ ] Query result export (CSV, PDF)
- [ ] Query history and saved queries
- [ ] Advanced filtering and sorting options
- [ ] User authentication and multi-user support
- [ ] Query performance optimization suggestions
- [ ] Natural language result summarization
- [ ] Voice input support
- [ ] Mobile-responsive design

---

## 📝 Requirements

```
streamlit>=1.0
pandas>=1.3
langchain>=0.1
langchain-ollama>=0.1
sqlalchemy>=2.0
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and enhancement requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💼 Author

**Furqan Ahmed**
- GitHub: [@Furqan-Ahmed2006](https://github.com/Furqan-Ahmed2006)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)

---

## 🙏 Acknowledgments

- **LangChain**: For seamless LLM integration
- **Ollama**: For local model deployment
- **Streamlit**: For rapid UI development
- **Qwen Team**: For the excellent Qwen 2.5 Coder model

---

## 📞 Support

For questions or issues, please open a GitHub issue or contact the maintainer directly.

---

**⭐ If you find this project helpful, please consider giving it a star!**
