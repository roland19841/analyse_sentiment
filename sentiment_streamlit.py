import streamlit as st
import requests
from loguru import logger

# --- Config logs ---
logger.add("logs/streamlit_app.log",
           rotation="10 MB",
           retention="7 days",
           compression="zip",
           level="INFO",
           enqueue=True,
           format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")

# --- Configuration de la page ---
st.set_page_config(page_title="Analyse de Sentiment", page_icon="💬")
st.title("💬 Application d’analyse de sentiment")
st.markdown("Cette interface envoie votre texte à l’API FastAPI et affiche les résultats de l’analyse de sentiment via le modèle **VADER**.")

# --- Entrée utilisateur ---
texte = st.text_area("Saisissez un texte en anglais :", height=150)

# --- URL de ton API (à adapter si besoin) ---
API_URL = "http://127.0.0.1:9000/analyse_sentiment/"

# --- Quand l’utilisateur clique sur le bouton ---
if st.button("Analyser le sentiment"):
    if not texte.strip():
        st.warning("⚠️ Merci de saisir un texte avant d’analyser.")
    else:
        try:
            logger.info(f"Envoi du texte à l’API: {texte}")
            response = requests.post(API_URL, json={"texte": texte})
            
            if response.status_code == 200:
                data = response.json()
                st.success("✅ Analyse réussie !")
                
                st.write("### Résultats :")
                st.write(data)

                compound = data.get("compound", 0)
                if compound >= 0.05:
                    st.markdown("**🟢 Sentiment positif**")
                elif compound <= -0.05:
                    st.markdown("**🔴 Sentiment négatif**")
                else:
                    st.markdown("**⚪ Sentiment neutre**")

            else:
                st.error(f"Erreur API ({response.status_code}) : {response.text}")
        except Exception as e:
            logger.exception(f"Erreur pendant la requête API: {e}")
            st.error("🚨 Impossible de contacter l’API. Vérifie qu’elle est bien en cours d’exécution.")