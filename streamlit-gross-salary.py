#importing required libraries

import streamlit as st




st.write("Employee Gross Salary Calculator")

a = st.text_input("Enter Name of Employee :  ")

h= st.text_input("Enter Name of Company : ")

b= st.number_input("Enter Basic salary of Employee : ")

c = st.number_input(" Dearness allowance percentage : ")

d = st.number_input(" House Rent allowance percentage : ")

st.write("Gross salaray Reciept of  ",a)
st.write(" Base salary Offered By company : ",b)

e= int(b)*int(c)/int(100)

st.write("Dearness allowance offered by company : ",e)

f= int(b)*int(d)/int(100)
st.write("House Rent Allowance offerd by Company : ",f)

g=int(b)+int(e)+int(f)
st.write(" Gross Salary : ",g)

st.write(h)


