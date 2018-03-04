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

def scrape_json(response):
    response_json = json.loads(response)
    response_list = []
    for i in range(len(response_json["entities"])):

        for j in range(len(response_json["entities"][i]["mentions"])):
            entity_list = []
            entity_list.append(response_json["entities"][i]["mentions"][j]["text"]["content"])
            entity_list.append(response_json["entities"][i]["mentions"][j]["sentiment"]["magnitude"])
            response_list.append(entity_list)
    #       print(response_json["entities"][i]["mentions"][j]["text"]["content"])
    #       print(response_json["entities"][i]["mentions"][j]["sentiment"]["magnitude"])
    #        print(response_json["entities"][i]["mentions"][j]["sentiment"]["score"])
    return response_list

def replace_substrings(html, sublist):
    for string in sublist:
        if string[0] in str(html):
            color = "0,0,255,"
            intensity = str(string[1])[0:3]
            front_div = '<div style="background-color: rgba(' + color + intensity +')">'
            end_div = '</div>'
            new_string = front_div + string[0] + end_div
            html = html.replace(string[0], new_string)
    return html

def add_class(html):
    html = html.replace("<body", '<style> .context :not(p) {background: #f1c40f; padding: 0;}</style>{<div class="context"><body', 1)
    html = html.replace("</body>", "</body></div>")
    return html


if __name__ == "__main__":
  #  html = urllib.request.urlopen(sys.argv[1:]).read()
    html = urllib.request.urlopen('http://money.cnn.com/2018/03/03/news/economy/trump-tariffs-cars-trade-war-europe/index.html').read()
    response = send_request(stripHTML(html))
    words = scrape_json(response)
    replace_substrings(html, words)
