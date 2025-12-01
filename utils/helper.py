import joblib
from utils.preprocessing import clean_text

def load_models(
    model_path='model/model.pkl',
    tfidf_path='model/tfidf.pkl',
    encoder_path='model/encoder.pkl'
):
    model = joblib.load(model_path)
    tfidf = joblib.load(tfidf_path)
    encoder = joblib.load(encoder_path)
    return model, tfidf, encoder

def predict_text(text, model, tfidf, encoder):
    cleaned = clean_text(text)
    vectorized = tfidf.transform([cleaned])
    pred = model.predict(vectorized)
    label = encoder.inverse_transform(pred)
    return label[0]
