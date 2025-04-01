import streamlit as st

st.set_page_config(page_title="growth mindset project")
st.title("Growth Mindset Challenge: Web App with Streamlit")
st.header("Welcome to your Growth Journey")
st.write("Embrace challenge, learn from mistakes, and unlock your full potential.")

st.header("Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: It is the courage to continue that counts - Winston Churchill")

st.header("What is your challenge today")
user_input = st.text_input("Describe a challenge you are facing:")

if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflection here")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties")

st.header("Celebrate Your Win!")
achievement = st.text_input("Share something you have recently achieved")

if achievement:
    st.success(f"Amazing! You achieved: {achievement}")  # Fixed variable name and f-string
else:
    st.info("Big or small, every achievement counts! Share one now")

st.write("-----------------")
st.write("Keep believing in yourself. Growth is a journey, not a destination!")
st.write("*******created by NoorAllah**********")