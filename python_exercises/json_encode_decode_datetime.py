from datetime import datetime
import json
from json import JSONDecoder
from json import JSONEncoder
import re

jsonData =open('sample.json')
print(jsonData.name)
print(type(jsonData))
jsonData = json.load(jsonData)
print(jsonData)
print(type(jsonData))
jsonStr = json.dumps(jsonData,cls=JSONEncoder)
print(jsonStr)
print(type(jsonStr))

class ISODateJSONDecoder(json.JSONDecoder):
  """ JSON Decoder that transforms ISO time format representations into datetime.datetime """
  iso_datetime_regex = re.compile("[0-3][0-9]\/[0-1][0-9]\/[0-9]{4} [0-1][0-9]:[0-5][0-9]:[0-5][0-9]")
  DATE_FORMAT = '%d/%m/%Y %H:%M:%S'

  def __init__(self, *args, **kwargs):
  	print("ISODateJSONDecoder. __init__")
  	json.JSONDecoder.__init__(self, *args, **kwargs)
  	self.parse_string = self.new_scanstring
  	self.scan_once = json.scanner.py_make_scanner(self)

  def new_scanstring(self, s, end, encoding=None, strict=True):
  	print("ISODateJSONDecoder. new_scanstring")
  	#print(s,end)
  	(s, end) = json.decoder.scanstring(s, end, encoding)
  	if self.iso_datetime_regex.match(s):
  		print("ISODateJSONDecoder Matched...****datetime")
  		return (datetime.strptime(s, self.DATE_FORMAT), end)
  	else:
  		print("new_scanstring Else.....")
  		return (s, end)

class ISODateJSONEncoder(json.JSONEncoder):
  DATE_FORMAT = '%d/%m/%Y %H:%M:%S'
  def default(self, obj):
  	print("ISODateJSONEncoder default")
  	if isinstance(obj, datetime):
  		print("isinstance datetime")
  		return obj.strftime(self.DATE_FORMAT)
  	else:
  		print("isinstance datetime false")
  		return json.JSONEncoder.default(self, obj)

class Main:
	def main(self):
		profile = json.loads(jsonStr, cls=ISODateJSONDecoder)
		print("In main...")
		print(profile)
		print(type(profile))
		o1 = json.dumps(profile, cls=ISODateJSONEncoder)
		print("o1*****")
		print(o1)
		print(type(o1))
		o2 = json.loads(o1, cls=ISODateJSONDecoder)
		print("o2***	")
		print(o2)
		print(type(o2))
Main().main()