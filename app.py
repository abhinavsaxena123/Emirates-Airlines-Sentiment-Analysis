from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import pandas as pd
import os


app = Flask(__name__)

# Set a secret key (make sure this is random and secure)
app.secret_key = os.urandom(24)


# Loading the trained model and vectorizer(tfidf)
model = pickle.load(open('SavedModels/svm.pkl', 'rb'))
vectorizer = pickle.load(open('SavedModels/tfidf_vec.pkl', 'rb'))

# Preprocess text function
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Remove non-alphabetic characters
    text = re.sub('[^a-zA-Z]', ' ', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize and lemmatize
    text = text.split()
    text = [lemmatizer.lemmatize(word) for word in text if word not in stop_words]
    # Rejoin the text
    return " ".join(text)

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Handle CSV file upload
        if 'file' in request.files and request.files['file'].filename != '':
            file = request.files['file']

            # Check if it's a CSV file
            if file.filename.endswith('.csv'):
                try:
                    df = pd.read_csv(file)

                    # Check if 'reviews' column exists
                    if 'reviews' not in df.columns:
                        flash('CSV file must contain a "reviews" column.')
                        return redirect(url_for('home'))
                    
                    csv_result = "CSV file uploaded successfully!"
                    reviews = df['reviews']  

                    # Preprocess and predict
                    processed_reviews = [preprocess_text(review) for review in reviews]
                    vectorized_reviews = vectorizer.transform(processed_reviews).toarray()
                    predictions = model.predict(vectorized_reviews)

                    positive_count = sum(predictions == 1)
                    negative_count = sum(predictions == 0)

                     # Flash success message and render the template with results
                    flash(csv_result, 'success')
                    return render_template('index.html', positive_count=positive_count, negative_count=negative_count)
                
                except Exception as e:
                    # Handle errors (e.g., empty file, pandas reading issues)
                    flash(f'Error processing file: {str(e)}', 'danger')
                    return redirect(url_for('home'))
                
            else:
                flash('Please upload a valid CSV file.', 'danger')
                return redirect(url_for('home'))
        
        elif 'review' in request.form:
            review = request.form['review']
            # Preprocess and predict the single review
            processed_review = preprocess_text(review)
            vectorized_review = vectorizer.transform([processed_review]).toarray()
            prediction = model.predict(vectorized_review)[0]

            # Set positive and negative count based on single review
            positive_count = 1 if prediction == 1 else 0
            negative_count = 1 if prediction == 0 else 0

            sentiment = "Positive" if prediction == 1 else "Negative"

            # Return the result
            return render_template('index.html', prediction_text=f'The review is: {sentiment}')
    
    else:
        # Flash error if no valid input is provided
        flash('Please provide a review or upload a CSV file.', 'danger')
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
