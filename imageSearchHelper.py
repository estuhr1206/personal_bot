import string
from google_images_download import google_images_download

def findImage(inputKeywords, num: int):
    #inputKeywords can possibly come in as a list of words
    response = google_images_download.googleimagesdownload()   #class instantiation
    #space in those quotes makes a space between words in joined string
    
    arguments = {"keywords":inputKeywords,"limit":num,"print_urls":True, "no_directory":True}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)

def findCountedImage(inputKeywords, num: int, randNum: int):
    #inputKeywords can possibly come in as a list of words
    response = google_images_download.googleimagesdownload()   #class instantiation
    #space in those quotes makes a space between words in joined string
    
    arguments = {"keywords":inputKeywords,"limit":num,"print_urls":True, "no_directory":True, "offset":randNum}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)
def testing():
    response = google_images_download.googleimagesdownload()   #class instantiation
    #space in those quotes makes a space between words in joined string
    
    arguments = {"keywords":'lawn chair',"limit":2,"print_urls":True, "no_directory":True, "offset":1}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)
#testing()
#asdf