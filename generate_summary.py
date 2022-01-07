# from transformers import BartTokenizer, BartForConditionalGeneration
# import torch
# from transformers import PegasusTokenizer, PegasusForConditionalGeneration

from preprocessing import*
from models import*
from webscraping import*
from countryinfo import* 
from imports import*

news_url = "https://news.google.com/news?q=Africa%20Covid&hl=en-US&sort=date&gl=Africa&num=10&ceid=US%3Aen&output=rss"
term = "vaccinations"
## combining results from both search terms 

def get_summary(news_url, term):
    news_df = generate_news_dataframe(news_url,term)
    selected_news = get_selected_news(news_df)
    article = get_article(selected_news)
    
    clustered_text, clustered_link = check_similarities(article, selected_news)

    #print(clustered_link)
    
    # my_links = [link.replace("\n", "") for link in link_list]

    new_links = []
    
    for links in clustered_link:
      inner_links = []
      for link in links:
          inner_links.append(link.replace("\n", ""))
      new_links.append(inner_links)

    # print("the new link at position 0",new_links[0])
    # print("the new link at position 1",new_links[1])
    # print("the new link at position 2",new_links[2])
    # print("the length of clustered text",len(clustered_link))
    # print("the length of the new link",len(new_links))

    summaries = []
    #Loop thru a list of text:links pairs
    i = 0
    for covid_data in clustered_text:
      summary = generate_summary(covid_data)
      summaries.append(summary)
      print("Summary: ", summary) 
      print("\nlink:"+str(i), new_links[i])
      print("the value of i is",i)
      i += 1
      # if i == 3:
      #     break
    
    return summaries, new_links

  
  