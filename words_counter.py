def words_counter(filename):
    with open(filename, 'r') as file:
        text = file.read()

    sentence_rozdilniks = ['.', '!', '?', '...']
    word_rozdilniks = [',', ' ', ':', ';']

    num_sentences = 0
    for char in text:
        if char in sentence_rozdilniks:
            num_sentences += 1

    words = text.split()
    for word in words:
        if any(char in word_rozdilniks for char in word):
            num_sentences += 1

    num_words = len(words) + num_sentences
    return num_words, num_sentences

filename = 'text.txt' 
num_words, num_sentences = words_counter(filename)

