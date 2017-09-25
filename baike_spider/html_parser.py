from bs4 import BeautifulSoup
import re
import urlparse
class HtmlParser(object):

    def _get_urls(self,soup,page_url):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/item/'))
        for link in links:
            full_url = urlparse.urljoin(page_url,link['href'])
            new_urls.add(full_url)
        return new_urls

    def _get_data(self,soup,page_url):
        data = {}
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        data['title'] = node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        node = soup.find('div',class_="lemma-summary")
        data['summary'] = node.get_text()

        data['url'] = page_url
        return data

    def parser_html(self,page_url,doc):
        if page_url is None or doc is None:
            return 
        soup = BeautifulSoup(doc,"html.parser",from_encoding = "utf-8")
        new_urls = self._get_urls(soup,page_url)
        new_data = self._get_data(soup,page_url)
        return new_urls,new_data