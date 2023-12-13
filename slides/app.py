import streamlit as st
import reveal_slides as rs


st.set_page_config(page_title="Streamlit slides", page_icon="🎈", initial_sidebar_state="collapsed")


def fragment(i: int) -> str:
    return f'<!-- .element: class="fragment" data-fragment-index="{i}" -->'


slides_intro = f"""
# **Streamlit**
## Example-driven learning

[github.com/pietroppeter/streamlit-example-driven](https://github.com/pietroppeter/streamlit-example-driven)
---
## Outline

- 🕵️ **Demo** {fragment(0)}  
  _widgets, streamlit💡, cache_ {fragment(0)}
- 🧑‍🔬 **Data Science** {fragment(1)}  
  _data, plots, columns, ..._ {fragment(1)}
- 🤖 **ELIZA** {fragment(2)}  
  _chat, state, url parameters_ {fragment(2)}
- 🎈 **Slides** {fragment(3)}  
  _components, multipage apps_ {fragment(3)}

"""
leftout = """
<!--
slides: <a target="_blank" href="">todo</a>

source: <a target="_blank" href="">todo</a>
-->

<!--

- 🥷 advanced tips {fragment(4)}
- 🏰 streamlit history and alternatives {fragment(5)}

-->
"""
i_title = 0
i_agenda = 1
i_agenda_fragment_demo = 0
i_agenda_fragment_science = 1
i_agenda_fragment_eliza = 2
i_agenda_fragment_slides = 3
i_agenda_fragment_ninja = 4
i_agenda_fragment_streamlit = 5
i_last = i_agenda

slides_demo = """
---
## 🕵️ **Demo**
--
### widgets

```python
def app():
    ...

    st.title(...)
    st.markdown(...)

    show_max_chunks = st.sidebar.number_input(...) # ✨

    documents = [ corpus[name]
        for name in st.multiselect(...)] # ✨

    if len(documents) == 0:
        st.error(...)
        st.stop()

    query = st.text_input(...) # ✨
    case_sensitive = st.checkbox(...) # ✨
    if query:
        for document in documents:
            st.markdown(...)

            matches = search.match(document, query, ...)
            if matches:
                st.success(...)
                show_matches = ...
                if len(show_matches) < len(matches):
                    st.warning(...)
                for match in show_matches:
                    st.markdown(...)
            else:
                st.warning(...)
    else:
        st.markdown(...)
```

--
### streamlit 💡

First principle of streamlit:
**Embrace Scripting!**

- every time there is an interaction... ✨
- _...rerun the whole python script!_ 🤯
- backend and frontend magic 🧙 makes interactivity smooth!
--
### cache

What about _long computations_? **Cache them!**

```python
@st.cache_data # 🔮
def load_corpus():
    corpus = data.load_corpus()
    return corpus


def app():
    corpus = load_corpus()
    ...
```
"""
i_demo = i_last + 1
i_demo_vertical_title = 0
i_demo_vertical_widgets = 1
i_demo_vertical_idea = 2
i_demo_vertical_cache = 3
i_last = i_demo

slides_data = """
---
## 🧑‍🔬 **Data Science**
--
### data
```python
def app()
    ...

    which_load = st.radio("Load data",
        ["Sample files", "Upload file"], horizontal=True)
    if which_load == "Sample files":
        which_img = st.selectbox("Pick an image",
            options=["flower.jpg", "china.jpg"])
        img = load_sample_image(which_img)
    else:
        uploaded_file = st.file_uploader("Upload an image file", accept_multiple_files=False, type=["png", "jpg"])
        if not uploaded_file:
            st.stop()
        else:
            ...
```

--
### plots (and tabs)
```python
tab1, tab2, tab3 = st.tabs(["Builtin (Altair)", ...])
with tab1:
    st.scatter_chart(df, x=feat1, y=feat2)
with tab2:
    fig = px.scatter(df, x=feat1, y=feat2)
    st.plotly_chart(fig, use_container_width=True)
with tab3:
    fig, ax = plt.subplots()
    ax.scatter(df[feat1], df[feat2])
    st.pyplot(fig)
```
--
### columns

```python
st.write("Pick two features")
col1, col2, _ = st.columns(3)
feat1 = col1.selectbox("Feature 1", df.columns)
feat2 = col2.selectbox("Feature 2", [c for c in df.columns if c != feat1])
```

or

```python
        col1, _ = st.columns([1, 3])
        with col1:
            which_data = st.selectbox(...)
```
"""
ih_data = i_last + 1
i_last = ih_data

