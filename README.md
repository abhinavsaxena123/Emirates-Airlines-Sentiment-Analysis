# Emirates-Airlines-Sentiment-Analysis

## Project Overview
This project aims to analyze customer sentiments about Emirates Airlines by collecting and processing data from online reviews. The insights gathered can help understand customer satisfaction levels, recurring topics, and key areas of improvement.

## Introduction
The goal is to capture and analyze customer sentiment regarding Emirates Airlines using machine learning and natural language processing. The project processes raw textual data and applies sentiment classification and topic modeling to uncover valuable insights.

## Data Collection
Data was gathered through web scraping using Beautiful Soup to collect reviews from [website - Skytrax]. The scraping script, located in Data_Collection/Web_Scraping.ipynb, extracts text reviews, ratings, and any relevant metadata.

## Data Cleaning
The raw data was cleaned to remove duplicates, null values, and irrelevant content. Text preprocessing steps included:
* Lowercasing
* Removing stop words
* Lemmatization
* Removing special characters

## Exploratory Data Analysis (EDA)
We performed an EDA to understand general trends, including:
* Rating distributions
* Country-Based Analysis
* Visualizations of sentiment distribution by word cloud and bar charts

## Sentiment Analysis
Sentiment classification was applied to categorize reviews as positive, neutral, or negative using libraries such as VADER or a machine learning model like Naive Bayes. The labeled data was used to train, validate, and test the sentiment classifier.

## Topic Modeling
Topic modeling was performed using Latent Dirichlet Allocation (LDA) to identify recurring themes in the reviews, such as 'service quality,' 'comfort,' and 'food and beverage.'

## Modeling and Evaluation
Various models were experimented with for sentiment analysis, including:
* Naive Bayes
* SVM
* Decision Tree
* Random Forest
* Ada Boost
* Gradient Boosting
* XG Boost
Each model was evaluated using metrics like accuracy, F1-score, and confusion matrix.

## Web Application
A Flask web app was created to allow users to input new reviews and predict sentiment in real-time.


## Results
Our sentiment analysis revealed that X% of reviews are positive, Y% are neutral, and Z% are negative. The top themes identified in the topic modeling were related to customer service, in-flight entertainment, and amenities.

## Future Improvements
* Implement additional deep learning models for more accurate sentiment classification.
* Adding a feedback loop to improve sentiment model accuracy with new data.
* More Meta Data about the reviews.
* Use of Pre-Trained Models like BERT.





