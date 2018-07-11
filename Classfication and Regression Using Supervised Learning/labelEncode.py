import numpy as np
from sklearn import preprocessing

# input labels
input_labels = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']

# creating a label encoder and fitting the labels
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

# print the mapping
print('Label mapping')
for i, item in enumerate(encoder.classes_):
	print(item, '==>', i)

# encode a set of labels using the encoder
test_labels = ['green', 'red',  'black']
encoded_values = encoder.transform(test_labels)
print("Encoded values =", list(encoded_values))

# decode a set of values using the encoder
encoded_values = [3,0,4,1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values = ", encoded_values)
print("Decoded values = ", list(decoded_list))

