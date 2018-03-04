from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
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
    conn = http.client.HTTPConnection("localhost", 8080)
    headers = {'Content-type': 'application/json'}
    text_dict = {'text': text}
    text_json = json.dumps(text_dict)
    conn.request('POST', text_json, headers)
    response = conn.getresponse()
    return response.read()


if __name__ == "__main__":
  #  html = urllib.request.urlopen(sys.argv[1:]).read()
    html = urllib.request.urlopen('http://money.cnn.com/2018/03/03/news/economy/trump-tariffs-cars-trade-war-europe/index.html').read()
    print(stripHTML(html))
