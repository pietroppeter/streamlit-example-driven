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


def match(corpus: Corpus, pattern: str, max_chunks=10) -> list[Match]:
    """Matches a corpus with a pattern and returns a list of `Match` objects"""
    result = []
    num_chunks = 0
    for chunk in corpus.chunks:
        if num_chunks >= max_chunks:
            break
        found_match = False
        for line in chunk.lines:
            if pattern in line:
                result.append(Match(chunk=chunk))
                found_match = True
                num_chunks += 1
                break
        if found_match:
            continue

    return result
