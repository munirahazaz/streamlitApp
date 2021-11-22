import streamlit as st
import numpy as np
import pandas as pd

st.header("SAVINGS CALCULATOR")
st.write("Let me help you on how to build your savings monthly")

st.write("")
st.write("Savings= Current income - personal needs - monthly expenses ")

from PIL import Image
image = Image.open('savings.jpg')

st.image(image, caption= 'Something to think of')

st.sidebar.write(""" ### Please key in numbers ONLY 
""")
income = st.sidebar.text_input('Current income (RM)')
personalNeeds = st.sidebar.text_input('Estimation of personal needs (RM)')
monthlyExpenses = st.sidebar.text_input('Total amount for monthly expenses (RM)')


class Savings():
  def __init__(self, income=float(income), personalNeeds=float(personalNeeds), monthlyExpenses=float(monthlyExpenses) ):
        self.totalIncome = income
        self.personalNeeds = personalNeeds
        self.monthlyExpenses = monthlyExpenses
       

  def gettotalIncome(self):
        return income

  def getTotalSavings(self):
        return self.totalIncome - self.personalNeeds - self.monthlyExpenses
    


mySavingsCalculator = Savings()

st.write("")
st.write("")
st.write("Your TOTAL INCOME is: RM ", (mySavingsCalculator.gettotalIncome()))
st.write("")
st.write("The SUGGESTED AMOUNT for your monthly savings is: RM ",(mySavingsCalculator.getTotalSavings()))
st.write("")
st.write("")
st.write("")
st.write("Oops! What if your suggested amount is negative values? Maybe you need to limit your monthly spending a bit")
st.write("Goodluck!")


st.balloons()


