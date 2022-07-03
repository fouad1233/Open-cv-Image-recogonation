"""The updated repo can be installed using the following command. 
pip install git+https://github.com/Joeclinton1/google-images-download.git"""
from google_images_download import google_images_download

#instantiate the class
response = google_images_download.googleimagesdownload()
arguments = {"keywords":" Rachel Green ",
             "limit":100,"print_urls":False}
paths = response.download(arguments)

#print complete paths to the downloaded images
print(paths)
