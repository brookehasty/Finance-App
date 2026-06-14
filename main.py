import streamlit as st
import pandas as pd 
import plotly.express as px
import json
import os

st.set_page_config(page_title="Finance App", page_icon="💰", layout="wide")

def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns] # remove white spaces
        st.write(df)

        return df
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

def main():
    st.title("Finance Dashboard")

    uploaded_file = st.file_uploader("Upload your transaction csv file", type=["csv"])

    if uploaded_file is not None:
        df = load_transactions(uploaded_file)

main()