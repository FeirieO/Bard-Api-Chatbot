from bardapi import Bard
import streamlit as st
from streamlit_chat import message
import os

os.environ["_BARD_API_KEY"] = ""

st.title("AI Utibe")

def response_api(prompt):
    message = Bard().get_answer(str(prompt))['content']
    return message

def user_input():
    input_text  = st.text_input("Enter your prompt:  ")
    return input_text

if 'generate' not in st.session_state:
    st.session_state['generate']=[]
if 'past' not in st.session_state:
    st.session_state['past']=[]

user_text = user_input()

if user_text:
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.generate.append(user_input)

if st.session_state['generate']:
    
    for i in range(len(st.session_state['generate']) -1 -1 -1):
        message(st.session_state['past'][i], is_user=True, key=str(1)+ '_user')
        message(st.session_state['generate'][i], key=str(i))