import logging
import requests

from tinydb import TinyDB, Query
from html.parser import HTMLParser

class Crawler(HTMLParser):
    def __init__(self, url, key='', keys=[]):
        super(Crawler, self).__init__()
        self.results = {}

        self.url = url
        self.key = key
        self.keys = keys
        
        # Initlize tiny db
        self.tinydb_path = '/root/bland.json'

    def monitor_set_id(self, _id, data):
        """ Store the data associated with the id in json a file
        """
        db = TinyDB(self.tinydb_path)
        db.insert({'_id': _id, 'data': data})

    def monitor_get_id(self, _id):
        """ Return data from json file associated with the id.
        """
        db = TinyDB(self.tinydb_path)
        query = Query()
        result = db.search(query._id == _id)
        return result

    def start(self):
        # Get the content and close the connection.
        #res = requests.get(self.url)
        #content = res.content.decode('utf-8')
        #res.close()
        content = None
        with open('/root/fb.html', 'r') as f:
            content = f.read()
        logging.debug('content-size:{0}'.format(len(content)))
        self.feed( content ) 

    def handle_data(self, data):
        if not self.lasttag == 'p':
            return

        for subset in self.keys:
            if any(key in data.lower() for key in subset):
                continue 
            break

        # Enters here if at least one element
        # in each subset is in the title.
        else: # (happens when for-loop doesn't break)
            link_id = 1 #self.extract_id(tag, attrs)
            try: 
                int(link_id)
            except:
                return

            link = 'http://test.is' #self.monitor_get_link(tag, attrs)
            
            logging.info('Found a link {0}'.format(link))

            if self.monitor_get_id( link_id ):
                logging.info('{0} id already exists!'.format(link_id))
                pass
            else:
                self.results[link_id] = {
                    'text': data,
                    'link': link
                }
        #print("Encountered some data  :", data)

    def handle_starttag(self, tag, attrs):
        text = self.harvest_html(tag, attrs)

        if not text:
            return
        
        #logging.debug('found text: {0}'.format(text))

        for subset in self.keys:
            if any(key in text.lower() for key in subset):
                continue 
            break

        # Enters here if at least one element
        # in each subset is in the title.
        else: # (happens when for-loop doesn't break)
            link_id = self.extract_id(tag, attrs)
            try: 
                int(link_id)
            except:
                return

            link = self.monitor_get_link(tag, attrs)
            
            logging.info('Found a link {0}'.format(link))

            if self.monitor_get_id( link_id ):
                logging.info('{0} id already exists!'.format(link_id))
                pass
            else:
                self.results[link_id] = {
                    'text': text,
                    'link': link
                }
                #self.monitor_set_id(link_id, self.results[link_id]) 

    def std_out_result(self):
        """
        """
        if self.results:
            for link_id, result in self.results.items():
                print( link_id )
                print( result['text'] )
                print( result['link'] )

    def harvest_html(self, tag, attrs):
        """ Return string from the given arguments.
            The text will be used to search in for keywords.
        """
        raise NotImplemented('harvest_html not implemented!')
    
    def extract_id(self, tag, attrs):
        """ Generate a unique ID from the given data.
        """
        raise NotImplemented('extract_id not implemented!')
    
    def monitor_get_link(self, tag, attrs):
        """ Construct a link from the given data.
        """
        raise NotImplemented('monitor_get_link not implemented!')