slides_eliza = """
---
## 🧑‍🔬 **ELIZA**
--
### chat / state (past messages)
`st.chat_message` and `st.session_state`

```python
eliza = load_eliza()
...
if "messages" not in st.session_state:
    st.session_state.messages = []
... # initial message
if not st.session_state.messages:
    st.session_state.messages.append(
        {"role": "assistant", "content": eliza.initial()}
    )
... # show past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
...
```
--
### chat / state (new messages)
`st.chat_input` (and `st.session_state`)

```python
...
if prompt := st.chat_input("What is up?"):
    # append my response
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = eliza.respond(prompt)
    if response is None: # final message
        with st.chat_message("assistant"):
            st.markdown(eliza.final())
        ...
    else: # append next eliza's response
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
```
--
### state (stopped)
at the beginning:
```python
if "stopped" not in st.session_state:
    st.session_state.stopped = False
```
at the end:
```python
if st.session_state.stopped:
    st.markdown("Conversation with Eliza has ended.")
    if st.button("Bookmark the conversation as url"):
        ...
    if st.button("Restart"):
        st.session_state.messages = []
        st.session_state.stopped = False
        st.rerun()
    st.stop()

if prompt := st.chat_input("What is up?"):
    ...
    response = eliza.respond(prompt)
    if response is None:
        ...
        st.session_state.stopped = True
        st.rerun()
```
--
### url parameters
at the beginning:
```python
if "encoded_messages" in st.experimental_get_query_params():
    encoded_messages = st.experimental_get_query_params(
        )["encoded_messages"][0]
    st.experimental_set_query_params()
    st.session_state.messages = decode(encoded_messages)
```
towards the end:
```python
if st.button("Bookmark the conversation as url"):
    encoded_messages = encode(st.session_state.messages)
    st.experimental_set_query_params(
        encoded_messages=encoded_messages)
```

"""
ih_eliza = i_last + 1
i_last = ih_eliza

slides_reveal = """
---
## 🧑‍🔬 **Slides** [reveal.js]()
--
### components
```
...
```

--
### multipage apps
```python
...
```

"""
ih_reveal = i_last + 1
i_last = ih_reveal


slides_markdown = slides_intro + slides_demo + slides_data + slides_eliza + slides_reveal

# change this while developing to start in the appropriate place
indexh = ih_eliza
indexv = 3
indexf = 0

def app():
    with st.sidebar:
        st.subheader("Slides component parameters")
        theme_default = "dracula"
        theme_options = [
            "black",
            "black-contrast",
            "blood",
            "dracula",
            "moon",
            "white",
            "white-contrast",
            "league",
            "beige",
            "sky",
            "night",
            "serif",
            "simple",
            "solarized",
        ]
        theme = st.selectbox(
            "Theme", theme_options, index=theme_options.index(theme_default)
        )

        transition = st.selectbox(
            "Transition", ["slide", "convex", "concave", "zoom", "none"]
        )

        # height = st.number_input("Height", value=500)
        height = 500
        # content_height = st.number_input("Content Height", value=900)
        content_height = 900
        # content_width = st.number_input("Content Width", value=900)
        content_width = 900
        # scale_range = st.slider("Scale Range", min_value=0.0, max_value=5.0, value=[0.1, 3.0], step=0.1)
        scale_range = [0.1, 3.0]
        # margin = st.slider("Margin", min_value=0.0, max_value=0.8, value=0.1, step=0.05)
        margin = 0.1
        # plugins = st.multiselect("Plugins", ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"], [])
        plugins = ["highlight", "katex"]

    currState = rs.slides(
        slides_markdown,
        height=height,
        theme=theme,
        config={
            "transition": transition,
            "width": content_width,
            "height": content_height,
            "minScale": scale_range[0],
            "center": True,
            "maxScale": scale_range[1],
            "margin": margin,
            "plugins": plugins,
        },
        initial_state={
            "indexh": indexh, 
            "indexv": indexv, 
            "indexf": indexf, 
            }, 
        markdown_props={"data-separator-vertical": "^--$"},
        key="foo",  # what is this about?
    )

    if currState["indexh"] == i_title:
        # todo add link (also to reveal?)
        st.markdown(
            "Slides made with [streamlit-reveal-slides](https://github.com/bouzidanas/streamlit-reveal-slides).  \nSee sidebar for changing `theme` and `transition`."
        )
        st.markdown("Press `F` for full screen, `Esc` to exit full screen.")
    elif currState["indexh"] == i_agenda:
        if currState["indexf"] == i_agenda_fragment_demo:
            st.markdown("") # todo fragment 1?
        elif currState["indexf"] == i_agenda_fragment_science:
            st.markdown("") # todo fragment 2?
    elif currState["indexh"] == i_demo:
        if currState["indexv"] == i_demo_vertical_title:
            st.markdown("") # todo details of steps
        elif currState["indexv"] == i_demo_vertical_widgets:
            st.markdown("") # todo link to more widgets


if __name__ == "__main__":
    app()
