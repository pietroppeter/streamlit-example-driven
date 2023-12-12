# chi-cerca-trova (kee chair-kah truh-vah)

Small demo app for a minimal
[information retrieval](https://en.wikipedia.org/wiki/Information_retrieval) system
built with streamlit.

Corpora are three cassics of Italian literature, widely studied at schoool:
- Divina Commedia by Dante Alighieri
- Promessi Sposi by Alessandro Manzoni
- Orlando Furioso by Ludovico Ariosto

Sources are taken from gutenberg project:
- https://www.gutenberg.org/ebooks/1012
- https://www.gutenberg.org/ebooks/3747
- https://www.gutenberg.org/ebooks/45334
in the repo we have both a copy of original gutenberg txt file
and a trimmed down version for easier processing.

Each corpus is processed in **chunks** and every chunk has associated metadata.

Modules:
- `data.py`: functionalities to load corpora
- `search.py`: functionalities to search in corpora
- `app.py`: streamlit app that implements a full stack minimal information retrieval system

"chi-cerca-trova" means "he who seeks shall find" in Italian.
