import streamlit as st
import reveal_slides as rs

def fragment(i: int) -> str:
    return f"<!-- .element: class=\"fragment\" data-fragment-index=\"{i}\" -->"

slides_intro = f"""
# [Streamlit]()
## Example-driven learning
slides: <a target="_blank" href="">todo</a>

source: <a target="_blank" href="">todo</a>

---
## Agenda

- 🕵️ **Demo** {fragment(0)}  
  _basic widgets, streamlit flow, cache_ {fragment(0)}
- 🧑‍🔬 **Data Science** {fragment(1)}  
  _image, charts, plots, columns_ {fragment(1)}
- 🤖 **ELIZA** {fragment(2)}  
  _chat, state, url parameters_ {fragment(2)}
- 🎈 **Slides** {fragment(3)}  
  _components, multipage apps_ {fragment(3)}
- 🥷 advanced tips {fragment(4)}
- 🏰 streamlit history and alternatives {fragment(5)}
---
## demo cerca

todo summary of steps
--
todo summary of widgets

-> add action to exit full screen from slides (this is the first time we go out)
"""
i_title = 0
i_agenda = 1
i_agenda_fragment_demo = 0
i_agenda_fragment_science = 1
i_agenda_fragment_eliza = 2
i_agenda_fragment_slides = 3
i_agenda_fragment_ninja = 4
i_agenda_fragment_streamlit = 5

i_demo = 2
i_demo_vertical_steps = 0
i_demo_vertical_widgets = 1

slides_main = r"""

"""

slides_markdown = slides_intro + slides_main


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
        markdown_props={"data-separator-vertical": "^--$"},
        key="foo", # what is this about?
    )

    if currState["indexh"] == i_title:
        # todo add link (also to reveal?)
        st.markdown(
            "Slides made with [streamlit-reveal-slides](https://github.com/bouzidanas/streamlit-reveal-slides).  \nSee sidebar for changing `theme` and `transition`."
        )
        st.markdown("Press `F` for full screen, `Esc` to exit full screen.")
    elif currState["indexh"] == i_agenda:
        if currState["indexf"] == i_agenda_fragment_demo:
            st.markdown("todo fragment 1")
        elif currState["indexf"] == i_agenda_fragment_science:
            st.markdown("todo fragment 2")
    elif currState["indexh"] == i_demo:
        if currState["indexv"] == i_demo_vertical_steps:
            st.markdown("todo details of steps")
        elif currState["indexv"] == i_demo_vertical_widgets:
            st.markdown("todo link to more widgets")


if __name__ == "__main__":
    app()
