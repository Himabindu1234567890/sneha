from flask import Flask, render_template, request
import pickle
import pandas as pd

model = pickle.load(open("sentiment_model.pkl","rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl","rb"))

app = Flask(__name__)


# Home page with two cards
@app.route("/")
def home():
    return render_template("home.html")


# Customer page
@app.route("/customer")
def customer():
    return render_template("customer.html")


# Company page
@app.route("/company")
def company():
    return render_template("company.html")


# Single review prediction
@app.route("/predict", methods=["POST"])
def predict():

    review = request.form["review"]

    review_vec = vectorizer.transform([review])

    prediction = model.predict(review_vec)[0]

    probs = model.predict_proba(review_vec)[0]

    confidence = round(max(probs)*100,2)

    if prediction == "Positive":
        rating = "⭐⭐⭐⭐⭐"
    elif prediction == "Neutral":
        rating = "⭐⭐⭐"
    else:
        rating = "⭐"

    return render_template(
        "customer.html",
        review=review,
        sentiment=prediction,
        confidence=confidence,
        rating=rating
    )


# Batch prediction
@app.route("/batch_predict", methods=["POST"])
def batch_predict():

    file = request.files["file"]

    df = pd.read_csv(file)

    vec = vectorizer.transform(df["review_text"])

    df["Sentiment"] = model.predict(vec)

    results = df[["review_text","Sentiment"]].values.tolist()

    return render_template(
        "company.html",
        results=results
    )
@app.route("/skin")
def skin():
    return render_template("skin.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    skin_type = request.form["skin"]

    if skin_type == "Oily":
        products = [
        "Oil-free moisturizer",
        "Salicylic acid face wash",
        "Gel-based sunscreen",
        "Niacinamide serum"
        ]

    elif skin_type == "Dry":
        products = [
        "Hydrating moisturizer",
        "Hyaluronic acid serum",
        "Cream-based cleanser",
        "Nourishing sunscreen"
        ]

    elif skin_type == "Sensitive":
        products = [
        "Aloe vera moisturizer",
        "Gentle cleanser",
        "Fragrance-free sunscreen",
        "Chamomile toner"
        ]

    else:
        products = [
        "Light moisturizer",
        "Vitamin C serum",
        "Balancing face wash",
        "SPF sunscreen"
        ]

    return render_template(
        "skin.html",
        skin_type=skin_type,
        products=products
    )

if __name__ == "__main__":
    app.run(debug=True)