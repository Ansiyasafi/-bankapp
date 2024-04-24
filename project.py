import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
import pandas as pd
import mysql.connector
import sqlite3
filepath='D:/application develop/Employee_monthly_salary.csv'
detail=pd.read_csv(filepath)
detail1=pd.DataFrame(detail)


st.set_page_config(layout='centered')
st.title('BANKING APPLICATION')
if 'authenticated' not in st.session_state:
   st.session_state['authenticated']=False
def cred_entered():
   user_name=st.text_input(label="USER NAME : ",value="")
   passcode=st.text_input(label="PASSWORD : ",value="", type="password",placeholder="enter the password...")
   button=st.button("login")
   if user_name=='admin' and passcode=='passkey' and button:
      st.session_state["authenticated"]=True
   else: 
      st.error("invalid username password")
   return   
     

if   st.session_state['authenticated']==False:   
   cred_entered()
        
else :  
   with st.sidebar:
      option=option_menu('WELCOME TO THE OFFICIAL PAGE OF SBI BANK',['SESSION1','SESSION2'])
        
   if option=='SESSION1':
         st.write("WELCOME TO SESSION 1")
        
         st.subheader(':red[EMPLOYEE DETAIL]')
         st.dataframe(detail1)
   else:
         option='SESSION2'
         st.write("WELCOME TO SESSION 2 ")
         id=st.text_input("ENTER YOUR NAME:")
         if st.button(":red[EMPLOYEE INFO]"):
            res=detail1[detail1["Name"]==id]
            st.dataframe(res)
