from pymongo.mongo_client import MongoClient
client = MongoClient("mongodb://dev:secret@aws-us-east-1-portal.25.dblayer.com:28209/ascension?ssl=true&ssl_cert_reqs=CERT_NONE&authMechanism=SCRAM-SHA-1")
db = client.get_database()
collection = db['metrics']
cursor = collection.find({})
print(cursor)
output =[]
for doc in cursor:
	output.append(doc)
print(output)
