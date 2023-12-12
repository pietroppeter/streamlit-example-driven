import streamlit as st
import data

st.title("Chi cerca trova")
st.write(data)

commedia = data.load_commedia()
st.write(commedia)
for chunk in commedia.chunks:
  if chunk.section == "" or chunk.subsection == "" or not chunk.lines:
    st.write(chunk)