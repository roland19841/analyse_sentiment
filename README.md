# 💬 Analyse de Sentiment — Module 0 (Formation IA - OPCO Atlas / Simplon)

## 🧠 Description du projet
Ce projet constitue le **Module 0** de la formation en Intelligence Artificielle (OPCO Atlas x Simplon).  
L’objectif est de mettre en place un environnement Python complet et de créer une **application d’analyse de sentiment** simple basée sur :

- **FastAPI** → pour le backend (API REST d’analyse)
- **Streamlit** → pour le frontend (interface utilisateur)
- **NLTK (VADER)** → pour l’analyse du sentiment du texte
- **Loguru** → pour la gestion centralisée des logs

---

## 🧩 Architecture générale
- **Streamlit** (port `8501`) : interface graphique pour saisir du texte et afficher les résultats.  
- **FastAPI** (port `9000`) : reçoit les requêtes HTTP, analyse le texte et renvoie les scores d’émotion.  
- Les deux applications communiquent en local via des appels HTTP (`requests.post()`).

---

## ⚙️ Installation et configuration

### 1️ - Cloner le dépôt

-> git clone https://github.com/<ton-nom-utilisateur>/analyse_sentiment.git
-> cd analyse_sentiment

### 2 - Créer un environnement virtuel
-> python -m venv .venv311
-> .\.venv311\Scripts\activate

### 3 - Installer les dépendances
-> pip install -r requirements.txt



## Lancer l'application

### 1 - démarrer le serveur Fast API
 -> uvicorn sentiment_api:app --host 127.0.0.1 --port 9000 --reload

Ouvre http://127.0.0.1:9000/docs pour tester les routes API.

### 2 - Démarrer l'interface Streamlit**
Dans un deuxième terminal avec "venv" activé : 

 -> streamlit run sentiment_streamlit.py
 
Ouvre http://localhost:8501 pour accéder à l’interface web.

💡 Exemple d’utilisation

Saisir un texte en anglais (ex. "I really love this project!")
Cliquer sur Analyser le sentiment
Visualiser les scores et la tonalité détectée :
{
  "neg": 0.0,
  "neu": 0.3,
  "pos": 0.7,
  "compound": 0.8
}
🟢 Sentiment positif

🧰 Technologies utilisées
Technologie	--- Rôle
Python 3.11	--- Langage principal
FastAPI	    --- API REST pour l’analyse
Streamlit	--- Interface web utilisateur
NLTK (VADER)---	Analyseur de sentiment
Pydantic    ---	Validation des données JSON
Uvicorn	    --- Serveur ASGI pour FastAPI
Loguru	    --- Gestion des logs

## Structure du projet 
analyse_sentiment/
│
├── sentiment_api.py            # Backend FastAPI
├── sentiment_streamlit.py      # Interface Streamlit
├── requirements.txt            # Dépendances
├── README.md                   # Documentation
├── logs/                       # Dossier des fichiers de logs
│   ├── sentiment_api.log
│   └── streamlit_app.log
└── tests/                      # (optionnel) Tests Pytest

---

> Auteur : Roland RENIER - Dans le cadre de la formation IA - OPCO Atlas X simplon (Module 0)
