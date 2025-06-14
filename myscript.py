import streamlit as st
import pandas as pd

st.title("Student Marks")

df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Marks': [85, 90]
})

st.write("Here is the student data:")
st.dataframe(df)

csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", csv, "marks.csv", "text/csv")


