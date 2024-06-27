from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables from .env file
load_dotenv()

# Set the API key for OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define the function to get OpenAI response
def get_openai_response(question):
    llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.5)
    response = llm(question)
    return response

# Streamlit application setup
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

# Input text from user
input_text = st.text_input("Input : ", key="input")

# Button to submit the question
submit = st.button("Ask the question")

# Display response when button is clicked
if submit:
    response = get_openai_response(input_text)
    st.subheader("The Response is: ")
    st.write(response)
