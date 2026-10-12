
import pytest

from src.chunking import chunk_text


def test_chunk_text_without_overlap():

    text = "ABCDEFGHIJ"

    chunks = chunk_text(text, chunk_size=4, overlap=0)

    assert chunks == ["ABCD", "EFGH", "IJ"]


def test_chunk_text_with_overlap():

    text = "ABCDEFGHIJ"

    chunks = chunk_text(text, chunk_size=4, overlap=2)

    assert chunks == ["ABCD", "CDEF", "EFGH", "GHIJ"]


def test_chunk_text_empty_input():

    with pytest.raises(ValueError, match="text cannot be empty"):
        chunk_text("")


def test_chunk_size_must_be_positive():

    with pytest.raises(ValueError, match="chunk_size must be greater than zero"):
        chunk_text("ABCDEFGHIJ", chunk_size=0)


def test_overlap_must_be_smaller_than_chunk_size():

    with pytest.raises(ValueError, match="overlap must be smaller than chunk_size"):
        chunk_text("ABCDEFGHIJ", chunk_size=4, overlap=4)


def test_chunk_text_preserves_paragraphs_when_possible():

    text = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."

    chunks = chunk_text(text, chunk_size=40, overlap=0)

    assert chunks == [
        "First paragraph.\n\nSecond paragraph.\n\n",
        "Third paragraph."
    ]


def test_chunk_text_respects_chunk_size_with_overlap():

    text = "A" * 50

    chunks = chunk_text(text, chunk_size=20, overlap=5)

    assert all(len(chunk) <= 20 for chunk in chunks)


def test_chunk_text_preserves_all_text():

    text = "ABCDEFGHIJ"

    chunks = chunk_text(
        text,
        chunk_size=4,
        overlap=2
    )

    reconstructed_text = chunks[0]

    for chunk in chunks[1:]:
        reconstructed_text += chunk[2:]

    assert reconstructed_text == text


def test_overlap_cannot_be_negative():

    with pytest.raises(ValueError, match="overlap cannot be negative"):
        chunk_text("ABCDEFGHIJ", chunk_size=4, overlap=-1)


def test_text_must_be_a_string():

    with pytest.raises(TypeError, match="text must be a string"):
        chunk_text(123)


def test_chunk_text_preserves_all_text_with_paragraphs():

    text = (
        "First paragraph.\n\n"
        "Second paragraph.\n\n"
        "Third paragraph."
    )

    overlap = 5

    chunks = chunk_text(
        text,
        chunk_size=30,
        overlap=overlap
    )

    reconstructed_text = chunks[0]

    for chunk in chunks[1:]:
        reconstructed_text += chunk[overlap:]

    assert reconstructed_text == text


def test_chunk_text_splits_long_paragraph():

    text = "A" * 100

    chunks = chunk_text(
        text,
        chunk_size=20,
        overlap=5
    )

    assert len(chunks) > 1
    assert all(len(chunk) <= 20 for chunk in chunks)

    reconstructed_text = chunks[0]

    for chunk in chunks[1:]:
        reconstructed_text += chunk[5:]

    assert reconstructed_text == text
