import http.client
import json

def fetch_live_matches():
    conn = http.client.HTTPSConnection("allsportsapi2.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "21b9ddbae5msh4a3c8b7c59c9c72p16414cjsn1a40e59b9ac8",
        'x-rapidapi-host': "allsportsapi2.p.rapidapi.com"
    }

    try:
        conn.request("GET", "/api/matches/live", headers=headers)
        res = conn.getresponse()
        data = res.read()
        response = json.loads(data.decode("utf-8"))
        return response.get("matches", [])
    except Exception as e:
        print("Erreur API:", e)
        return []
