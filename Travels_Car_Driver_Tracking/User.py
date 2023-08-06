from github import Github
from github import Auth
import streamlit as st

#______________Authenticating GITHUB________________#
GITHUB_REPO = 'Travels_Car_Driver_Tracking'
GITHUB_TOKEN = st.secrets["Git_Hub_Token"]
auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

def get_file():
    """
    Parameters: None,
    return    :repo, repo_file, file_textrepository,
               file in the repository we mention in get_contents() method,
               Text in the file
    Reads the file in repository returns repository, file in the repository we mention in get_contents() method, text in the file
    """
    repo = g.get_user().get_repo(GITHUB_REPO)
    repo_file = repo.get_contents('Travels_Car_Driver_Tracking/Data.txt')
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

st.subheader("Balaji Travels Car Tracking")
Driver_Name = st.text_input("Name of Driver", value=" ", help="Driver Name", placeholder=None)
Driver_Phone_Num = st.text_input("Driver Phone Number", value=" ", help="Diver Phone Number", placeholder=None)
c1,c2 = st.columns(2)
with c1:
  Car_Name = st.selectbox("Car Name", ['baleeno','ertiga','i10','ferare','Bugati','roles Royes'], help='Car Name')
with c2:
  Car_Num = st.text_input("Car Number", value=" ", help="Car Number Plate", placeholder=None)
Route = st.text_input("Travel Route", value=" ", help="Car Travelling Route", placeholder=None)
co1,co2,co3 = st.columns(3)
with co1:
  Loc = st.text_input("Location", value=" ", help="Car Exact Location", placeholder=None)
with co2:
  Date = st.date_input("Date", value=None,help='Date')
with co3:
  Time = st.time_input("Time", value=None,help="Time")
text = f'\n{Driver_Name}|{Driver_Phone_Num}|{Car_Name}|{Car_Num}|{Route}|{Loc}|{str(Date)}|{str(Time)}'
st.button('SUBMIT',on_click = write,args = [text])

# if st.button("Submit"):
#   with open("Travels_Car_Driver_Tracking/Data.txt",'a') as f:
#     L = f'\n{Name}|{Ph_Num}|{Car_Name}|{Car_Num}|{Route}|{Loc}|{str(Date)}|{str(Time)}'
#     f.writelines(L)
#     f.close()
#     st.success("Saved")
