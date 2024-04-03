import pytest
from words_counter import words_counter


@pytest.fixture
def sample_text_file(tmp_path):
    sample_text = "Apple ok hello tree home door.And second rand!And to be.A this last?Apple,apple,apple."
    file_path = tmp_path / "sample.txt"
    with open(file_path, 'w') as f:
        f.write(sample_text)
    return file_path

@pytest.mark.parametrize("input_file, expected_words, expected_sentences", [
    ("sample.txt", 18, 6), 

])
def test_words_counter(input_file, expected_words, expected_sentences):

    num_words, num_sentences = words_counter(input_file)
    assert num_words == expected_words
    assert num_sentences == expected_sentences


