import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
st.title("🏠Housing Price")
st.header("Enter House Details:")
size = st.number_input("Size of the house(in sqft):")

bedrooms = st.slider("Number of bedrooms:",1,6,3)
age = st.slider("Age of house in years:",1,50,5)
data = {
    'Size_sqft': [1000, 1500, 1500, 2000, 2000, 2500, 2500],
    'Bedrooms':  [2,    2,    3,    3,    4,    3,    4],
    'Age':       [10,   8,    6,    5,    2,    4,    1],
    'Price':     [200000, 210000, 240000, 280000, 310000, 320000, 350000]
}
if st.button("Calculate Price"):
    df = pd.DataFrame(data)
    reg = linear_model.LinearRegression()
    Xtrain,Xtest,ytrain,ytest = train_test_split(df[['Size_sqft','Bedrooms','Age']],df['Price'],test_size = 0.1)
    reg.fit(Xtrain,ytrain)
    inp = [[size,bedrooms,age]]
    a = reg.predict(inp)[0]
    st.success(f"The price of {size}sqft, {bedrooms}bedrooms, {age}yrs is :{int(a)}")