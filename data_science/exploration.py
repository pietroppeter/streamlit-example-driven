import streamlit as st
import pandas as pd
import numpy as np
from sklego.datasets import load_penguins
import plotly.express as px
import matplotlib.pyplot as plt


title = "📊 Data Exploration"


def app():
    st.title(title)
    which_load = st.radio("Load data", ["Sample files", "Upload file"], horizontal=True)

    if which_load == "Sample files":
        col1, _ = st.columns([1, 3])
        which_data = col1.selectbox(
            "Pick a dataset",
            options=[
                "Random",
                "Penguins",
            ],
        )
    else:
        uploaded_file = st.file_uploader(
            "Upload a data file", accept_multiple_files=False, type=["csv"]
        )
        if not uploaded_file:
            st.stop()
        else:
            pass  # todo implement processing

    if which_data == "Random":
        df = pd.DataFrame(
            {
                "A": np.random.randn(24),
                "B": np.random.randint(2, 10, 24),
                "C": [
                    np.random.choice(["rand_1", "rand_2", "rand_4", "rand_6"])
                    for i in range(24)
                ],
                "D": ["spam", "eggs", "spam", "eggs"] * 6,
                "E": ["alpha", "beta", "gamma"] * 8,
                #'F' : [np.random.choice(pd.date_range(datetime.datetime(2013,1,1),datetime.datetime(2013,1,3))) for i in range(24)],
            }
        )
    elif which_data == "Penguins":
        df = load_penguins(as_frame=True)

    st.write("Here is a peek into the dataset:")
    st.write(df.head())

    st.write("Pick two features")
    col1, col2, _ = st.columns(3)
    feat1 = col1.selectbox("Feature 1", df.columns)
    feat2 = col2.selectbox("Feature 2", [c for c in df.columns if c != feat1])

    tab1, tab2, tab3 = st.tabs(["Builtin (Altair)", "Plotly", "Matplotlib"])
    with tab1:
        st.scatter_chart(df, x=feat1, y=feat2)
    with tab2:
        fig = px.scatter(df, x=feat1, y=feat2)
        st.plotly_chart(fig, use_container_width=True)
    with tab3:
        fig, ax = plt.subplots()
        ax.scatter(df[feat1], df[feat2])
        st.pyplot(fig)


if __name__ == "__main__":
    app()
