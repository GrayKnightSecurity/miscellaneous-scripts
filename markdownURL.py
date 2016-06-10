""" 
Returns webpage title and URL formatted for Markdown. Can be used with a file or single URL
Usage:
 python markdownURL.py -u url
 python markdownURL.py -f filename
File must be one URL per line
"""

import requests
import sys

def markdown(your_url):
    r = requests.get(your_url)
    title = str(r.text.split("title")[1].strip(">").strip("</"))
    print "[" + title + "](" + your_url + ")"

def bulk_smash(url_file):
    with open(url_file) as file_n:
        for url_line in file_n:
            your_url = url_line.strip("\n")
            markdown(your_url)

if __name__ == "__main__":
    option = sys.argv[1]
    if option == "-u":
        markdown(sys.argv[2])
    elif option == "-f":
        bulk_smash(sys.argv[2])
    else:
        print "Whoopsy daisy! Try again."
