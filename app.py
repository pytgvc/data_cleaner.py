import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("🧹 Data Cleaner App")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read dataset
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Original Data Preview")
    st.write(df.head())

    # Sidebar cleaning options
    st.sidebar.header("Cleaning Options")

    # Remove duplicates
    if st.sidebar.checkbox("Remove Duplicates"):
        df = df.drop_duplicates()

    # Handle missing values
    missing_option = st.sidebar.selectbox(
        "Handle Missing Values",
        ["Do Nothing", "Drop Rows", "Fill with Mean", "Fill with Median"]
    )
    if missing_option == "Drop Rows":
        df = df.dropna()
    elif missing_option == "Fill with Mean":
        df = df.fillna(df.mean(numeric_only=True))
    elif missing_option == "Fill with Median":
        df = df.fillna(df.median(numeric_only=True))

    # Standardize text columns
    if st.sidebar.checkbox("Standardize Text Columns"):
        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].str.strip().str.lower()

    # Rename columns
    if st.sidebar.checkbox("Rename Columns"):
        new_cols = {}
        for col in df.columns:
            new_name = st.text_input(f"Rename {col}", col)
            new_cols[col] = new_name
        df = df.rename(columns=new_cols)

    # Show cleaned data
    st.subheader("✨ Cleaned Data Preview")
    st.write(df.head())

    # Visualization
    st.subheader("📈 Data Visualization")
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if len(numeric_cols) > 0:
        col_to_plot = st.selectbox("Select numeric column to visualize", numeric_cols)
        fig, ax = plt.subplots()
        df[col_to_plot].hist(ax=ax, bins=20)
        ax.set_title(f"Distribution of {col_to_plot}")
        st.pyplot(fig)
    else:
        st.write("No numeric columns available for visualization.")

    # Download cleaned dataset
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download Cleaned CSV",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )