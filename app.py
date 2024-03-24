# Import the packages
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import sklearn as sk
import joblib

# Titre de l'application
st.title('Dashboard interactif avec Streamlit')

# Charger les données
@st.cache_data
def load_data():
    # Chargement de données)
    data = pd.read_csv("data/exercice_data.csv",index_col = 'StudentID', sep=',',encoding='latin1')
    # liste de colonnes numeriques
    colNumToConvert = [x for x in data.columns if x not in ["age","absences","FinalGrade"]]
    # Appliquer astype('object') sur les colonnes spécifiées
    data[colNumToConvert] = data[colNumToConvert].astype('object')
    return data

# Appeler la fonction pour charger les données
data = load_data()

model = joblib.load("data/LinearRegression_model.sav")
data["score"] = model.predict(data[["paid","studytime","goout","Dalc","Walc","schoolsup","internet","absences"]])

# Afficher un echantillon de 5 lignes du dataframe
st.write("Voici les premières lignes du dataframe :")
st.write(data.sample(5))

# Créer un graphique interactif avec Altair
st.write("Graphique interactif avec Altair :")
# Sélectionner les colonnes à inclure dans le graphique
columns = st.multiselect("Sélectionnez les colonnes à inclure :", data.columns.tolist())
# Créer le graphique interactif
if columns:
    chart = alt.Chart(data).mark_point().encode(
        x=columns[0],
        y=alt.Y(columns[1], scale=alt.Scale(zero=False)),
        tooltip=columns
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

# Créer un graphique boxplot interactif avec Altair
st.write("Graphique Boxplot interactif avec Altair :")

# Sélection de la variable catégorielle
cat_variable = st.selectbox("Sélectionnez la variable catégorielle :", data.select_dtypes(include='O').columns.tolist())

if cat_variable:
    # Création du graphique boxplot interactif
    boxplot_chart = alt.Chart(data).mark_boxplot().encode(
        x=cat_variable,
        y='FinalGrade:Q',  # Variable cible
        tooltip=[cat_variable, 'FinalGrade']  
    ).properties(
        width=600,
        height=400
    ).interactive()

    st.altair_chart(boxplot_chart, use_container_width=True)


#creer un bouton activable permettant de garder seulement les variables ci dessous
#[["studytime","goout","Dalc","Walc","schoolsup","internet","absences"]]