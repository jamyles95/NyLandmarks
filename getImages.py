import os
from google_images_download import google_images_download

cwd = os.getcwd()
response = google_images_download.googleimagesdownload()


search_queries = [
    'Empire State Building',
    'The Chrysler Building',
    'The Flatiron Building',
    'One World Trade Center',
    'Rockefeller Plaza',#30 Rock
    'Met Life Tower',
    'Manhattan Municipal Building',
    'New York Life Insurance Building',
    'The E.V. Haughwout Building',
]

def downloadimages(query):

	arguments = {"keywords": query,
				"format": "jpg",
				"limit":100,
				"print_urls":True,
				"size": "medium",
                "output_directory": cwd + "/images",
				"aspect_ratio": "panoramic"}
	try:
		response.download(arguments)

	# Handling File NotFound Error
	except FileNotFoundError:
		arguments = {"keywords": query,
					"format": "jpg",
					"limit":4,
					"print_urls":False,
					"size": "medium"}

		# Providing arguments for the searched query
		try:
			# Downloading the photos based
			# on the given arguments
			response.download(arguments)
		except:
			pass

if __name__ == "__main__":
    for query in serach_queries:
        downloadimages(query)
