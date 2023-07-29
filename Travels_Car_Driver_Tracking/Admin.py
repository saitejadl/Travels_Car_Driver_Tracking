import streamlit as st
import pandas as pd

st.subheader("Balaji Travels Admin")
with open("Travels_Car_Driver_Tracking/Users_Password.txt",'r') as f:
  a = f.readline()[:-2].split(",")
keys=[]
vals=[]
for i in a:
  keys.append(i.split(":")[0])
  vals.append(i.split(":")[1])
u_p = dict(zip(keys,vals))

user_name = st.sidebar.text_input('Username', value="")
password = st.sidebar.text_input('Password', value="", type="password")

if user_name in u_p.keys():
  if u_p[user_name]==password:
    st.sidebar.success("SIGN IN")
    df = pd.read_csv("Travels_Car_Driver_Tracking/Data.txt",sep="|")
    st.dataframe(data=df,use_container_width=True)
    c1,c2 = st.columns(2)
    with c1:
      col = st.selectbox("Filter by:", df.columns)
    with c2:
      search = st.selectbox("Filter by:", df[col].unique())
    st.dataframe(data=df[df[col]==search],use_container_width=True)
  else:
    st.sidebar.error("Invalid Password")
else:
    st.sidebar.error("Invalid Username")

if st.sidebar.button("SIGN UP"):
  r_user = st.sidebar.text_input('Username', value="")
  r_password = st.sidebar.text_input('Password', value="", type="password")
  r_verify = st.sidebar.text_input('Re-Enter Password', value="", type="password")
  if(r_password==r_verify):
    Referal_Code = st.sidebar.text_input('Referal Code', value="")
    if Referal_Code=="saiteja":
      with open("Travels_Car_Driver_Tracking/Users_Password.txt",'a') as d:
        d.writelines(f",{r_user}:{r_password}")





  

