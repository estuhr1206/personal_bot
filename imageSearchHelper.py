import string
from google_images_download import google_images_download

def findImage(inputKeywords, num: int):
    #inputKeywords can possibly come in as a list of words
    response = google_images_download.googleimagesdownload()   #class instantiation
    #space in those quotes makes a space between words in joined string
    
    arguments = {"keywords":inputKeywords,"limit":num,"print_urls":True, "no_directory":True}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)


#asdf