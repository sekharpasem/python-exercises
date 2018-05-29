import json
from datetime import datetime

'''Create an encoder subclassing JSON.encoder. 
Make this encoder aware of our classes (e.g. datetime.datetime objects) 
'''
class Encoder(json.JSONEncoder):
    def default(self, obj):
        print("Called default")
        if isinstance(obj, datetime):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)

o = {
    'a': {
        'boo': 'far',
        'created': datetime.now(),
    },
    'foo': 'Bar',
}

print(json.dumps(o, cls=Encoder, indent=4))