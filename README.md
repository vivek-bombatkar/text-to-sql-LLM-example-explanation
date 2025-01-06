---
title: Text To Sql Example Explanation
emoji: 👀
colorFrom: pink
colorTo: red
sdk: streamlit
sdk_version: 1.32.2
app_file: app.py
pinned: false
license: mit
---

# SQL Query Generator

Effortlessly transform your natural language inputs into SQL queries using this Streamlit application powered by Google Generative AI.

## Features
- Generate SQL queries from natural language input.
- Optionally specify schema and table names for precise query generation.
- Get sample expected responses for the generated SQL query.
- Receive a simple explanation of the SQL query.

---

## Prerequisites
### 1. Install Required Tools
Ensure the following tools are installed:
- Python 3.8+

### 2. Obtain API Key
1. Get an API key for Google Generative AI from [Google Cloud Console](https://console.cloud.google.com/).
2. Save the API key for later configuration.

---

## Installation

### Clone the Repository
```bash
# Clone this repository
git clone <repository_url>
cd <repository_folder>
```

### Create and Activate a Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For MacOS/Linux:
source venv/bin/activate
```

### Install Dependencies
```bash
# Install required Python libraries
pip install -r requirements.txt
```

---

## Configuration
1. Create a `.env` file in the root of your project directory.
2. Add your Google API key to the `.env` file as follows:
```env
GOOGLE_API_KEY="<your_google_api_key>"
```

---

## Usage

### Run the Application
```bash
streamlit run app.py
```

### Input Details
1. Enter your natural language query in the text box.
2. Optionally, specify a schema name.
3. Enter a table name (this is mandatory).
4. Click on **Generate SQL Query**.

### Outputs
The application will provide:
1. The generated SQL query.
2. A sample tabular response for the query.
3. A simple explanation of the SQL query.

---

## Project Structure
```
.
├── app.py             # Main Streamlit app
├── .env               # Environment file for API key
├── requirements.txt   # Python dependencies
├── README.md          # This file
```

---

## Troubleshooting
### 1. Error: `Please enter the table name!`
- Ensure the **Table Name** field is not empty.

### 2. API Key Issues
- Verify the API key in your `.env` file is correct and has sufficient permissions.

### 3. Missing Dependencies
- Ensure all dependencies are installed via `pip install -r requirements.txt`.

---

## Contributing
Feel free to fork this repository, raise issues, or submit pull requests. Contributions are always welcome!

---

## License
This project is licensed under the MIT License.

---

## Acknowledgments
- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://cloud.google.com/genai)
- [dotenv](https://pypi.org/project/python-dotenv/)


Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
