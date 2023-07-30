from github import Github
from github import Auth
import streamlit as st

st.write(st.experimental_user)

GITHUB_REPO = 'Travels_Car_Driver_Tracking'
GITHUB_TOKEN = st.secrets["Git_Hub_Token"]

auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)


st.title('Try to add text to GitHub')

def write(text):
    r, rf,ft = get_file()
    t = ft + text
    r.update_file(rf.path,'streamlit commit',t,rf.sha,branch='main')

text = st.text_input('Text')
st.button('Add text to file',on_click = write,args = [text])

# using an access token

# First create a Github instance:

# Public Web Github

# all_files = []
# contents = repo.get_contents("tests/test_1.txt")

# print(contents)
# new_text = contents.decoded_content.decode() + '\nAdding stuff'

# repo.update_file(contents.path,'Adding stuff',new_text,contents.sha,branch='main')
