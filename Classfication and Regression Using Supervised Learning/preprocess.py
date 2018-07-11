import numpy as np
from sklearn import preprocessing

# some sample data
input_data = np.array([[5.1, -2.9, 3.3],[-1.2, 7.8, -6.1],[3.9,0.4,2.1],[7.3,-9.9,-4.5]])
print(input_data)
# binarizatin method
data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data)
print(data_binarized)
# mean removal
print('\nBefore')
print('Mean =', input_data.mean(axis=0))
print('Standard deviation =', input_data.std(axis=0))

# let's remove the mean
data_scaled = preprocessing.scale(input_data)
print('After')
print('Mean =', data_scaled.mean(axis=0))
print('Standard deviation =', data_scaled.std(axis=0))

# min max scaling
data_scaler_minmax = preprocessing.MinMaxScaler((0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print('Min max scaled data:')
print(data_scaled_minmax)

# normaliation
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
print('L1 normalization:', data_normalized_l1)
print('L2 normalization:', data_normalized_l2)

