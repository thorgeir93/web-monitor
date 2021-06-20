"""
Run with python3.5
"""
from monitor import Crawler

class BlandCrawler(Crawler):
    def extract_id(self, tag, attrs):
        """
        """
        attrs = dict(attrs)
        _id = attrs.get('href', '').split('/')
        _id = list(filter(None, _id))
        return _id.pop()
    
    def harvest_html(self, tag, attrs):
        if not tag == 'a':
            return
        
        attrs = dict(attrs)

        title = attrs.get('title')
        if not title:
            return

        return title.strip()

    def monitor_get_link(self, tag, attrs): 
        attrs = dict(attrs)
        return 'http://bland.is{0}'.format(attrs.get('href'))

sofi = {
    'keys': ( ['sófi', 'sofi'], ),
    'url': (
        'https://bland.is/solutorg/'
        'heimilid/stofa-sofi/?categoryId=29'
    )
}

hjol = {
    'keys': (
        ['hjól', 'hjol'],
    ),
    'url': (
        'https://bland.is/solutorg/'
        'ithrottir-heilsa/reidhjol/?categoryId=88'
    )
}

crawler = BlandCrawler( **sofi )
crawler.start()
crawler.std_out_result()
