import urllib2
class UrlDownloader(object):

    def get_html(self,url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            print "no"
            return None

        return response.read()




