import sys
import falcon
from places import Places, Echo

p = Places()
api = falcon.API()
api.add_route ('/maps/api/geocode/json',p)
api.add_route ('/maps/api/timezone/json',p)
#e = Echo()
#api.add_sink (e, r'/.*')
