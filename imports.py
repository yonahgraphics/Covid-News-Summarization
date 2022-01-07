#from GoogleNews import GoogleNews
from bs4 import BeautifulSoup
import textwrap
import requests
from datetime import date
from newspaper import Article
from newspaper import Config
import pandas as pd
import nltk
import numpy as np
from nltk.stem.snowball import SnowballStemmer

from nltk.corpus import wordnet
nltk.download('wordnet')
from nltk.tokenize.texttiling import TextTilingTokenizer
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
from sentence_transformers import SentenceTransformer
from sentence_transformers import models, losses
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from rouge import Rouge
import requests
import sys
from bs4 import BeautifulSoup
import re
import validators
from urllib.parse import urlparse
from transformers import BartTokenizer, BartForConditionalGeneration
import torch
from transformers import PegasusTokenizer, PegasusForConditionalGeneration
import datetime
from countryinfo import* 
from website_rank import*
from preprocessing import*
from generate_summary import*
from models import*
from webscraping import*
from countryinfo import*
from sklearn.cluster import DBSCAN
