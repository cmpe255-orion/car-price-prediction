# Car Price Prediction

## Presentation Video
https://drive.google.com/file/d/10VEOTdA9LbEyZOtinrI99-Efre40mXUJ/view?usp=sharing

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Platforms](#platforms)
* [Contributors](#contributors)
* [Status](#status)

## General info
Car purchases are a significant part of an individual’s life, and choosing the right car can have a significant impact on a person’s quality of life. Since a vehicle is a major ordeal, variables such as car price, mileage, brand, model, and year are all important factors for customers looking to choose a car. Since a vehicle’s value can depreciate over time and that different models have different rates of depreciation, customers must also have good knowledge of car prices in order to identify the cars which will be of most value to them. With the advancement of technology especially in the field of machine learning and data mining, humans can now be complemented with machine knowledge to make the best decisions. In this project, the team has used machine learning algorithms to identify and predict the car prices for used cars so that potential customers can get a better idea of which cars to purchase to guarantee their satisfaction.


## Technologies 

To best understand the variation of the data that is being worked with, it is imperative to use KMeans clustering to find the golden cluster, or the cluster of datapoints of cars that would give the best purchase value. By finding the SSE and the silhouette score, the number of clusters  K that determines the number of clusters can be derived, and that is used to run the KMeans algorithm. After running KMeans and getting the best cluster performance for the car value prediction column, the process is repeated two more times for a total of three KMeans iterations. 
  These are similar to the first KMeans process in that they use the SSE and silhouette score to determine the number of clusters that should be applied in the next iteration. Finally in the third KMeans, the best cluster is selected and the make and models for the best cars can be determined.
	The next step is to do the actual modeling on the training and testing set. Splitting the dataset into a training to testing set based on a 80: 20 ratio using the train_test_split() function allows X_train and y_train to be used as training to predict the X_test and y_test.  These will be used as the input for the multiple machine learning algorithms. The main classification models used are Nearest Neighbors, Decision Tree, Random Forest, Neural Net, and AdaBoost classifiers since these are the most prominent classification algorithms currently used.  These are run through a muller loop and the classification algorithm with the best results for car price prediction is identified. The main regression models used include Linear Regression, MLPRegressor, RandomForestRegressor, KNNRegressor, and XBoost Regressor, which are used to predict the prices of the cars. Similarly to classification algorithms, these algorithms are run through a muller loop and the regression algorithm with the best result is identified. 

## Platforms
* Python & Jupyter Notebook
* Flask API & Heroku

## Contributors

* Eric Cheng
* Archana Shokeen
* Babu Rajendran
* Hung Le
* Tingjia Zhang


## Status
Project is: _Completed_
