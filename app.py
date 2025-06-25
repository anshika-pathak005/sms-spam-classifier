import streamlit as st
import pickle
import string
import nltk
# nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer

tfidf = pickle.load(open('vectorizer3.pkl','rb'))
model = pickle.load(open('model3.pkl','rb'))


ps = PorterStemmer()

# this is function for preprocessing the text
def text_transform(text):
    # lower-case
    text = text.lower()

    # tokenization
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)

    # text = nltk.word_tokenize(text)
    # # text = nltk.word_tokenize(text, language='english')
    # # from nltk.tokenize import PunktWordTokenizer
    # # tokenizer = PunktWordTokenizer()
    # # text = tokenizer.tokenize(text)
    # tokenizer = RegexpTokenizer(r'\w+')
    # text = tokenizer.tokenize(text)

    # Removing special characters (we will only keep alpabetical or alphanumerical)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)


    #- removing stopwords and punctuation
    text = y[:] #cloning the list
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)


    # stemming
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return  " ".join(y)



st.title("Email/SMS Spam Classifier")

input_sms = st.text_input("Enter the message...")

if st.button('Predict'):
    # now next we have to pereform 3 steps
    # 1, preprocess the text
    transformed_sms =  text_transform(input_sms)

    # 2, vectorization
    vector_input = tfidf.transform([transformed_sms])
    # 3, apply algo/ predict
    result = model.predict(vector_input)[0]

    # 4, display the output
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")


