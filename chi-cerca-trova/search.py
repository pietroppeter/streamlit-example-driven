from dataclasses import dataclass, field
from data import Corpus, Chunk


@dataclass
class Occurrence:
    line_index: int
    start_index: int
    end_index: int


@dataclass
class Match:
    chunk: Chunk
    occurrences: list[Occurrence] = field(default_factory=list)


def match(corpus: Corpus, pattern: str, case_sensitive=True, max_chunks=-1) -> list[Match]:
    """Matches a corpus with a pattern and returns a list of `Match` objects"""
    result = []
    num_chunks = 0
    for chunk in corpus.chunks:
        if max_chunks > 0 and num_chunks >= max_chunks:
            break
        found_match = False
        for line in chunk.lines:
            if case_sensitive:
                found_match = pattern in line
            else:
                found_match = pattern.lower() in line.lower()
            if found_match:
                result.append(Match(chunk=chunk))
                found_match = True
                num_chunks += 1
                break
        if found_match:
            continue

    return result
