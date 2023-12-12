import streamlit as st
import data
import search


corpus = data.load_corpus()

st.title("Chi cerca trova")
st.markdown("Search in a small corpus of Italian literature documents.")

show_max_chunks = st.sidebar.number_input(
    "Max number of chunks to show", min_value=3, max_value=100, value=10
)

documents = [
    corpus[name]
    for name in st.multiselect("Documents", corpus.keys(), default=corpus.keys())
]

if len(documents) == 0:
    st.error("Please select at least one document")
    st.stop()


query = st.text_input("Search query")
case_sensitive = st.checkbox("Case sensitive", value=False)
if query:
    for document in documents:
        st.markdown("---")
        st.markdown(f"### {document.title}")
        matches = search.match(document, query, case_sensitive=case_sensitive)
        if matches:
            st.success(f"Found {len(matches)} matches.")
            show_matches = matches[: min(show_max_chunks, len(matches))]
            if len(show_matches) < len(matches):
                st.warning(f"showing first {len(show_matches)} matches")
            for match in show_matches:
                st.markdown(f"**{match.chunk.section}, {match.chunk.subsection}**")
                st.markdown("  \n".join(match.chunk.lines))
        else:
            st.warning(f"No matches found")
else:
    st.markdown("Please enter a search query")
