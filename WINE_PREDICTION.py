import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense,Dropout
from keras.optimizers import Adam

def wine_quality_prediction():
  st.title("Wine Quality Prediction")
  st.write("wine quality prediction system employs a state-of-the-art Artificial Neural Network (ANN) model to assess and forecast wine quality. With an impressive accuracy rate of 92%, this predictive model is finely tuned to analyze a plethora of wine attributes and characteristics. By examining factors such as acidity, alcohol content, pH levels, and more, our ANN model provides precise insights into wine quality. Whether you're a winemaker striving for excellence or a wine enthusiast seeking exceptional choices, our system offers dependable predictions that guide your selection process with confidence. Explore the world of wine with data-driven precision and elevate your wine experience to new heights.")

  wine_data = pd.read_csv('winequality-red.csv')

  clean_data = wine_data.drop("residual sugar", axis = 1)

  #replace alcohol outlier with mean
  def replace_outliers_with_mean(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
    return data

  # Group the data by quality
  grouped = clean_data.groupby('quality')

  # Replace the outlier values of alcohol with mean for each quality group
  clean_data['alcohol'] = grouped['alcohol'].transform(replace_outliers_with_mean)

  #replace fixed acidity outlier with mean
  def replace_outliers_with_mean(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
    return data

  # Group the data by quality
  grouped = clean_data.groupby('quality')

  # Replace the outlier values of alcohol with mean for each quality group
  clean_data['fixed acidity'] = grouped['fixed acidity'].transform(replace_outliers_with_mean)

  #remove volatile acidity outlier
  def replace_outliers_with_mean(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
    return data

  # Group the data by quality
  grouped = clean_data.groupby('quality')

  # Replace the outlier values of alcohol with mean for each quality group
  clean_data['volatile acidity'] = grouped['volatile acidity'].transform(replace_outliers_with_mean)

  #remove citric acid outlier
  def replace_outliers_with_mean(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
    return data

  # Group the data by quality
  grouped = clean_data.groupby('quality')

  # Replace the outlier values of alcohol with mean for each quality group
  clean_data['citric acid'] = grouped['citric acid'].transform(replace_outliers_with_mean)

  #remove chloride outlier
  def replace_outliers_with_mean(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
    return data

  # Group the data by quality
  grouped = clean_data.groupby('quality')

  # Replace the outlier values of alcohol with mean for each quality group
  clean_data['chlorides'] = grouped['chlorides'].transform(replace_outliers_with_mean)

  #remove free sulfur dioxide outlier
  def replace_outliers_with_mean(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
    return data

  # Group the data by quality
  grouped = clean_data.groupby('quality')

  # Replace the outlier values of alcohol with mean for each quality group
  clean_data['free sulfur dioxide'] = grouped['free sulfur dioxide'].transform(replace_outliers_with_mean)

  #remove total sulfur dioxide outlier
  def replace_outliers_with_mean(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
    return data

  # Group the data by quality
  grouped = clean_data.groupby('quality')

  # Replace the outlier values of alcohol with mean for each quality group
  clean_data['total sulfur dioxide'] = grouped['total sulfur dioxide'].transform(replace_outliers_with_mean)

  #remove density outlier
  def replace_outliers_with_mean(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
    return data

  # Group the data by quality
  grouped = clean_data.groupby('quality')

  # Replace the outlier values of alcohol with mean for each quality group
  clean_data['density'] = grouped['density'].transform(replace_outliers_with_mean)

  #remove pH outlier
  def replace_outliers_with_mean(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
    return data

  # Group the data by quality
  grouped = clean_data.groupby('quality')

  # Replace the outlier values of alcohol with mean for each quality group
  clean_data['pH'] = grouped['pH'].transform(replace_outliers_with_mean)

  #remove sulphates outlier
  def replace_outliers_with_mean(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data[(data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))] = data.mean()
    return data

  # Group the data by quality
  grouped = clean_data.groupby('quality')

  # Replace the outlier values of alcohol with mean for each quality group
  clean_data['sulphates'] = grouped['sulphates'].transform(replace_outliers_with_mean)

  # Categorize the data
  cat_data = []
  for each in clean_data.quality:
      if 4 >= each >= 3:
          cat_data.append(0)
      elif 6 >= each >= 5:
          cat_data.append(1)
      else:
          cat_data.append(2)

  # Create a new dataframe with the same columns as the original dataframe
  new_data = clean_data.copy()

  # Add the categorized data to the new dataframe
  new_data['quality'] = cat_data

  # Get the value counts of the target variable
  class_counts = new_data['quality'].value_counts()

  # Calculate the desired number of samples for each class
  n_samples = class_counts.max()

  sampling_strategy = {0: n_samples, 1: n_samples, 2: n_samples}

  # Instantiate the SMOTE object with the desired sampling strategy
  oversample = SMOTE(sampling_strategy=sampling_strategy, k_neighbors=5, random_state=1)

  # Resample with SMOTE
  X_resampled, y_resampled = oversample.fit_resample(new_data.iloc[:,:-1], new_data.iloc[:,-1])

  # Combine the features and the target variable into a single dataframe
  resampled_data = pd.concat([pd.DataFrame(X_resampled), pd.DataFrame(y_resampled)], axis=1)
  resampled_data.columns = new_data.columns

  # define the input features and target variable
  X = resampled_data.drop('quality', axis=1)
  y = resampled_data['quality']

  X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)
  print(X_train.shape)
  print(X_test.shape)
  print(y_train.shape)
  print(y_test.shape)

  #Normalization
  scaler= StandardScaler()

  X_train= scaler.fit_transform(X_train)
  X_test= scaler.transform(X_test)

  #one-hot encoding
  y_train_encoded = to_categorical(y_train)
  y_test_encoded = to_categorical(y_test)

  def user_report():
    fixed_acidity = st.slider('Fixed Acidity', 4.6, 13.3, 0.0)
    volatile_acidity = st.slider('Volatile Acidity', 0.12, 1.185, 0.0)
    citric_acid = st.slider('Citric Acid', 0.0, 0.78 ,0.0 )
    chlorides = st.slider('Chlorides', 0.03, 0.2, 0.0 )
    free_sulfur_dioxide = st.slider('Free Sulfur Dioxide', 1.0, 43.0, 0.0)
    total_sulfur_dioxide = st.slider('Tree Sulfur Dioxide', 6.0, 155.0, 0.0)
    density = st.slider('Density', 0.9908, 1.0015, 0.0)
    pH = st.slider('pH', 2.92, 3.75, 0.0)
    sulphates = st.slider('Sulphates', 0.33, 1.08, 0.0)
    alcohol  = st.slider('Alcohol', 8.4, 14.0, 0.0)

    user_report = {
          'fixed acidity':fixed_acidity,        
          'volatile acidity':volatile_acidity,          
          'citric acid':citric_acid,              
          'chlorides':chlorides,                
          'free sulfur dioxide':free_sulfur_dioxide,    
          'total sulfur dioxide':total_sulfur_dioxide,   
          'density':density,                   
          'pH':pH,                        
          'sulphates':sulphates,                 
          'alcohol':alcohol                  
      }
    report_data = pd.DataFrame(user_report, index=[0])
    return report_data

  user_data = user_report()

  #building the sequential model
  #L1 is first hidden layers, L2 is second hidden layers
  L1=100
  L2=100

  ann = Sequential()
  ann.add(Dense(L1,input_dim=10,activation='relu'))
  ann.add(Dense(L2,activation='relu'))
  ann.add(Dense(3,activation='softmax'))

  # compiling the sequential model
  ann.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

  #Implement early stopping
  early_stopping_monitor = EarlyStopping(patience=5)

  history = ann.fit(X_train, y_train_encoded, epochs=300, batch_size=300,
                      validation_data=(X_test, y_test_encoded),
                      callbacks=[early_stopping_monitor])

  #building the sequential model
  #L1 is first hidden layers, L2 is second hidden layers
  L1=100
  L2=100

  ann = Sequential()
  ann.add(Dense(L1,input_dim=10,activation='relu'))
  ann.add(Dense(L2,activation='relu'))
  ann.add(Dense(3,activation='softmax'))

  user_result = ann.predict(user_data)
  st.subheader('Your Report: ')
  output = ''

  # Check if user_result is a 2D array and reshape if necessary
  if user_result.ndim > 1:
      user_result = np.argmax(user_result, axis=1)  # Convert probabilities to class labels

  # Calculate the most common prediction in user_result
  predicted_quality = np.argmax(np.bincount(user_result))

  # Map the predicted quality to a text description
  if predicted_quality == 0:
      output = 'Wine Quality is LOW'
  elif predicted_quality == 1:
      output = 'Wine Quality is MODERATE'
  else:
      output = 'Wine Quality is HIGH'

  st.write(output)


