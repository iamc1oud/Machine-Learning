import random
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy as nltk_accuracy
from nltk.corpus import names


def extract_features(word, N=2):
    last_n_letters = word[-N:]
    return {'feature':last_n_letters.lower()}

'''
x = extract_features('Ajay')
print(x)

Output:
{'feature': 'ay'}
'''

if __name__ == '__main__':
    # creating training data using labelled names available in nltk
    males_list = [(name,'male') for name in names.words('male.txt')]
    females_list = [(name,'female') for name in names.words('female.txt')]
    data = (males_list + females_list)      # 7944 Names
    random.seed(5)
    random.shuffle(data)

    # test data
    input_names = ['Alexander','Ajay','Jyoti','Rahul','Veronica','Julia']

    num_train = int(0.8*len(data))

    features = [(extract_features(n,2), gender) for (n, gender) in data]
    train_data, test_data = features[:num_train], features[num_train:]
    classifier = NaiveBayesClassifier.train(train_data)

    # computing the accuracy
    accuracy = round(100 * nltk_accuracy(classifier, test_data),2)
    print('Accuracy = ' + str(accuracy) + '%')

    # prediction
    for name in input_names:
        print(name, '==>', classifier.classify(extract_features(name,2)))
    
