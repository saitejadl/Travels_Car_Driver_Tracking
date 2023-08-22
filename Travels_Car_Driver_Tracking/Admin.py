#>                                 https://travels-car-driver-tracking.streamlit.app/
from github import Github
from github import Auth
import streamlit as st
import pandas as pd
import json
import requests
from streamlit_lottie import st_lottie

#-------Page Congigurations
PAGE_NAME = "Admin Balaji Travels Tracking | APP"
PAGE_ICON = "🗺️📌"
st.set_page_config(page_title=PAGE_NAME, page_icon=PAGE_ICON,layout="wide")

#-------Animation setup
url1 = requests.get("https://lottie.host/67db9e87-0d87-4959-84b5-a33e9e73d39e/GF5O7NQSHU.json")
if url1.status_code == 200:
    url_json1 = url1.json()
else:
    print("URL ERROR")

    
#______________Authenticating GITHUB________________#
GITHUB_REPO = 'Travels_Car_Driver_Tracking'
GITHUB_TOKEN = st.secrets["Git_Hub_Token"]
auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

def get_file():
    """
    Parameters: None,
    return    :repo, repo_file, file_text
    Reads the file in repository returns repository, file in the repository we mention in get_contents() method, text in the file
    """
    repo = g.get_user().get_repo(GITHUB_REPO) 
    repo_file = repo.get_contents('Travels_Car_Driver_Tracking/Users_Password.txt')
    file_text = repo_file.decoded_content.decode()
    return repo, repo_file, file_text
def write(text):
    """
    Parameter : text
    return    : None
    Commits the changes in the repository file
    """
    r, rf,ft = get_file()
    t = ft + text
    r.update_file(rf.path,'streamlit commit',t,rf.sha,branch='main')

st.subheader("Balaji Travels Admin")

# Reading Users_Password.txt from github in read mode and converting the read text into u_p dictionary for usernames and passwords
with open("Travels_Car_Driver_Tracking/Users_Password.txt",'r') as f:
  a = f.read().split("\n")[:-1]
keys=[]
vals=[]
for i in a:
  keys.append(i.split(":")[0])
  vals.append(i.split(":")[1])
u_p = dict(zip(keys,vals))

st.sidebar.subheader(':blue[SIGNIN]', anchor='signin')
user_name = st.sidebar.text_input('Username', value="")
password = st.sidebar.text_input('Password', value="", type="password")

# Authenticating user from u_p dictionary which is created from Users_Password.txt file in gihub
if user_name in u_p.keys():
  if password==u_p[user_name]:
      
    st.sidebar.success("SIGN IN")
      
    # Reading Data.txt from github into a Dataframe by | as a separator
    df = pd.read_csv("Travels_Car_Driver_Tracking/Data.txt",sep="|")
    st.dataframe(data=df,use_container_width=True)
      
    # Adding filter mechanism through variables of dataframe then values of that variable
    c1,c2 = st.columns(2)
    with c1:
      col = st.selectbox("Filter by:", df.columns)
    with c2:
      search = st.selectbox("Filter by Value:", df[col].unique())
    st.dataframe(data=df[df[col]==search],use_container_width=True)
      
  elif password!='':
    st.sidebar.error("Invalid Password")      
elif user_name!='':
    st.sidebar.error("Invalid Username")
    
for i in range(20):
    st.sidebar.write("###")
    if i==7:
        col1,col2,col3 = st.sidebar.columns([1,6,1])
        with col1:
            pass
        with col2:
            st_lottie(url_json1)
        st.sidebar.write("---")


    
st.sidebar.subheader(':orange[SIGNUP]', anchor='signup')
with st.sidebar.expander("SIGNUP"):
    r_user = st.sidebar.text_input('New Username', value="")
    r_password = st.sidebar.text_input('New Password', value="", type="password")
    r_verify = st.sidebar.text_input('Re-Enter Password', value="", type="password")
    if(r_password==r_verify):
      Referal_Code = st.sidebar.text_input('Referal Code', value="")
      if Referal_Code=="saiteja":
        st.sidebar.button('SIGNUP',on_click = write,args = [f'{r_user}:{r_password}'])
      elif Referal_Code!='':
        st.sidebar.error("Invalid Referal")
          
st.write("---")
st.header("Contact:")
st.write("+91 9542593585    |        lakshmisaitejadharmada@gmail.com")
