from github import Github
from github import Auth
import streamlit as st
import pandas as pd

GITHUB_REPO = 'Travels_Car_Driver_Tracking'
GITHUB_TOKEN = st.secrets["Git_Hub_Token"]
auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

def get_file():
    repo = g.get_user().get_repo(GITHUB_REPO)
    repo_file = repo.get_contents('Travels_Car_Driver_Tracking/Users_Password.txt')
    file_text = repo_file.decoded_content.decode()
    return repo, repo_file, file_text
def write(text):
    r, rf,ft = get_file()
    t = ft.replace("\n", "") + text + '  '
    r.update_file(rf.path,'streamlit commit',t,rf.sha,branch='main')


st.subheader("Balaji Travels Admin")
with open("Travels_Car_Driver_Tracking/Users_Password.txt",'r') as f:
  a = f.readline()[:-2].split(",")
  st.sidebar.write(a)
keys=[]
vals=[]
for i in a:
  keys.append(i.split(":")[0])
  vals.append(i.split(":")[1])
u_p = dict(zip(keys,vals))

user_name = st.sidebar.text_input('Username', value="")
password = st.sidebar.text_input('Password', value="", type="password")
# st.write(u_p[user_name])

if user_name in u_p.keys():
  if password==u_p[user_name]:
    st.sidebar.success("SIGN IN")
    df = pd.read_csv("Travels_Car_Driver_Tracking/Data.txt",sep="|")
    st.dataframe(data=df,use_container_width=True)
    c1,c2 = st.columns(2)
    with c1:
      col = st.selectbox("Filter by:", df.columns)
    with c2:
      search = st.selectbox("Filter by:", df[col].unique())
    st.dataframe(data=df[df[col]==search],use_container_width=True)
  elif password!='':
    st.sidebar.error("Invalid Password")
elif user_name!='':
    st.sidebar.error("Invalid Username")
st.sidebar.write("---")

with st.expander("SIGNUP"):
    r_user = st.sidebar.text_input('New Username', value="")
    r_password = st.sidebar.text_input('New Password', value="", type="password")
    r_verify = st.sidebar.text_input('Re-Enter Password', value="", type="password")
    if(r_password==r_verify):
      Referal_Code = st.sidebar.text_input('Referal Code', value="")
      if Referal_Code=="saiteja":
        st.sidebar.button('SIGNUP',on_click = write,args = [f',{r_user}:{r_password}'])
      elif Referal_Code!='':
        st.sidebar.error("Invalid Referal")






  

