# Modules
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

category = {'talk.politics.misc':'Politics','rec.autos':'Autos',
            'rec.sport.hockey':'Hockey','sci.electronics':'Electronics',
            'sci.med':'Medicine'}

# More groups are
'''
'alt.atheism',
 'comp.graphics',
 'comp.os.ms-windows.misc',
 'comp.sys.ibm.pc.hardware',
 'comp.sys.mac.hardware',
 'comp.windows.x',
 'misc.forsale',
 'rec.autos',
 'rec.motorcycles',
 'rec.sport.baseball',
 'rec.sport.hockey',
 'sci.crypt',
 'sci.electronics',
 'sci.med',
 'sci.space',
 'soc.religion.christian',
 'talk.politics.guns',
 'talk.politics.mideast',
 'talk.politics.misc',
 'talk.religion.misc'

 '''

# Training dataset fetch
training_data = fetch_20newsgroups(subset='train',categories=category.keys(), shuffle=True, random_state= 5)

# Build a count vectorizer and extract term counts
count_vectorizer = CountVectorizer()
train_tc = count_vectorizer.fit_transform(training_data.data)
print('Dimensions of training data:', train_tc.shape)

# Create the tf-idf transformer
tfidf = TfidfTransformer()
train_tfidf = tfidf.fit_transform(train_tc)

# test data
'''
input_data = ['You need to be careful with cars when you are driving on slippery roads.',
            'A lot of electronics devices can be operated wirelessly.',
            'Players need to be careful when they are close to goal posts.',
            'Political debates helps us to understand about our country.',
            'Lamborghini is very fast.', 'I had used arduino in my project.']
'''
while True:
    input_data = []
    text = raw_input('Enter a text:')
    input_data.append(text)
    # train a multinomial naive bayes classifier
    classifier = MultinomialNB().fit(train_tfidf, training_data.target)

    # transform input data using count vectorizer
    input_tc = count_vectorizer.transform(input_data)

    # transform vectorized data using tfidf transformer
    input_tfidf = tfidf.transform(input_tc)

    # predict the output categories
    predictions = classifier.predict(input_tfidf)

    # output
    for sent, category_map in zip(input_data, predictions):
        print('Input:', sent, ' Predicted category:', category[training_data.target_names[category_map]])
