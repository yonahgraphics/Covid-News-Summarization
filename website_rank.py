#!/usr/bin/python3
# import requests
# import sys
# from bs4 import BeautifulSoup
# import re
# import validators
# from urllib.parse import urlparse

# if len(sys.argv) !=2:
#      print("Please pass the TLD (url without http(s))")
#      print("python {0} TopLevelDomain\nEx: python {0} theayurveda.org".format(sys.argv[0]))
#      exit(0)

from imports import*

def is_valid_domain(site_name):
    if validators.domain(site_name):
        return True
    else:
        return False

def getPageRank(url): 

  alexa_base_url = 'https://alexa.com/siteinfo/'
  site_name = urlparse(url).netloc
  site_name.lower()
  if not is_valid_domain(site_name):
    print("Not a valid domain format {0} Exiting...".format(site_name))
    print("Valid Top Level Domain looks like 'theayurveda.org' or 'www.theayurveda.org' ")
    exit(0)

  url_for_rank = alexa_base_url + site_name

  # Request formatted url for rank(s)
  page = requests.get(url_for_rank)
  soup = BeautifulSoup(page.content, 'html.parser')
  #print(soup)
  # get ranks text in a list
  country_ranks = soup.find_all('div', id='CountryRank')

  # select the data with class='rank-global' and the class='data'
  global_rank = soup.select('.rank-global .data')
  #print(global_rank)

  # Display Global rank safely
  try:
      match = re.search(r'[\d,]+', global_rank[0].text.strip())
      rankGlobal =  match.group()
      #print("Global Rank: ", match.group())
  except:
      rankGlobal = 'No global rank found'
  return int(rankGlobal.replace(",",""))
