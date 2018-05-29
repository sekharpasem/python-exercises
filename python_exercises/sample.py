from config import Config

class Sample:

	def main(self):
		for i in range(5):
			stri = Config.PREDICTION_DS_CONTRIBUTING_FACTORS+str(i)
			
			print(stri)


if __name__ == '__main__':
    Sample().main()