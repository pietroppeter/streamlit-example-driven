import streamlit as st
import reveal_slides as rs

slides_markdown = r"""
# Streamlit
## Example-driven learning
add link to <a target="_blank" href="https://revealjs.com/">slides</a>
---
## Installation
`pip install streamlit-reveal-slides`
---
## Presentation Features
- Create slides from markdown or markup <!-- .element: class="fragment" data-fragment-index="0" -->
- Touch, mouse, and keyboard navigation <!-- .element: class="fragment" data-fragment-index="1" -->
- Fullscreen and overview modes <!-- .element: class="fragment" data-fragment-index="2" -->
- Search and Zoom (plugins) <!-- .element: class="fragment" data-fragment-index="3" -->
- Display LaTeX and syntax highlighted code (plugins) <!-- .element: class="fragment" data-fragment-index="4" -->
"""


def app():
  with st.sidebar:
      st.header("Component Parameters")
      theme = st.selectbox("Theme", ["black", "black-contrast", "blood", "dracula", "moon", "white", "white-contrast", "league", "beige", "sky", "night", "serif", "simple", "solarized"])
      height = st.number_input("Height", value=500)
      st.subheader("Slide Configuration")
      content_height = st.number_input("Content Height", value=900)
      content_width = st.number_input("Content Width", value=900)
      scale_range = st.slider("Scale Range", min_value=0.0, max_value=5.0, value=[0.1, 3.0], step=0.1)
      margin = st.slider("Margin", min_value=0.0, max_value=0.8, value=0.1, step=0.05)
      transition = st.selectbox("Transition", ["slide", "convex", "concave", "zoom", "none"])
      plugins = st.multiselect("Plugins", ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"], [])
      st.subheader("Initial State")
      hslidePos = st.number_input("Horizontal Slide Position", value=0)
      vslidePos = st.number_input("Vertical Slide Position", value=0)
      fragPos = st.number_input("Fragment Position", value=-1)
      overview = st.checkbox("Show Overview", value=False)
      paused = st.checkbox("Pause", value=False)

  currState = rs.slides(slides_markdown, 
                      height=height, 
                      theme="dracula", 
                      config={
                              "transition": transition,
                              "width": content_width, 
                              "height": content_height, 
                              "minScale": scale_range[0], 
                              "center": True, 
                              "maxScale": scale_range[1], 
                              "margin": margin, 
                              "plugins": plugins
                              }, 
                      initial_state={
                                      "indexh": hslidePos, 
                                      "indexv": vslidePos, 
                                      "indexf": fragPos, 
                                      "paused": paused, 
                                      "overview": overview 
                                      }, 
                      markdown_props={"data-separator-vertical":"^--$"}, 
                      key="foo")

  if currState["indexh"] == 0:
      st.markdown("Reveal.js is an open source HTML presentation framework. It enables anyone with a web browser to create fully-featured and beautiful presentations for free. \n\nThe framework comes with a broad range of features including nested slides, Markdown support, Auto-Animate, PDF export, speaker notes, LaTeX support and syntax highlighted code.")
  elif currState["indexh"] == 2:
      if currState["indexf"] == 0:
          st.markdown("_(see later slides for details and examples)_")
      elif currState["indexf"] == 1:
          st.markdown("- You can swipe horizontally or vertically to navigate through a presentation on any touch-enabled device. \n- You can use the arrow keys on your keyboard to navigate as well. \n- Navigating with the mouse is as simple as clicking the directional arrows near the edges or corners of the slides.")
      elif currState["indexf"] == 2:
          st.markdown("- Press the `F` key on your keyboard to enter full-screen presentation mode. Press `ESC` to exit full-screen mode. \n- Press the `O` of `ESC` key to enter and exit overview mode")
      elif currState["indexf"] == 3:
          st.write(":arrow_left: Make sure to add the search and zoom plugins to activate these features.")
          st.markdown("- Press `Ctrl` + `Shift` + `F` keys on your keyboard to open and close the search dialog. \n- Press the `Alt` key and right click to zoom in and out on the region the mouse is hovering over.")
      elif currState["indexf"] == 4:
          st.markdown("_(see later slides for details and examples)_")


if __name__ == "__main__":
    app()