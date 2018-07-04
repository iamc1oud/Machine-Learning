from nltk.tokenize import sent_tokenize,word_tokenize,WordPunctTokenizer

# Input text
input_text = "Do you know me? If you know me, tell me the truth."

# Sentence tokenizer
print("Sentence Tokenizer:")
print(sent_tokenize(input_text))

# Word tokenize
print('Word Tokenizer: ')
print(word_tokenize(input_text))

# WordPunct Tokenizer
print('Word punct tokenizer:')
print(WordPunctTokenizer().tokenize(input_text))