from datetime import datetime
import json
from json import JSONDecoder
from json import JSONEncoder
import re
from bson import ObjectId

class DateTimeDecoder(json.JSONDecoder):
  def __init__(self, *args, **kargs):
    JSONDecoder.__init__(self, object_hook=self.dict_to_object,
                         *args, **kargs)

  def dict_to_object(self, d):
    if '__type__' not in d:
      return d

    type = d.pop('__type__')
    try:
      dateobj = datetime(**d)
      return dateobj
    except:
      d['__type__'] = type
      return d


class DateTimeEncoder(JSONEncoder):
  """ Instead of letting the default encoder convert datetime to string,
      convert datetime objects into a dict, which can be decoded by the
      DateTimeDecoder
  """

  def default(self, obj):
    if isinstance(obj, datetime):
      return {
        '__type__': 'datetime',
        'year': obj.year,
        'month': obj.month,
        'day': obj.day,
        'hour': obj.hour,
        'minute': obj.minute,
        'second': obj.second,
        'microsecond': obj.microsecond,
      }
    else:
      return JSONEncoder.default(self, obj)

class ISODateJSONDecoder(json.JSONDecoder):
  """ JSON Decoder that transforms ISO time format representations into datetime.datetime """
  iso_datetime_regex = re.compile("[0-3][0-9]\/[0-1][0-9]\/[0-9]{4} [0-1][0-9]:[0-5][0-9]:[0-5][0-9]")
  DATE_FORMAT = '%d/%m/%Y %H:%M:%S'

  def __init__(self, *args, **kwargs):
    json.JSONDecoder.__init__(self, *args, **kwargs)
    self.parse_string = self.new_scanstring
    self.scan_once = json.scanner.py_make_scanner(self)

  def new_scanstring(self, s, end, encoding=None, strict=True):
    (s, end) = json.decoder.scanstring(s, end, encoding)
    if self.iso_datetime_regex.match(s):
      return (datetime.strptime(s, self.DATE_FORMAT), end)
    else:
      return (s, end)


class ISODateJSONEncoder(json.JSONEncoder):
  DATE_FORMAT = '%d/%m/%Y %H:%M:%S'

  def default(self, obj):
    if isinstance(obj, datetime):
        return obj.strftime(self.DATE_FORMAT)
    if isinstance(obj, ObjectId):
      return str(obj)
    else:
        return json.JSONEncoder.default(self, obj)