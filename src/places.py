import falcon
import requests
import json

class Places (object):
    key='google api key'
    def __call__(self, req, resp):
        echo = {
            'relative_uri': req.relative_uri
        }
        url='https://maps.googleapis.com'+req.relative_uri+'&key='+self.key
        result = requests.get (url)
        resp.status = str(result.status_code) + ' ' + result.reason
        resp.content_type = result.headers['content-type']
        resp.body = result.text
