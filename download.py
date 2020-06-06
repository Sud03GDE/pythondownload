import urllib.request

print ("For downloading files from the internet.") 
file=input ("website download link: ")
name=input ("Name of file with entension: ")
urllib.request.urlretrieve (file, name)
