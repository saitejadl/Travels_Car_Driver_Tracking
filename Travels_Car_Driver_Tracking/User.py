import streamlit as st
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
if st.button("Submit"):
  with open("Travels_Car_Driver_Tracking/Data.txt",'a') as f:
    L = f'\n{Name}|{Ph_Num}|{Car_Name}|{Car_Num}|{Route}|{Loc}|{str(Date)}|{str(Time)}'
    f.writelines(L)
    f.close()
    st.success("Saved")
