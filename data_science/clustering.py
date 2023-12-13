import streamlit as st
from time import time

import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans
from sklearn.datasets import load_sample_image
from sklearn.metrics import pairwise_distances_argmin
from sklearn.utils import shuffle


title = "🖼️ Clustering colors"


def app():
    st.title(title)
    st.markdown(
        "Streamlit port of [scikit-learn example](https://scikit-learn.org/stable/auto_examples/cluster/plot_color_quantization.html) _Color Quantization using K-means_"
    )

    which_load = st.radio("Load data", ["Sample files", "Upload file"], horizontal=True)
    if which_load == "Sample files":
        which_img = st.selectbox(
            "Pick an image",
            options=[
                "flower.jpg",
                "china.jpg",
            ],
        )
        img = load_sample_image(which_img)
    else:
        uploaded_file = st.file_uploader(
            "Upload an image file", accept_multiple_files=False, type=["png", "jpg"]
        )
        if not uploaded_file:
            st.stop()
        else:
            pass  # todo implement processing

    # Convert to floats instead of the default 8 bits integer coding. Dividing by
    # 255 is important so that plt.imshow behaves works well on float data (need to
    # be in the range [0-1])
    img_float = np.array(img, dtype=np.float64) / 255
    st.image(img_float)  # works the same as img!

    # Load Image and transform to a 2D numpy array.
    w, h, d = original_shape = tuple(img_float.shape)
    assert d == 3
    img_array = np.reshape(img_float, (w * h, d))

    n_colors = st.number_input("How many colors?", min_value=2, max_value=256, value=4)

    st.write("Fitting model on a small sub-sample of the data")
    t0 = time()
    img_array_sample = shuffle(img_array, random_state=0, n_samples=1_000)
    kmeans = KMeans(n_clusters=n_colors, n_init="auto", random_state=0).fit(
        img_array_sample
    )
    st.write(f"done in {time() - t0:0.3f}s.")

    # Get labels for all points
    st.write("Predicting color indices on the full image (k-means)")
    t0 = time()
    labels = kmeans.predict(img_array)
    st.write(f"done in {time() - t0:0.3f}s.")

    st.write(f"### Quantized image ({n_colors} colors, K-Means)")
    st.image(recreate_image(kmeans.cluster_centers_, labels, w, h))

    # random color selection
    codebook_random = shuffle(img_array, random_state=0, n_samples=n_colors)
    st.write("Predicting color indices on the full image (random)")
    t0 = time()
    labels_random = pairwise_distances_argmin(codebook_random, img_array, axis=0)
    st.write(f"done in {time() - t0:0.3f}s.")

    st.write(f"### Quantized image ({n_colors} colors, Random)")
    st.image(recreate_image(codebook_random, labels_random, w, h))


def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    return codebook[labels].reshape(w, h, -1)


if __name__ == "__main__":
    app()
