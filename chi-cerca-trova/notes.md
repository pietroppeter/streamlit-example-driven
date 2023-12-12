## demo script

### step 0 - workflow

start with minimal app

```py
import streamlit as st

st.title("Chi cerca trova")
```

- then add a bit of explanatory text
- show rerun
- change again text
- turn on auto rerun

### step 1 - discovery

discovery of data module

- import data
- show `st.write(data)` comment `load_commedia``
- load `document = data.load_commedia()`
- show `st.write(document)`
- mention magic alternative (just `document`)

discovery of search module...

use also for streamlit commands!
- e.g. st.title, st.markdown, st.selectbox, ...

### step 2 - mvp

build basic search

```py
import streamlit as st
import data
import search

st.title("Chi cerca trova")
st.markdown("""
Information retrieval system for search in Italian literature corpora.
""")
corpus = data.load_commedia()
st.markdown(f"Current corpus is {corpus.title}")

query = st.text_input("Search query")
if query:
  matches = search.match(corpus, query)
  if matches:
    st.success(f"Found {len(matches)} matches")
    for match in matches:
      st.markdown(f"**{match.chunk.section}, {match.chunk.subsection}**")
      st.markdown("  \n".join(match.chunk.lines))
  else:
    st.warning(f"No matches found")
```

### step 3 - more widgets

- control case sensitivity (checkbox)
- control show max matches (number_input)
  - pagination: skip and leave as exercise for the reader
- more corpora: selectbox first, then multiselect (separated by )


```py
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
```

when using single selectbox:
```py
...
document = corpus[st.selectbox("Document", corpus.keys())]
...
```
### step 4 - beautify

improve layout/formatting:

- expander
- match colors?
- emoji! (and subheader)

### summary

in the demo we have covered
- text elements:
  - st.title
  - st.markdown
- debug:
  - st.write
  - magic
- input elements:
  - st.text_input
  - st.checkbox
  - st.number_input
  - st.selectbox
  - st.multiselect
- simple layout elements:
  - st.sidebar
  - st.expander

## later

- mention chart and data
  - stats of coprpora!
- cache!!!
- state management (session_state)
- more layout (columns!)
- button (later)

at the end:
- elitza to show chat elements
