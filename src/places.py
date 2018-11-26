import falcon
import requests
import json
import re

google_key='<oak_api_key>'
oakridge_key='Oakridge'

class Places (object):
    def on_get (self, req, resp):
        if req.get_param('key') != oakridge_key:
            raise falcon.HTTPBadRequest('Invalid oak_key', 'need a valid API_KEY to proceed!')
        # use google key for real query
        # we can't use falcon build-in <req.param> because,
        # some URI with vars contain <,> will be decode wrong as saved in {dict}
        # for example: tipark2.oakridge.io:8000/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key=<key>'
        # therefore we use regex to only replace <key> with google_key
        new_relative_uri = re.sub (r'(.*&key=).*(&.*|$)', r'\1'+google_key+r'\2', req.relative_uri)
        url='https://maps.googleapis.com'+new_relative_uri
        result = requests.get (url)
        resp.status = str(result.status_code) + ' ' + result.reason
        resp.content_type = result.headers['content-type']
        resp.body = result.text

class Echo (object):
    def __call__(self, req, resp):
        result = {
            'attribute': dir(req),
            'params': req.params,
            'path': req.path,
            'relative_uri': req.relative_uri,
            'uri': req.uri,
            'prefix': req.prefix,
            'headers': req.headers,
            '_params': req._params
        }
        resp.status = falcon.HTTP_200
        resp.body=json.dumps (result, sort_keys=True, indent=4, separators=(',', ': '))
