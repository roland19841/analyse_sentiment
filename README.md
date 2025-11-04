# Projet : Analyse de Sentiment avec FastAPI et Streamlit

Ce projet fait partie du module 0 de la formation OPCO Atlas – Intelligence Artificielle.

## 🎯 Objectif
Créer une application web complète :
- Une API FastAPI pour analyser le sentiment d’un texte via le modèle VADER (NLTK)
- Une interface Streamlit pour interagir facilement avec cette API

## ⚙️ Technologies
- Python
- FastAPI / Uvicorn
- NLTK (VADER)
- Pydantic
- Loguru
- Streamlit

## 🚀 Lancement
### API
```bash
uvicorn sentiment_api:app --host 127.0.0.1 --port 9000 --reload