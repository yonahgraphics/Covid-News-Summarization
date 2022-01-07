from flask import Flask, redirect, url_for, render_template, request
from imports import*
from models import*

news_url1 = "https://news.google.com/news?q=Africa%20Covid&hl=en-US&sort=date&gl=Africa&num=10&ceid=US%3Aen&output=rss"
summaries1, my_links1 = get_summary(news_url1, "covid cases")
news_url2 = "https://news.google.com/rss/search?q=%22vaccination%22%20in%20Africa&hl=en-US&sort=date&gl=US&num=10&ceid=US:en"
summaries2, my_links2 = get_summary(news_url2, "vacinations")


app = Flask(__name__)

data1 = summaries1
links1 = my_links1
data2 = summaries2
links2 = my_links2

links_1 = []
links_2 = []


for lin1, lin2 in zip(links1, links2):
    if len(lin1) >=2 and len(lin2) >=2:
        links_1.append(lin1[:2])
        links_2.append(lin2[:2])
    elif len(lin1) >=2 and len(lin2) <2:
        links_1.append(lin1[:2])
        links_2.append([lin1[0]])
    elif len(lin1) <2 and len(lin2) >=2:
        links_1.append([lin2[0]])
        links_2.append(lin2[:2])
    else:
        links_1.append([lin1[0]])
        links_2.append([lin2[0]])
       

@app.route('/', methods=['GET'])
def home():

    cardTitle1 = "Cases"
    cardTitle2 = "Vaccinations"
  

    if request.method == 'GET':
        return render_template('index.html',
        card_title1=cardTitle1,
         card_title2=cardTitle2,
          data_link1 = zip(data1,links_1),
          data_link2 = zip(data2,links_2),
           )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


