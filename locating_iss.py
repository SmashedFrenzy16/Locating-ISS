import urllib.request
import json
import webbrowser

response = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
print(response)
data = json.loads(response.read())
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

final_url = 'https://www.openstreetmap.org/?mlat=' + str(latitude) + '&mlon=' + str(longitude) + '#map=3/' + str(latitude) + '/' + str(longitude)

webbrowser.open_new_tab(final_url)
