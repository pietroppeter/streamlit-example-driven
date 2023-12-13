# streamlit-example-driven

a streamlit presentation for beginners:
- start with demo of `cerca` app from scratch
- then run streamlit multipage app

To run multipage app, from root folder run with:
```
streamlit run 1_🎈_Slides.py
```
single pages are implemented in `pages`,
but they mostly call a separate app from outside.

App implementations are in its own specific folders:
- `slides`: slides for presentation
- `cerca`: a simple information retrieval system
- `data_science`: data science use cases (clustering, data exploration)
- `elitza`: ELIZA chatbot

To run single app (e.g. cerca) first set PYTHONPATH to `.`,
e.g. on mac/linux:
```
export PYTHONPATH=.
```

then, from root folder:
```
streamlit run cerca/app.py
```
