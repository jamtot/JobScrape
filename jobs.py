import requests
from bs4 import BeautifulSoup

def scrapeIndeed():
    #collect what jobs the user is looking for and where

    #what = input("What job are you looking for? ")
    what = "software developer" # default for developing
    #where = input("Where are you looking for the job? ")
    where = "brisbane" # default for developing

    perpage=100

    page = requests.get("https://au.indeed.com/jobs?q="+what+"&l="+where+"&limit="+str(perpage))
    soup = BeautifulSoup(page.text, 'html.parser')

    #finds the job listings on the page
    listings = soup.findAll(True, {'class':['jobsearch-SerpJobCard', 'unifiedRow', 'row', 'result', 'clickcard']})

    #places jobs are listed as
    places = soup.findAll(True, {'class':['location', 'accessible-contrast-color-location']})

    #companies posts are listed under
    companys = soup.findAll(True, {'class':['company']})

    comp=""
    for i in range(len(listings)):
        lblock = listings[i].find_all("div", {"class": "title"})
        title=(lblock[0].find('a').text).strip()
        place=(places[i].text).strip()
        try:
            comp=(companys[i].text).strip()
        except:
            comp = soup.findAll('class')['company']
        print(str(i+1)+": "+title+"\n"+place+"\n"+comp+"\n")


    # TODO 
    # figure out issue with company name not working if it's a link
    # write into CSV file
    # take more information
    # split out skills sought      

if __name__=="__main__":
    scrapeIndeed()
