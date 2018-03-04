import selenium.webdriver as webdriver
from time import sleep
import bs4

def get_results(search_term):
    MAX_LINKS = 5   # Set the maximum number of links to gather

    # Use google to search the search term
    url = "https://www.google.com"
    browser = webdriver.Chrome()
    browser.get(url)
    search_bx = browser.find_element_by_class_name('gsfi')
    search_bx.send_keys(search_term + " news")
    search_bx.submit()

    try:
        # links = browser.find_elements_by_class_name('//rc/r')
        links = browser.find_elements_by_xpath('//div//h3//a')
    except:
        print("error")

    results = []
    # retrieves first two links
    for link in links[0:MAX_LINKS]:
        # href = link.get_attribute('r')
        href = link.get_attribute('href')
        results.append(href)
    browser.close()
    return results


def write_js(urls):
    file = open("options.js", "w")
    file.write("window.addEventListener('DOMContentLoaded', function() {")
    i = 0
    for url in urls:
        file.write("var link = document.getElementById('btnOpenNewTab" + str(i) +"');")
        file.write("link.addEventListener('click', function() {")
        file.write("var newURL = \"" + url + "\";")
        file.write("chrome.tabs.create({ url: newURL });")
        file.write("});")
        i+=1
    file.write("});")
    file.close()


def write_html(urls):
    file = open("popup.html", "w")
    file.write("<!doctype html><html><head><title>Demo</title><link href=\"style.css\" rel=\"stylesheet\" type=\"text/css\"><script src=\"options.js\"></script></head><body>")
    i = 0
    for url in urls:
        file.write("<input type=\"button\" id=\"btnOpenNewTab" + str(i) + "\" value=\" " + url + "\"/>")
        i+=1
    file.write("</body></html>")
    file.close()


if __name__ == "__main__":
    results = get_results("guns")
    write_js(results)
    write_html(results)