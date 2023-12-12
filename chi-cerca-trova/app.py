import streamlit as st
import data
import search

st.title("Chi cerca trova")
st.subheader("_(kee chair-kah truh-vah)_")
st.markdown("""
Information retrieval system for search in Italian literature corpora.
""")
commedia = data.load_commedia()
st.markdown(f"Current corpus is {commedia.title}")
#search.match

query = st.text_input("Search query")
if query:
  matches = search.match(commedia, query)
  if matches:
    st.success(f"Found {len(matches)} matches")
    for match in matches:
      st.markdown(f"**{match.chunk.section}, {match.chunk.subsection}**")
      st.markdown("  \n".join(match.chunk.lines))
  else:
    st.warning(f"No matches found")
