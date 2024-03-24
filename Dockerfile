# Utilisez une image de base contenant Python
FROM python:3.9-slim

# Copiez les fichiers locaux dans le conteneur
COPY . /app

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Installez les dépendances du projet
RUN pip install -r requirements.txt

# Exposez le port sur lequel Streamlit fonctionne par défaut
EXPOSE 8501

# Commande pour exécuter l'application Streamlit lorsque le conteneur démarre
CMD ["streamlit", "run", "app.py"]
# docker run -p 8501:8501 mon_app_streamlit 
#http://localhost:8501