# sentiment_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from loguru import logger
from nltk.sentiment import SentimentIntensityAnalyzer

# --- Configuration du logger ---
logger.add("logs/sentiment_api.log",
           rotation="10 MB",
           retention="7 days",
           compression="zip",
           level="INFO",
           enqueue=True,
           format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")

# --- Modèle d'entrée ---
class Texte(BaseModel):
    texte: str = Field(..., min_length=1, description="Texte à analyser")

# --- Création de l'application FastAPI ---
app = FastAPI(title="API Analyse de Sentiment", version="0.1.0")

# --- Initialisation du modèle VADER ---
sia = SentimentIntensityAnalyzer()

@app.get("/")
def root():
    """Vérifie que l'API fonctionne."""
    logger.info("Route '/' appelée.")
    return {"message": "API OK", "docs": "/docs"}

@app.post("/analyse_sentiment/")
def analyse_sentiment(texte_object: Texte):
    """Analyse le sentiment d'un texte avec VADER."""
    try:
        texte = texte_object.texte
        logger.info(f"Texte reçu: {texte}")
        sentiment = sia.polarity_scores(texte)
        logger.info(f"Résultat: {sentiment}")
        return sentiment
    except Exception as e:
        logger.exception(f"Erreur d'analyse: {e}")
        raise HTTPException(status_code=500, detail="Erreur serveur")