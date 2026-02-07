import streamlit as st
import pandas as pd

st.title("Dashboard for Scientist")
CSV_data = st.file_uploader("Upload CSV File", type=["csv"])
if CSV_data is None:
    st.info("Please upload a CSV file to continue.")
    st.stop()

Diabetes_df = pd.read_csv(CSV_data)
st.dataframe(Diabetes_df.head())
print(f"Number of Rows: \n{Diabetes_df.shape[0]}")
st.text("Number of Rows:")
st.write(Diabetes_df.shape[0])
st.text("Number of Columns")
st.write(Diabetes_df.shape[1])
st.text("Overall Shape")
st.write(Diabetes_df.shape)
st.text("All Coloumns and their Data Types : ")
st.dataframe(Diabetes_df.dtypes)
st.text("Total NUll Values: ")
st.write(Diabetes_df.isnull().sum().sum())
st.text("Column Wise Null Values Are: ")
st.dataframe(Diabetes_df.isnull().sum())
