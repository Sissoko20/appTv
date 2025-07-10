import streamlit as st
import requests

st.title("📊 Statistiques de l'équipe")

team_id = st.number_input("ID de l’équipe", min_value=1, value=2829)
tournament_id = st.number_input("ID du tournoi", min_value=1, value=8)
season_id = st.number_input("ID de la saison", min_value=1, value=61643)

if st.button("📈 Charger les stats"):
    url = f'https://allsportsapi2.p.rapidapi.com/api/team/{team_id}/tournament/{tournament_id}/season/{season_id}/goal-distributions'

    headers = {
        'x-rapidapi-key': '21b9ddbae5msh4a3c8b7c59c9c72p16414cjsn1a40e59b9ac8',
        'x-rapidapi-host': 'allsportsapi2.p.rapidapi.com'
    }

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        stats = r.json()
        st.json(stats)
    else:
        st.error(f"Erreur {r.status_code}")
