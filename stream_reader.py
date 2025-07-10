import requests

url = 'https://all-sport-live-stream.p.rapidapi.com/api/v2/all-live-stream'

headers = {
    'x-rapidapi-key': '54174e58demshb68c0b5e1e36baep12dcecjsn985c9fffadcc',
    'x-rapidapi-host': 'all-sport-live-stream.p.rapidapi.com'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    all_matches = []

    for sport in data:
        sport_name = sport.get('sport_name', 'Unknown')
        for match in sport.get('data', []):
            m3u8 = match.get('m3u8_source')
            if m3u8:
                team1 = match.get('team_one_name', 'Team 1')
                team2 = match.get('team_two_name', 'Team 2')
                score = match.get('score', 'N/A')
                print(f"🏆 {sport_name} | {team1} vs {team2} | Score: {score}")
                print(f"🎥 Lien M3U8: {m3u8}")
                print("-" * 80)
else:
    print(f"Erreur API: {response.status_code} - {response.text}")
