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


def replace_substrings(html, sublist):
    for string in sublist:
        if string in html:
            print(string)
            front_div = '<div class="highlight">'
            end_div = '</div>'
            new_string = front_div + string + end_div
            html = html.replace(string, new_string)
    return html


if __name__ == "__main__":
    #  html = urllib.request.urlopen(sys.argv[1:]).read()
    html = urllib.request.urlopen('http://money.cnn.com/2018/03/03/news/economy/trump-tariffs-cars-trade-war-europe/index.html').read()
    print(stripHTML(html))
    strings = ["Personal Finance", "dow 30"]
    print(replace_substrings(str(html), strings))