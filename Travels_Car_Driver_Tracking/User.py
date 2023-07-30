import streamlit as st
from github import Github
from github import Auth
GITHUB_REPO = 'Travels_Car_Driver_Tracking'
GITHUB_TOKEN = st.secrets["Git_Hub_Token"]
auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)
def write(text):
    r, rf,ft = get_file()
    t = ft + text
    r.update_file(rf.path,'streamlit commit',t,rf.sha,branch='main')
def get_file():
    repo = g.get_user().get_repo(GITHUB_REPO)
    repo_file = repo.get_contents('Travels_Car_Driver_Tracking/edit.txt')
    file_text = repo_file.decoded_content.decode()
    return repo, repo_file, file_text
st.subheader("Balaji Travels Car Tracking")
Name = st.text_input("Name of Driver", value=" ", help="Driver Name", placeholder=None)
Ph_Num = st.text_input("Driver Phone Number", value=" ", help="Diver Phone Number", placeholder=None)
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
L = f'\n{Name}|{Ph_Num}|{Car_Name}|{Car_Num}|{Route}|{Loc}|{str(Date)}|{str(Time)}'
st.button('Submit',on_click = write,args = [L])

# if st.button("Submit"):
#   with open("Travels_Car_Driver_Tracking/Data.txt",'a') as f:
#     L = f'\n{Name}|{Ph_Num}|{Car_Name}|{Car_Num}|{Route}|{Loc}|{str(Date)}|{str(Time)}'
#     f.writelines(L)
#     f.close()
#     st.success("Saved")
