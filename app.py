import streamlit as st
from main import get_data_from_database
st.set_page_config(
    page_title="Text_To_SQL Engine",
    page_icon="🤖",
    layout="centered"
)
st.title("🤖 ChatWithDB: AI-Powered Text-to-SQL Engine")
st.markdown("Bridge the gap between natural language and SQL databases securely.")
user_query = st.text_area("💬 Enter your question:", placeholder="e.g., Total products sold in 2025")
if st.button("Analyze"):
    if user_query.strip() == "":
        st.warning("Please enter a question to analyze.")
    else:
        with st.spinner("Analyzing your query..."):
            database_response = get_data_from_database(user_query)
        st.success("Analysis complete!")
        st.markdown("🔍 **Here's the analysis for your query:**")
        if not database_response.empty: 
          st.dataframe(database_response, use_container_width=True)
        else:
          st.info("No data found or action completed.")