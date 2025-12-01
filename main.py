from utils.helper import load_models
from interface.ui_main import run_ui

# Load semua model
model, tfidf, encoder = load_models()

# Run UI
run_ui(model, tfidf, encoder)
