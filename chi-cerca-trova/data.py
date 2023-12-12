"""Module to load corpora for information retrieval

Run python data.py to run tests
"""
from dataclasses import dataclass, field


@dataclass
class Chunk:
    section: str = ""
    subsection: str = ""
    lines: list[str] = field(default_factory=list)


@dataclass
class Corpus:
    title: str = ""
    author: str = ""
    chunks: list[Chunk] = field(default_factory=list)


def read_file(filename: str) -> str:
    """Generic utility function to read a text file"""
    with open(filename, "r") as f:
        return f.read()


def load_commedia() -> Corpus:
    """Load Corpus of Divina Commedia"""
    def is_empty(line):
        return line.strip() == ""
    
    def is_metadata_line(i, lines):
        return i > 1 and len(lines) > i + 2 and is_empty(lines[i + 1]) and is_empty(lines[i + 2]) and is_empty(lines[i - 1]) and is_empty(lines[i - 2])

    text = read_file("commedia.txt")
    result = Corpus(title="Divina Commedia", author="Dante Alighieri")
    lines = text.splitlines()
    chunk_lines = []
    section = ""
    subsection = ""

    for i, line in enumerate(lines):
        if is_empty(line):
            if chunk_lines:
                chunk = Chunk(section=section, subsection=subsection, lines=chunk_lines)
                result.chunks.append(chunk)
                chunk_lines = []

        elif is_metadata_line(i, lines):
            if chunk_lines:
                chunk = Chunk(section=section, subsection=subsection, lines=chunk_lines)
                result.chunks.append(chunk)
                section, subsection, chunk_lines = "", "", []
            try:
                section, subsection = [s.strip() for s in line.split("•")]
            except ValueError:
                import streamlit as st
                st.write(line)
        else:
            chunk_lines.append(line)
    
    return result


if __name__ == "__main__":
    # tests
    commedia = load_commedia()
    assert commedia.title.lower().startswith("divina")
    assert commedia.author.lower().startswith("dante")
    assert len(commedia.chunks) > 10
    sections = set()
    for chunk in commedia.chunks:
        assert len(chunk.section) > 0
        assert len(chunk.subsection) > 0
        assert len(chunk.lines) > 0
        sections.add(chunk.section)
    print(f"{len(commedia.chunks)=}")
    print(f"{sections=}")
    for section in sections:
        n_chunks = len([c for c in commedia.chunks if c.section == section])
        n_subsections = len({c.subsection for c in commedia.chunks})
        print(f"{section}: {n_subsections=}, {n_chunks=}")