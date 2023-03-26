import streamlit as st
st.title("Hello world")

f = open("db.txt", "a+")

class Person:
    def __init__(self, name, age, sexuality, gender):
        self.name = name
        self.age = age
        self.sexuality = sexuality
        self.gender = gender

    def __str__(self):
        return f"{name} {age} {sexuality} {gender}\n"

name = st.text_input("Name")
age = st.text_input("Age")
sexuality = st.text_input("Sexuality")
gender = st.text_input("Gender")

if st.button("Submit"):
    f.write(str(Person(name, age, sexuality, gender)))
    f.close()
    
    f = open("db.txt", "r")

for x in f.readlines():
    st.write(x)
f.close()
