from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import http.client
import requests
import json
# import sys

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def stripHTML(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

def send_request(text):
    r = requests.post("http://localhost:8080", data={'data':stripHTML(html).replace('  ', '')})

def send_request_(text):
    conn = http.client.HTTPConnection("localhost", 8080)
    headers = {'Content-type': 'application/json'}
    text_dict = {'text': text}
    text_json = json.dumps(text_dict)
    conn.request('POST', text_json, json.dumps(headers))
    response = conn.getresponse()
    print(response.status, response.reason)
    print(response.read())
    return conn.close()


if __name__ == "__main__":
  #  html = urllib.request.urlopen(sys.argv[1:]).read()
    html = urllib.request.urlopen('http://money.cnn.com/2018/03/03/news/economy/trump-tariffs-cars-trade-war-europe/index.html').read()
    send_request(stripHTML(html))
