import		json
import urllib.request
class AstroPhoto:
	def __init__(self, data):
		self.title = data["title"]
		self.date = data["date"]
		self.description = data["explanation"]
		self.url = data.get("hdurl", data.get("url", None))

		def get_short_description(self):
			if len(self.description) <= 200:
				return self.description
			else:
				return self.description[:197] + "..."

def get_apods_between(api_key, start_date, end_date):
	url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={start_date}&end_date={end_date}"
	with urllib.request.urlopen(url) as request:
		response = request.read().decode()

	photos =[AstroPhoto(item) for item in json.loads(response)]
	return photos


# test code
apods = get_apods_between("DEMO_KEY", "2023-01-01", "2023-01-07")
for photo in apods:
	print(f"Date: {photo.date}, Title: {photo.title}")