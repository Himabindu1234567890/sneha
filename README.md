# AI Skincare Review Sentiment Analysis & Recommendation System

## Overview

The **AI Skincare Review Sentiment Analysis & Recommendation System** is a web-based application that analyzes customer skincare product reviews using machine learning techniques.
The system classifies reviews into **Positive, Neutral, or Negative sentiments** and provides insights for both **customers and skincare companies**.

In addition to sentiment analysis, the system also provides **skin-type-based product recommendations**, helping users choose suitable skincare products.

---

## Key Features

### Customer Module

* Analyze individual skincare reviews
* Sentiment classification (Positive / Neutral / Negative)
* Confidence score display
* Automatic star rating generation
* Easy-to-use web interface

### Company Module

* Upload CSV files for **batch review analysis**
* Automatic sentiment classification for multiple reviews
* Table view of review results
* Helps companies analyze customer feedback

### Skin Type Recommendation Module

* Select skin type (Oily, Dry, Sensitive, Combination)
* Get recommended skincare products
* Helps users choose suitable products for their skin

---

## Technologies Used

* **Python**
* **Flask (Web Framework)**
* **Machine Learning (Scikit-learn)**
* **TF-IDF Vectorization**
* **HTML & CSS**
* **Pandas**

---

## Machine Learning Models

The system uses machine learning algorithms such as:

* Naive Bayes
* Logistic Regression
* Random Forest

These models classify skincare reviews based on sentiment.

---

## Project Structure

```
AI-Skincare-Sentiment-System
│
├── app.py
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
│
├── templates
│   ├── home.html
│   ├── customer.html
│   ├── company.html
│   └── skin.html
│
├── dataset
│   └── skincare_reviews.csv
│
└── README.md
```

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/Himabindu1234567890/sneha.git
```

### 2. Navigate to the Project Folder

```
cd sneha
```

### 3. Install Required Libraries

```
pip install flask pandas scikit-learn
```

### 4. Run the Application

```
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

## Example Use Cases

### Customer

A user enters a skincare review:

```
This moisturizer keeps my skin hydrated and smooth.
```

Output:

* Sentiment: Positive
* Confidence: 92%
* Rating: ⭐⭐⭐⭐⭐

---

### Company

Upload a CSV file containing multiple reviews:

```
review_text
This cream works well
This product caused irritation
The moisturizer is average
```

Output table:

| Review            | Sentiment |
| ----------------- | --------- |
| works well        | Positive  |
| caused irritation | Negative  |
| average           | Neutral   |

---

## Applications

* Skincare product review analysis
* Customer feedback monitoring
* Product quality improvement
* Personalized skincare recommendations

---

## Future Enhancements

* Deep learning based sentiment analysis
* Real-time review analytics dashboard
* Integration with e-commerce platforms
* Mobile application version

---

## Author


B.Tech Computer Science & Engineering (Data Science)

---
