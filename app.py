import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure GenerativeAI with API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def main():
    # Function to generate SQL query based on prompt input
    def gemini_ans(prompt_input):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content([prompt_input])
        return response.text

    # Set page configuration
    st.set_page_config(page_title='SQL Query Generator', page_icon=':robot:')
    
    # Header section
    st.markdown(
        """
        <style>
            .header {
                padding: 20px;
                background-color: #f0f0f0;
                border-radius: 10px;
                margin-bottom: 20px;
                color: black;
            }
            .header h1, .header h3 {
                margin: 0;
                color: black;
            }
        </style>
        """
    , unsafe_allow_html=True)

    st.markdown(
        """
        <div class="header">
            <h1 style="text-align: center;">SQL Query Generator 🤖</h1>
            <h3 style="text-align: center;">Generate SQL queries with ease!</h3>
            <p style="text-align: center;">This tool allows you to generate SQL queries based on your prompt.</p>
        </div>
        """
    , unsafe_allow_html=True)
    
    # Text area for input
    input_text = st.text_area('Enter your query...')
    
    # Generate SQL Query button
    submit = st.button('Generate SQL Query', key='generate_button')
    
    # Prompts for model responses
    prompt = """
        You are an English to SQL language translator. Using the given text here {en},
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
        with st.spinner('Generating SQL Query...'):
            # Generate SQL query
            sql_query = gemini_ans(prompt.format(en=input_text))
            st.header('Model Response')
            st.success("Generated SQL Query Successfully!")
            st.write(sql_query)

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
