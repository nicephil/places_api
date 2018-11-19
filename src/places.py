import falcon
import requests
import json

google_key='put google api key here'
oakridge_key='Oakridge'

class Places (object):
    def on_get (self, req, resp):
        if req.get_param('key') != oakridge_key:
            raise falcon.HTTPBadRequest('Invalid key', 'need a valid API_KEY to proceed!')
        # use google key for real query
        req.params['key']=google_key
        url='https://maps.googleapis.com'+req.path
        result = requests.get (url, req.params)
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
            'headers': req.headers
        }
        resp.status = falcon.HTTP_200
        resp.body=json.dumps (result, sort_keys=True, indent=4, separators=(',', ': '))
