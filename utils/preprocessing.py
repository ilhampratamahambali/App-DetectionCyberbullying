import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Inisialisasi NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Fungsi pembersihan teks
def clean_text(text):
    if not isinstance(text, str):
        return ""

    # Lowercase
    text = text.lower()

    # Hapus URL, username, hashtag
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"@\w+|#\w+", "", text)

    # Hapus emoji & non-ascii
    text = text.encode("ascii", "ignore").decode()

    # Hapus tanda baca & angka
    text = re.sub(r"[^a-z\s]", " ", text)

    # Tokenisasi
    words = nltk.word_tokenize(text)

    # Stopwords
    words = [w for w in words if w not in stop_words and len(w) > 2]

    # Stemming
    words = [stemmer.stem(w) for w in words]

    return " ".join(words)
