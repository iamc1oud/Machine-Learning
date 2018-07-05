from nltk.stem import WordNetLemmatizer
import nltk


nltk.download('wordnet')
input_words = ['swimming']

lemmatizer = WordNetLemmatizer()

# List of lemmatizer names for display
lemmatizer_names = ['NOUN LEMMATIZER','VERB LEMMATIZER']
formatted_text = '{:>24}'* (len(lemmatizer_names)+1)
print(formatted_text.format('INPUT WORD',*lemmatizer_names))
print('='*78)

# Iterate though each word
for word in input_words:
    output = [word,lemmatizer.lemmatize(word,pos='n'),lemmatizer.lemmatize(word, pos='v')]
    print(formatted_text.format(*output))
