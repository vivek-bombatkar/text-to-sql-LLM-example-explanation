import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def main():
    # Function to generate SQL query based on prompt input
    def gemini_ans(prompt_input):
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content([prompt_input])
        return response.text

    # Set page configuration
    st.set_page_config(page_title='SQL Query Generator', page_icon=':robot:')
    
    # Custom CSS for styling
    st.markdown(
        """
        <style>
            body {
                background-color: #f5f5f5;
                font-family: 'Arial', sans-serif;
            }
            .header {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }
            .header h1 {
                margin: 0;
                color: #333333;
                text-align: center;
            }
            .header p {
                margin: 0;
                text-align: center;
                color: #666666;
                font-size: 14px;
            }
            .input-container {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }
            .stTextArea, .stTextInput, .stButton {
                margin-top: 15px;
            }
            .stButton > button {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
            .stButton > button:hover {
                background-color: #45a049;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header section
    st.markdown(
        """
        <div class="header">
            <h1>SQL Query Generator</h1>
            <p>Effortlessly transform your natural language input into SQL queries!</p>
        </div>
        """
    , unsafe_allow_html=True)

    # Input section with a card-like design
    st.markdown(
        """
        <div class="input-container">
            <h4>Enter your details below:</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Inputs
    input_text = st.text_area('Enter your natural language query...', placeholder="e.g., Get total sales for this month")
    schema_name = st.text_input('Enter the schema name (optional):', placeholder="e.g., public")
    table_name = st.text_input('Enter the table name:', placeholder="e.g., users")

    # Generate SQL Query button
    submit = st.button('Generate SQL Query', key='generate_button')
    
    # Prompts for model responses
    prompt = """
        You are an English to SQL language translator. The schema name is {schema}, 
        and the table name is {table}. Using the given text here {en},
        write a SQL query only without making any mistakes.
    """

    prompt1 = """
        What would be the expected response of this query snippet:
        ```
        {query}
        ```
        Provide a sample tabular response with no explanation.
    """

    prompt2 = """
        Explain the SQL query:
        ```
        {query}
        ```
        Please provide the simplest explanation.
    """

    # Handle button click event
    if submit:
        if not table_name:
            st.error("Please enter the table name!")
            return
        
        with st.spinner('Generating SQL Query...'):
            # Generate SQL query
            sql_query = gemini_ans(prompt.format(
                schema=schema_name or 'default schema', 
                table=table_name, 
                en=input_text
            ))
            st.header('Model Response')
            st.success("Generated SQL Query Successfully!")
            st.code(sql_query, language="sql")

            # Generate sample expected output
            sql_table = gemini_ans(prompt1.format(query=sql_query))
            st.success('Sample Expected Output')
            st.markdown(sql_table)

            # Generate explanation of the given query
            sql_explanation = gemini_ans(prompt2.format(query=sql_query))
            st.success('Explanation of the Given Query')
            st.markdown(sql_explanation)

# Execute main function
if __name__ == "__main__":
    main()
