# chi-cerca-trova (kee chair-kah truh-vah)

Small demo app for a minimal
[information retrieval](https://en.wikipedia.org/wiki/Information_retrieval) system
built with streamlit.

Corpus is two cassics of Italian literature, widely studied at schoool:
- Divina Commedia by Dante Alighieri
- Orlando Furioso by Ludovico Ariosto

Sources are taken from gutenberg project.

Each corpus is processed in **chunks** and every chunk has associated metadata.

Modules:
- `data.py`: functionalities to load corpora
- `search.py`: functionalities to search in corpora
- `app.py`: streamlit app that implements a full stack minimal information retrieval system

"chi-cerca-trova" means "he who seeks shall find" in Italian.
