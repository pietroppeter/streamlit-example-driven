import streamlit as st
import data
import search

st.title("Chi cerca trova")
st.subheader("_(kee chair-kah truh-vah)_")
st.markdown(
    """
Information retrieval system for search in Italian literature corpora.
"""
)

corpus = data.load_orlando()

st.markdown(f"Current corpus is {corpus.title}")
show_max_matches = st.sidebar.number_input(
    "Max number of matches to show", min_value=3, max_value=100, value=10
)

query = st.text_input("Search query")
case_sensitive = st.checkbox("Case sensitive", value=False)
if query:
    matches = search.match(corpus, query, case_sensitive=case_sensitive)
    if matches:
        num_pages = ((len(matches) - 1) // show_max_matches) + 1
        show_pages = (
            f" Showing in {num_pages} pages (of {show_max_matches} matches max)."
            if num_pages > 1
            else ""
        )
        es = "es" if len(matches) > 1 else ""
        st.success(f"Found {len(matches)} match{es}." + show_pages)
        if num_pages > 1:
            num_page = st.number_input(
                "Page", min_value=1, max_value=num_pages, value=1
            )
            start_index = (num_page - 1) * show_max_matches
            end_index = start_index + show_max_matches
            show_matches = matches[start_index:end_index]
        else:
            show_matches = matches
        for match in show_matches:
            st.markdown(f"**{match.chunk.section}, {match.chunk.subsection}**")
            st.markdown("  \n".join(match.chunk.lines))
    else:
        st.warning(f"No matches found")
