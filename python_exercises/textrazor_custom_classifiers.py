import textrazor
textrazor.api_key = "dc6fe1bad26d32afe2c1abb394588cff198b87bd5585fdc3130f3b88"
manager = textrazor.ClassifierManager()
csv_contents = open("sports_classifier.csv").read()
print(csv_contents)

manager.create_classifier_with_csv("my_sports", csv_contents)