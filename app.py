import streamlit as st
import requests
from streamlit_hls_player import hls_player  # importer le lecteur

st.title("📺 IPTV Live Player")

url = 'https://all-sport-live-stream.p.rapidapi.com/api/v2/all-live-stream'
headers = {
    'x-rapidapi-key': '54174e58demshb68c0b5e1e36baep12dcecjsn985c9fffadcc',
    'x-rapidapi-host': 'all-sport-live-stream.p.rapidapi.com'
}

r = requests.get(url, headers=headers)

if r.status_code == 200:
    data = r.json()
    for sport in data:
        sport_name = sport.get("sport_name", "Inconnu")
        matches = sport.get("data")

        if not isinstance(matches, list):
            continue

        for match in matches:
            m3u8 = match.get("m3u8_source")
            if m3u8:
                st.markdown(f"### ⚽ {sport_name} : {match['team_one_name']} vs {match['team_two_name']}")
                st.markdown(f"⏱ {match.get('start_time', 'N/A')} | 📊 {match.get('score', 'N/A')}")
                if st.button(f"▶️ Lire ce match", key=m3u8):
                    hls_player(m3u8)
                st.markdown("---")
else:
    st.error(f"Erreur API : {r.status_code}")
