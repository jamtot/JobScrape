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

    # finds a post on the job listing page
    listings = soup.findAll('div',attrs={'class':['jobsearch-SerpJobCard', 'unifiedRow', 'row', 'result', 'clickcard']})

    
    for post in listings:
        # takes the link to the single page post
        link = post.findAll('a', attrs={'class':'jobtitle turnstileLink'})
        nextPage = "https://www.indeed.com.au"+str(link[0]['href'])
        # opens the single page post
        newPage = requests.get(nextPage)
        newSoup = BeautifulSoup(newPage.text, 'html.parser')

        # takes the title, the poster, and any meta details included such as location, contract, pay
        title = newSoup.find(True, {'class':['icl-u-xs-mb--xs', 'icl-u-xs-mt--none', 'jobsearch-JobInfoHeader-title']})
        print(title.text)
        lister = newSoup.find(True, {'class':['icl-u-lg-mr--sm', 'icl-u-xs-mr--xs']})
        print(lister.text)
        meta = newSoup.findAll(True, {'class':['jobsearch-JobMetadataHeader-iconLabel']})
        for m in meta:
            print(m.text)
        # prints the link too
        print(nextPage+'\n')


    """ # test area (for using a single page to find details)
    page = requests.get("https://www.indeed.com.au/company/AiGroup/jobs/Graduate-Developer-3d4831a1a59ea3e0?fccid=db48a678d96be103&vjs=3")
    soup = BeautifulSoup(page.text, 'html.parser')
    #print(soup.prettify())

    title = soup.find(True, {'class':['icl-u-xs-mb--xs', 'icl-u-xs-mt--none', 'jobsearch-JobInfoHeader-title']})
    print(title.text)
    lister = soup.find(True, {'class':['icl-u-lg-mr--sm', 'icl-u-xs-mr--xs']})
    print(lister.text)
    meta = soup.findAll(True, {'class':['jobsearch-JobMetadataHeader-iconLabel']})
    for m in meta:
        print(m.text)
    """

    # TODO 
    # figure out issue with company name not working if it's a link
    # write into CSV file
    # take more information
    # split out skills sought      

if __name__=="__main__":
    scrapeIndeed()
