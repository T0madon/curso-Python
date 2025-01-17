import http.client

conn = http.client.HTTPSConnection("instagram-scraper-api2.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "Sign Up for Key",
    'x-rapidapi-host': "instagram-scraper-api2.p.rapidapi.com"
}

conn.request("GET", "/v1/audio_info?audio_canonical_id=18404792044021762", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))