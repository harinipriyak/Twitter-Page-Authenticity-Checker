import numpy
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

max_features = 1024
seed = 7
numpy.random.seed(seed)
# load dataset
dataset = numpy.loadtxt(r"C:\Users\Dheethaa\Desktop\dataset.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:, 0:11]
Y = dataset[:, 11]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=seed)
lb = LabelBinarizer()
y_test = lb.fit_transform(y_test)

model = Sequential()
model.add(Embedding(max_features, output_dim=256))
model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=16, epochs=10)
score = model.evaluate(x_test, y_test, batch_size=16)
print("loss:", score[0], "accuracy: ", score[1])