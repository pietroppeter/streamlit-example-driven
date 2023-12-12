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
- load `commedia = data.load_commedia()`
- show `st.write(commedia)`
- mention magic alternative (just `commedia`)

discovery of search module...

### step 2 - mvp

build basic search

```py
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
```

### step 3 - more widgets

more corpora:
- selectbox

more options:
- control max matches (number_input)
- control case sensitivity (checkbox)

- multiselect?

### step 4 - beautify

improve layout/formatting:

- expander
- match colors?

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
  - st.number_input
  - st.selectbox
  - st.checkbox
- layout elements:
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
