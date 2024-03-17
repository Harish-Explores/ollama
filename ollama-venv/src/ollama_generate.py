import ollama
import streamlit as st
import pyautogui
from datetime import datetime 

def getLLMResponse(user_prompt):
    start_time = datetime.now() 
    with st.spinner('Getting response...'):
        response_generated = ollama.generate(
            model='llama2',
            prompt=user_prompt
        )
    return response_generated, start_time

def getResponseTime(start_time, end_time):
    response_time = end_time - start_time
    difference = divmod(response_time.total_seconds(), 60)
    return str(int(difference[0])) + 'm ' + str(round(difference[1],2)) + 's'
    

if __name__ == '__main__':
    st.set_page_config(page_title="Ask Llama2",layout="wide")
    st.title('Hello, try out Llama2 from Meta')
    st.caption("""
               This a text generation project build by Harish Kumar using Llama2, Llama2 is a open source large language model (llm) from Meta,\n 
               the whole model is downloaded and the queries are processed using basic CPU compution, hence please expect some delay in retrieving the response.
               """)
    
    chat_column, analytics_column = st.columns((2, 1))
    
    with chat_column:
        st.header('Question')
        user_prompt = st.text_input('Enter Your Question')
        
        if user_prompt:
            if st.button('Ask New Question'):
                pyautogui.hotkey('f5')
        
        st.divider()
        
        st.header('Answer')
        generated_response, start_time = getLLMResponse(user_prompt)
        st.write(generated_response['response'])
        
    with analytics_column:
        st.header("Response Metrics")
        if generated_response['response']:
            response_time = getResponseTime(start_time, datetime.now())
            analytics_column.metric('Response Time', response_time)

        