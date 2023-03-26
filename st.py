import streamlit as st
st.title("Hello world")

#create a python object with personal info

db = []

class Person:
    def __init__(self, name, age, sexuality, gender):
        self.name = name
        self.age = age
        self.sexuality = sexuality
        self.gender = gender

    def __str__(self):
        return f"{name} {age} {sexuality} {gender}"

name = st.text_input("Name")
age = st.text_input("Age")
sexuality = st.text_input("Sexuality")
gender = st.text_input("Gender")

db.append(Person(name, age, sexuality, gender))

for x in db:
    st.write(x)
