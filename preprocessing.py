from imports import*
from webscraping import*
from sklearn.cluster import DBSCAN
from sklearn.cluster import SpectralClustering

def get_root_list():
    covid_vocabulary = {"Coronavirus","SARS","SARS-CoV-2","wave","Incubation","quarantine", "isolation","preventing","Covid19","Spread","disease","endemic","epidemic","outbreak","pandemic",
    "distancing","vaccine","cases","test","restrictions","hospitals","health","wear","variants","mutations","infections","mask","spike","lift","symptom","death","die","covid","doses","shots"}

    synlist=[]
    root_list = set()
    covid_vocab = set(covid_vocabulary)
    for word in covid_vocab:
      for syn in wordnet.synsets(word):
        for l in syn.lemmas():
          synlist.append(l.name())

    covid_vocab.update(synlist)

    englishStemmer=SnowballStemmer("english")
    for i in covid_vocab :
      root_list.add(englishStemmer.stem(i))
    return root_list

def lemmatization(wordlist):
    root_list = set()
    englishStemmer=SnowballStemmer("english")
    for word in wordlist:
        root_list.add(englishStemmer.stem(word))
    return root_list
 
def get_selected_news(news_df): 
    news_df['lemma'] = news_df['keywords'].apply(lemmatization)

    news_df['counter'] = 0
    news_df['related'] = False
    african_countries = get_African_Countries()
    for index,row in news_df.iterrows():
      intersection_set = set.intersection(set(row['lemma']), set(lemmatization(african_countries)))
      intersection_list = list(intersection_set)
      #print(intersection_list)
      if len(intersection_list) != 0 :
        news_df.loc[index,'related'] = True
      
    for index,row in news_df.iterrows():
      for word in row['lemma']:
        if word in get_root_list():
          news_df.loc[index,'counter'] +=1
    for index in range(len(news_df)):
      if  news_df.loc[index,'counter'] <= 2 :
        #print("*********************")
        if news_df.loc[index,'related'] == True : 
           
           news_df.loc[index,'related'] = False     
     
    selected_news = news_df[news_df['related'] == True]
    selected_news.reset_index(inplace = True)
    selected_news = selected_news.drop_duplicates(subset=['Title', 'Article'], keep='first')
    selected_news.reset_index(inplace = True)
    return selected_news

def get_article(selected_news):
    article = []
    for index in range(len(selected_news)):
      text=selected_news.loc[index,'Title']
      text += selected_news.loc[index,'Article']
      article.append(text)
    return article

#Adding all articles in a text 
def get_article_text(selected_news):
    article_text = ''
    for index in range(len(selected_news)):
      text = selected_news.loc[index,'Article']
      article_text +=''.join(text)
    return article_text
  
# def check_similarities(text):
#   id_1 = []
#   id_2 = []
#   score = []
#   indices = []
#   sorted_text =''
#   model = SentenceTransformer('bert-base-nli-mean-tokens')
#   text_embeddings = model.encode(text, batch_size = len(text), show_progress_bar = True)
#   similarities = cosine_similarity(text_embeddings)
#   similarities_sorted = similarities.argsort()
  
#   for index,array in enumerate(similarities_sorted):
#       id_1.append(index)
#       id_2.append(array[-2])
#       score.append(similarities[index][array[-2]])
#   index_df = pd.DataFrame({'id_1' : id_1,
#                             'id_2' : id_2,
#                             'score' : score})
#   index_df = index_df.sort_values(by=['score'])
  
#   return index_df
def check_similarities(text, selected_news):
  id_1 = []
  id_2 = []
  score = []
  indices = []
  sorted_text =''
  indices_cluster = {}
  clustered_text =[]
  clustered_link = []
  model = SentenceTransformer('bert-base-nli-mean-tokens')
  text_embeddings = model.encode(text, batch_size = len(text), show_progress_bar = True)
  similarities = cosine_similarity(text_embeddings)
  similarities_sorted = similarities.argsort()
  
  # clusters = DBSCAN(min_samples=1).fit_predict(similarities)
  clusters = SpectralClustering(10).fit_predict(similarities)

  for i in np. unique(clusters):
    if i in clusters:
      indices_cluster[i],= np.where(clusters == i)

  for key,value in indices_cluster.items():
    long_text = ''
    links =[]
    for index in value:
      long_text +=" " + text[index]
      links.append(selected_news.loc[index,'Link'])
    clustered_text.append(long_text)
    clustered_link.append(links)

  return clustered_text, clustered_link

 
 
############sorting the text according the similarities 
# def sort_text(index_df, article, selected_news):
#     graph = nx.from_pandas_edgelist(index_df, 'id_1', 'id_2',['score'], create_using=nx.Graph())
#     # data = {}
#     indices = []
#     sorted_text = ''
#     long_text = ""
#     link_list = []
#     for node in graph.nodes:
#       for x in list(nx.bfs_edges(graph,node)):
#         (x1,x2) = x
#         if x1 not in indices :
#           indices.append(x1)
#         if x2 not in indices : 
#           indices.append(x2)     
#     for index in indices:
#       text = article[index]
#       long_text += "*+_+*"
#       long_text += text
#       # sorted_text +=''.join(text)
#       link = selected_news.loc[index,'Link']
#       link_list.append(link)
#       # link_list.append(link)
#       # data[text] = link
#     # return sorted_text, link_list
#     return long_text, link_list