import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo','bar')
re=r.get('43')
print(re)