from website_rank import *
from imports import *
from countryinfo import*
from datetime import date
import datetime

def get_African_Countries():
    african_countries=[] 
    for i in countries:
        if i['continent']== 'Africa': 
            african_countries.append(i['name'])
    african_countries.append('Africa')## Appended Africa here
    return african_countries
        
def get_date_scrapped():
    date_scrapped = []
    for i in range(0,4):
      previous_Date = datetime.datetime.today() - datetime.timedelta(days=i)
      date_scrapped.append(previous_Date.date())
    return date_scrapped

def get_items(soup):
  #print(len(soup.findAll("item")))
  counter=0
  for news in soup.findAll("item"):
    try:
      counter = counter +1
      stringDate = news.pubDate.text
      stringDate = stringDate.replace(",","")
      date = datetime.datetime.strptime(stringDate,'%a %d %b %Y %H:%M:%S %Z')
      if date.date() in get_date_scrapped():
        datepublished = date
        html = requests.get(news.link.text,timeout = 3)
        yield html.url,datepublished
    except:
      pass

def getSearch1(news_url):
    news_Africa = pd.DataFrame(columns = ['url','dates'])
    url_list =[]
    dates =[]
    width = 80
    counter = 0
    
    rss_text = requests.get(news_url).text
    soup_page = BeautifulSoup(rss_text, "xml")
    for (url,date) in get_items(soup_page):
        url = '\n'.join(textwrap.wrap(url, width))
        url_list.append(url)
        dates.append(date)
    news_Africa['url'] = url_list
    news_Africa['dates'] = dates
    return news_Africa


def getSearch2(term):
    search_terms =[]
    african_countries = get_African_Countries()
    for index,country in enumerate (african_countries):
      if (index + 1) % 4 == 0 or index + 1 == len(african_countries) :
        search_term = search_term.replace(" ","%20")
        search_terms.append(search_term)
      else:
        if index % 4 == 0:
           search_term = country
        else :
          search_term +=' OR '+ country
          
    news_country= pd.DataFrame(columns = ['url','dates'])
    url_list =[]
    dates =[]
    width = 80
    counter = 0
    for search_term in search_terms:
      news_url1="https://news.google.com/news?q="+search_term+"%20"+term+"&hl=en-US&gl=US&sort=date&ceid=US%3Aen&output=rss"
      rss_text1 = requests.get(news_url1).text
      soup_page1 = BeautifulSoup(rss_text1, "xml")
      for (url,date) in get_items(soup_page1):
        if url not in url_list:
          url = '\n'.join(textwrap.wrap(url, width))
          url_list.append(url)
          dates.append(date)
    news_country['url'] = url_list
    news_country['dates'] = dates
    return news_country
    
## combining results from both search terms 
def combine_news(news_url, term):
    news_Africa = getSearch1(news_url)
    news_country = getSearch2(term)
    news = news_Africa.append(news_country)
    news.reset_index(inplace=True)
    return news

def generate_news_dataframe(news_url,term):
    list_article=[]
    news = combine_news(news_url, term)
    print("News: ", news)
    for ind in news.index:
        try:
            dict={}
            #print(df['link'][ind])
            article = Article(news['url'][ind])
            article.download()
            article.parse()
            article.nlp()
            date = article.publish_date
            #print(article.title)
            #dict['Date']=df['date'][ind]
            dict['Link'] = news['url'][ind]
            #dict['Media']=df['media'][ind]
            dict['Global_Rank'] = getPageRank(news['url'][ind])
            dict['Title']=article.title
            #print(article.title)
            dict['Article']=article.text
            dict['keywords'] = article.keywords
            # dict['Summary']=article.summary
            list_article.append(dict)
        except:
          pass
    news_df=pd.DataFrame(list_article)
    news_df = news_df.sort_values(by='Global_Rank', ascending=True)
    return news_df