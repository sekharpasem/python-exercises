import re

base_url = "https://www.universalorlando.com/web/proxy/service/k2/en/us/"
url = 'https://www.universalorlando.com/web/en/us/things-to-do/dining/bumblebee-mans-taco-truck/index.html'

def replace(index1, index2, mainstring, replacementstring):

 	return mainstring.replace(mainstring[index1:index2], replacementstring)


i= url.find('things-to-do')
print(i)
if i!=-1:
	print(" found...")
else:
	print("not found")
print(url[:i])
print(url[i:])

final = replace(0,i, url, base_url)
print(final)