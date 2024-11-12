# Emirates-Airlines-Sentiment-Analysis ✈️

## Project Overview 
This project aims to analyze customer sentiments about Emirates Airlines by collecting and processing data from online reviews. The insights gathered can help understand customer satisfaction levels, recurring topics, and key areas of improvement.

## Installation: ⚙️
### 1. Clone this repository
```
git clone https://github.com/abhinavsaxena123/Emirates-Airlines-Sentiment-Analysis
cd Emirates-Airlines-Sentiment-Analysis
```

### 2. Set Up a Virtual Environment
* Using venv (for Python):
```
python3 -m venv env                        # Use `python` on Windows instead of `python3`
source env/bin/activate                    # On Windows, use source env/Scripts/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run the Flask app ✈️
```
python app.py
```



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
<img width="862" alt="image" src="https://github.com/user-attachments/assets/f573cbd3-7e61-4bf1-85c0-e7a05645e3db">

* Country-Based Analysis
* Visualizations of sentiment distribution by word cloud and bar charts


## Sentiment Analysis
Sentiment classification was applied to categorize reviews as positive, neutral, or negative using libraries such as VADER or a machine learning model like Naive Bayes. The labeled data was used to train, validate, and test the sentiment classifier.

<img width="744" alt="image" src="https://github.com/user-attachments/assets/d661f4d6-3a31-4e87-9fb6-17417ecc6cab">

<img width="554" alt="image" src="https://github.com/user-attachments/assets/1602a4ce-0f1d-4a32-8c13-0dda984b1b55">

<img width="563" alt="image" src="https://github.com/user-attachments/assets/afe86b4f-b9f4-40db-ace5-989fae9275a7">



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
### Model Performance Summary
<img width="833" alt="image" src="https://github.com/user-attachments/assets/3ffd894f-3723-45f3-be65-ce38cf7c9f18">

### Analysis
### 1. Top Performers:
* SVM achieved the highest scores across all metrics except precision, indicating strong overall performance in detecting sentiments effectively.
* XGBoost also performed well, with slightly lower F1 and recall scores compared to SVM but close precision.

### 2. Boosting Methods:
* Gradient Boost and AdaBoost scored relatively well, especially in terms of precision, but were slightly outperformed by XGBoost and SVM.

### 3. Decision Tree Variants:
* Both decision tree classifiers had moderate performance, with GridSearch tuning slightly improving recall but marginally lowering precision.

### 4. Random Forest:
Precision for the Random Forest classifier was high, but recall and F1 were lower, suggesting it struggled with correctly identifying some sentiment classes.

### 5. Multinomial Naive Bayes (MNB):
MNB showed the highest precision but a very low F1 score, indicating that while it made fewer false positives, it missed many actual cases due to low recall. This trade-off can be useful if precision is prioritized over recall.

Our sentiment analysis revealed that X% of reviews are positive, Y% are neutral, and Z% are negative. The top themes identified in the topic modeling were related to customer service, in-flight entertainment, and amenities.

## Future Improvements
* Implement additional deep learning models for more accurate sentiment classification.
* Adding a feedback loop to improve sentiment model accuracy with new data.
* More Meta Data about the reviews.
* Use of Pre-Trained Models like BERT.





