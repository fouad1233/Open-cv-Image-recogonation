"""The updated repo can be installed using the following command. 
pip install git+https://github.com/Joeclinton1/google-images-download.git"""
from google_images_download import google_images_download

#instantiate the class
missing_charackters = ["Monica Geller", "Phoebe Buffay", "Janice Hosenstein" , "Chandler Bing", "Ross Geller", "Joey Tribbiani"]
for i in range(len(missing_charackters)):
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":missing_charackters[i],
                "limit":100,"print_urls":False}
    paths = response.download(arguments)

    #print complete paths to the downloaded images
    print(paths)
