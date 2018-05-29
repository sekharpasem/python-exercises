import textrazor
textrazor.api_key = "dc6fe1bad26d32afe2c1abb394588cff198b87bd5585fdc3130f3b88"
client = textrazor.TextRazor(extractors=["entities", "topics"])
client.set_cleanup_mode("cleanHTML")
client.set_classifiers(["textrazor_newscodes"])
response = client.analyze_url("http://www.bbc.co.uk/news/uk-politics-18640916")
entities = list(response.entities())
entities.sort(key=lambda x: x.relevance_score, reverse=True)
seen = set()
for entity in entities:
	if entity.id not in seen:
		print(entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types)
		seen.add(entity.id)


for category in response.categories():
	print category.category_id, category.label, category.score