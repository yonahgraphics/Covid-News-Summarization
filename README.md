# Covid News Summarizer

Covid news summarizer is a tool built entirely in python that is used to scrape, preprocess and summarize covid news around Africa.

## Installation

The easiest way to install it is by installing all the necessary depencdecies and then running the Flask app.

```python
pip install beautifulsoup4==4.10.0
pip install bs4==0.0.1
pip install certifi==2021.10.8
pip install charset-normalizer==2.0.9
pip install click==8.0.3
pip install colorama==0.3.9
pip install cssselect==1.1.0
pip install decorator==5.1.0
pip install feedfinder2==0.0.4
pip install feedparser==6.0.8
pip install filelock==3.4.0
pip install Flask==2.0.2
pip install huggingface-hub==0.2.1
pip install idna==3.3
pip install itsdangerous==2.0.1
pip install jieba3k==0.35.1
pip install Jinja2==3.0.3
pip install joblib==1.1.0
pip install lxml==4.6.4
pip install MarkupSafe==2.0.1
pip install newspaper3k==0.2.8
pip install nltk==3.6.5
pip install numpy==1.21.4
pip install packaging==21.3
pip install pandas==1.3.4
pip install Pillow==8.4.0
pip install pyparsing==3.0.6
pip install python-dateutil==2.8.2
pip install pytz==2021.3
pip install PyYAML==6.0
pip install regex==2021.11.10
pip install requests==2.26.0
pip install requests-file==1.5.1
pip install rouge==1.0.1
pip install sacremoses==0.0.46
pip install sentence-transformers==2.1.0
pip install sentencepiece==0.1.96
pip install scikit-learn==1.0.1
pip install scipy==1.7.3
pip install sgmllib3k==1.0.0
pip install six==1.16.0
pip install soupsieve==2.3.1
pip install threadpoolctl==3.0.0
pip install tinysegmenter==0.3
pip install tldextract==3.1.2
pip install tokenizers==0.10.3
pip install torchaudio==0.10.0+cu111
pip install torchsummary==1.5.1
pip install torchtext==0.11.0
pip install torchvision==0.11.1+cu111
pip install tqdm==4.62.3
pip install transformers==4.12.5
pip install typing-extensions==4.0.1
pip install urllib3==1.26.7
pip install validators==0.18.2
pip install Werkzeug==2.0.2
pip install wordnet==0.0.1b2
```

Then you will be able to import the all theses libraries and use their functionalities.

## Description of the modules
Below is a brief description of the different modules and what they do.

### Imports.py

This module contains all the imports statement required to run the all the libraries used in the project.

### webscraping.py and countryinfo.py

In this module,we scraped google news website related to covid and parsed them.We used Google News and newspaper libraries for parsing the article and being able to fetch data. Given the time period and query on which you want to search the news articles, we would get a list which will contain date, title, link,article. Given the scope of the project was restricted  to the African context,we proceeded with web scraping using various key words such African countries contained in countryinfo.py combined with terms such as covid or vaccinations.Furthermore, given limitations on the size of the dashboard, and relevancy of the data (more recent information preferred), we concentrated on results no older than 2 days from the current date.As result,we generated a dataframe containing the title,date of publication,text and keywords of each article.


### preprocessing.py

Given that the results returned by google search are not always relevant to the query submit, an additional layer of data preprocessing was required. At this stage, for each article the keywords were identified. The keywords are most frequent words in text, or the entities recognized in text. Keywords were both used to eliminate articles that are not related to covid or articles that are out of African context. Keeping articles containing at least two keywords in the compiled list of words related to Covid.

Certain number of articles scrapped are approximately similar or complementing each other. To maintain coherence, at this stage the similarity score between one article to another was computed. We first transformed the articles text into word embedding or real-valued vectors using a sentence transformer. This results in vectors that are similar for words that appear in similar contexts, and thus have a similar meaning which enabled us to handle synonyms or words with similar meaning in the text and then we computed their similarity score using cosine similarity. The articles were clustered and combined according to their similarity score.


### models.py

The combined articles went through a text preprocessing process such as  tokenization. The combined articles were divided into chunks of length that could be processed by the model and then they are summarized  using BART which uses a combination of concepts from BERT and GPT using Bidirectional and Auto-Regressive Transformers to train the model. Depending on the results, we improved the previous stages (web scraping, document filtering and similarity).


### generate_summary.py 

In this module,we combine all the above module to generate summary with respect to the url that was passed in. 

## Running the app (Usage)
To run the app, run the file, ```app.py``` on your local computer and preview the app in the browswer

## Contribution

Pull requests are welcome. We will review your code and incoporate it into the project.

## Support

There are many ways to support a project - starring⭐️ the GitHub repo is just one.
