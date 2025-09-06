# 📩 SMS / Email Spam Classifier  

A **Machine Learning based Spam Classifier** that predicts whether a given SMS/Email is **Spam** or **Not Spam**.  
Built as a practice project while learning Machine Learning.

## 🚀 Live Demo  
👉 [Click Here to Try](https://sms-spam-classifier007.streamlit.app/)  

## 🌟 Features  
- 📝 **Custom Text Preprocessing**  
  - Lowercasing  
  - Tokenization (Regex Tokenizer)  
  - Stopword removal (NLTK)  
  - Stemming (PorterStemmer)  

- 📊 **Vectorization with TF-IDF**  
- 🤖 **Machine Learning Model (pickled)** for classification  
- 🖥️ **Streamlit-based Web UI** for easy interaction  
- ⚡ Instant prediction: Enter a message → Get result → "Spam" / "Not Spam"  

## 🛠️ Tech Stack  
- **Python 3**  
- **Streamlit** – Web Framework  
- **Scikit-learn** – Model Training & Prediction  
- **NLTK** – Natural Language Processing  
- **Pandas & NumPy** – Data handling  
- **Pickle** – Model & vectorizer serialization  

## 📂 Project Structure  

```
sms-spam-classifier/
├── app.py                # Streamlit app code
├── model3.pkl            # Trained ML model
├── vectorizer3.pkl       # TF-IDF Vectorizer
├── requirements.txt      # Dependencies
├── .gitignore
└── README.md
```

## 📷 Screenshots  

### 🔹 Home Page  
![Screenshot1](LINK_TO_IMAGE)  

### 🔹 Prediction Example  
![Screenshot2](LINK_TO_IMAGE)  


## 🏗️ How to Run Locally  

1. Clone the repository  
   ```bash
   git clone https://github.com/YOUR_USERNAME/sms-spam-classifier.git
   cd sms-spam-classifier
   ```

2. Create & activate a virtual environment (recommended)

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # For Linux/Mac
   .venv\Scripts\activate      # For Windows
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app

   ```bash
   streamlit run app.py
   ```

5. Open in browser → [http://localhost:8501](http://localhost:8501) 🎉

## 👩‍💻 Author

Made with ❤️ while learning ML from **CampusX** and improving it with my own ideas.
