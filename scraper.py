import requests
import lxml.html
import bs4 as BeautifulSoup
import mechanize

# Takes in zip as a string and returns the name of the representative
def rep_from_zip(zip):
    
    # Insantiate browser
    br = mechanize.Browser()
    br.set_handle_robots(False)

    # Open lookup link
    br.open("https://ziplook.house.gov/")

    # Find form and input zipcode
    br.select_form(nr=1)
    br.form["ZIP"] = zip
    br.submit()
    
    # Open URL
    URL = br.geturl()  
    page = requests.get(URL, headers={
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})

    # Scrape HTML
    html = lxml.html.fromstring(page.content)
    name = html.xpath("/html/body/div[2]/div/div[2]/section/div/div[2]/div[2]/div/div/p/a[1]")
    return(name[0].text)
