import falcon
from places import Places

p = Places()
api = falcon.API()
api.add_sink (p, r'.*')
