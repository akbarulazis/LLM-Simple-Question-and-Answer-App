# Import streamlit for web application framework
import streamlit as st
# import lanchain for llm framework
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environments variables from .env
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
# function to invoke question into llm
def text_question(text):
    llm = ChatOpenAI(model_name="gpt-4o")
    res = llm.invoke(text)
    return res.content


st.set_page_config(page_title = 'LangChain Open AI Testing / Demo', page_icon=':robot')
st.header('LangChain Open AI Demo')


def text_input():
    input_txt = st.text_input('Ask Question : ', key='input'  )
    return input_txt

user_input = text_input()
response  = text_question(user_input)

submit = st.button('Generate')

# if button is clicked
if submit:
    st.subheader('ANSWER')
    st.write(response)
