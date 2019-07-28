# Create first network with Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
from sklearn.model_selection import train_test_split

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load dataset
dataset = numpy.loadtxt(r"C:\Users\HARINI PRIYA\FYP\Final_Dataset.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:11]
Y = dataset[:,11]
# split into 80% for train and 20% for test
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=seed)

# create model
model = Sequential()
model.add(Dense(20, input_dim=11, init='normal', activation='relu'))
model.add(Dense(16, input_dim=11, init='normal', activation='relu'))
model.add(Dense(16, input_dim=11, init='normal', activation='relu'))
model.add(Dense(1, init='normal', activation='sigmoid'))
# Compile model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X_train, y_train, validation_data=(X_test,y_test), epochs=150, batch_size=50)

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

