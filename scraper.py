import requests
import lxml.html
from bs4 import BeautifulSoup
import mechanize
import regex as re
import google.generativeai as genai
import config

def from_zip(zip):
    if (len(zip) == 5):
    
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
        return URL
    else:
        return "invalid"

# Takes in zip as a string and returns the name of the representative
def rep_from_zip(zip):

    URL = from_zip(zip)
    if URL == "invalid":
        return URL 
    else:
        page = requests.get(URL, headers={
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
        # Scrape HTML
        html = lxml.html.fromstring(page.content)
        name = html.xpath("/html/body/div[2]/div/div[2]/section/div/div[2]/div[2]/div/div/p/a[1]")
        return(name[0].text)
    
def dist_party_from_zip(zip):
    
    # Insantiate browser
    URL = from_zip(zip) 
    if URL == "invalid":
        return URL, URL, URL
    page = requests.get(URL, headers={
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})

    # Scrape HTML
    html = lxml.html.fromstring(page.content)
    name = html.xpath("/html/body/div[2]/div/div[2]/section/div/div[2]/div[2]/div/div/p/a[1]")
        
    soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")
    
    if (len(name) > 1): 
        table = soup.find('div', attrs = {'id':'PossibleReps'})
        info = table.findAll('div')[0].text.split() 
        
        district = ""
        for te in info[-3:]:
            district = district + te + " "
        district = district[:-1]
        party = info[-4]
        image = "https://ziplook.house.gov/" + table.find_all("img")[0]['src']
        return party, district, image
        
        
    else:
        table = soup.find('div', attrs = {'class':'col-xs-16 col-md-4 pull-md-12 repdistrict'}) 
        info = table.find('p')
        district = str.splitlines(info.text)[5]
        dist = re.match("([^0-9]*)([0-9].*)", district).group(2)
        party = party = str.splitlines(info.text)[12]
        party = re.sub(r'[\t ]', "", party)
        image = "https://ziplook.house.gov/" + table.find_all("img")[0]['src']
        return party, dist[:-1], image

def gen_rep_info(name):
    genai.configure(api_key=config.api_key)
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,    
    }

    model = genai.GenerativeModel(model_name="gemini-2.0-flash", generation_config=generation_config)
    convo = model.start_chat(history = [])
    convo.send_message(f"""Do not provide any text in the beginning of this response that does not address this prompt directly.
    Give me the following information about representative {name}. 
     \n Their three most recent key votes ordered by date (most recent to least recent) sourced from the representative's 
     Ballotopedia.org \"key votes\" section in a table format containing the vote name, whether the vote passed, whether 
     the representative voted yay or nay for it, and the date of the vote. \n If the representative serves on a house committee, 
     and if so which ones. List the house committees in a list and the relevant subcommittees under them. Do not use bullet points or numbers. If not, return that 
     the representative is not on any house committees. Source must be from Ballotopedia or the representative's house.gov
     website. \n One relevant fact about the representative  (one sentence). \n Make the answer very concise and readable for 
     a middle school level. Format everything as HTML. Do not include a title, such as the representative's name, in the 
     first line of your response. Directly provide the response. Please add a line citing sources at very the end. """)
    return convo.last.text[8:-9]