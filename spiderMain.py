# baike_spider
from baike_spider import url_manager, url_downloader, html_parser, html_outputer

class spiderMain (object):
    def __init__(self):
        self.url = url_manager.UrlManager()
        self.downloader = url_downloader.UrlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self,url):
        self.url.add_new_url(url)
        count = 1
        try:
            while self.url.has_new_url():
                new_url = self.url.get_new_url()
                print "craw %d: %s" % (count,new_url)
                html_doc = self.downloader.get_html(new_url)
                new_urls, new_data = self.parser.parser_html(new_url,html_doc)
                self.url.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)


                if count == 10:
                    break

                count = count + 1

        except:
            print "craw failed"

        self.outputer.output_data()



if __name__ == '__main__':
    url_root = 'http://baike.baidu.com/link?url=8vjGKITmIsUXbM3fhsdEDr8iXXDQZGQHPCb_keVkt6RYk1Zs71Gea6iwXH-wguE9p8nRbXCV9QfJz_cID2fi2a'
    spider = spiderMain()
    spider.crawl(url_root)