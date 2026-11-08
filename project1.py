import streamlit as st

#HAPPY DIWALI


st.write("🪔HAPPY DIWALI🪔")
st.write("=====================")

st.write("Wishing you a joyous and prosperous Diwali filled with love, light, and happiness!")
st.write("======================================================================================")

st.write("May the festival of lights bring you and your family good health, wealth, and success in all your endeavors.")
st.write("===============================================================================================================")

name= st.text_input("Enter your name: ")
st.write(f"Happy Diwali, {name}! 🪔")

st.write("What would you like to do today?")
st.write("1. Light diyas! 🪔")
st.write("2. Burst crackers! 🎆")
st.write("3. Enjoy sweets! 🍬")
st.write("4. Decorate your home! 🏠")

activity = st.selectbox("Enter your choice",["1","2","3","4"])

match activity:
    case "1":
        st.write("Light diyas! 🪔")
    case "2":
        st.write("Burst crackers! 🎆")
    case "3":
        st.write("Enjoy sweets! 🍬")
    case "4":
        st.write("Decorate your home! 🏠")
    case _:
        st.write("You don't have any other option, but you can still enjoy the festival! 🪔")
