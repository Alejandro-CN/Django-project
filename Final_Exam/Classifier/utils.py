import re
import spacy
import emoji
import pickle


def clean_tweet(text):
    text = re.sub('[^a-zA-Z]', ' ', str(text).lower().strip())
    text = re.sub('@[A-Za-z0-9_]+', '', text)
    text = re.sub('#', '', text)
    text = re.sub('RT[\s]+', '', text)
    text = re.sub('https?:\/\/\S+', '', text)
    text = re.sub('\n', ' ', text)
    text = emoji.replace_emoji(text, replace='')
    return text


def text_preprocessing(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)


# Load the saved model and vectorizer from the .pkl file
with open('model/model_and_vectorizer.pkl', 'rb+') as file:
    logreg_model, vectorizer = pickle.load(file)

def predict_result(text):
  text = clean_tweet(text)
  text = text_preprocessing(text)
  text = vectorizer.transform([text])
  predicted_numerical_label = logreg_model.predict(text.reshape(1, -1))
  predicted_textual_label = predicted_numerical_label[0]
  return(predicted_textual_label)
