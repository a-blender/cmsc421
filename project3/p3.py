#!/usr/bin/env python3

import csv
import random

# Anna Blendermann

class NaiveBayes():

	"""TODO: implement Naive Bayes"""

	def splitDataset(self, dataset, splitRatio):
		trainSize = int(len(dataset) * splitRatio)
		trainSet = []
		copy = list(dataset)
		while len(trainSet) < trainSize:
			index = random.randrange(len(copy))
			trainSet.append(copy.pop(index))
		return [trainSet, copy]


	def separateByClass(self, data):
		democrat = []
		republican = []
		for i in range(len(data)):
			if data[i][0] == "democrat":
				democrat.append(data[i])
			else:
				republican.append(data[i]) 
		return democrat, republican


	def separateByAttribute(self, data):
		attributes = []

		for i in range(16):
			dict = {}
			dict["y"] = 0
			dict["n"] = 0
			dict["?"] = 0
			attributes.append(dict)

		for i in range(len(data)):
			for v in range(1,16):
				attributes[v][data[i][v]] += 1
		return attributes				


	def train(self, datafile):

		# load class and voting data from the datafile
		data = []
		with open(datafile, "r") as file:
			for line in file:
				data.append(line.strip().split(","))

		print("Data**************")
		for line in data:
			print(line)

		# separate the data by class
		democrat, republican = self.separateByClass(data)
		print("Democrat class***************")
		for line in democrat:
			print(line)
		print("Republican class***************")
		for line in republican:
			print(line)

		# separate each class set by attribute	
		demAttributes = self.separateByAttribute(democrat)
		repAttributes = self.separateByAttribute(republican)

		print("Democrat attributes***************")
		for line in demAttributes:
			print(line)
		print("Republican attributes***************")
		for line in repAttributes:
			print(line) 

		# compute conditional probabilities

		






		
		"""
		Train a Naive Bayes on the data in datafile.

		datafile will always be a file in the same format as
		house-votes-84.data, i.e. a comma-seperated values file where
		the first field is the class and the other 16 fields are 'y',
		'n' or '?'.
		
		train() should estimate the appropriate probabilities from
		datafile. The conditional probabilities should be estimated
		with Laplace smoothing (also known as add-one smoothing).
		"""
		pass


	def predict(self, evidence):
		"""
		Return map of {'class': probability, ...}, based on 			evidence
		"""
		return {'democrat': 0.5, 'republican': 0.5}


def main():
	"""Example usage"""

	classifier = NaiveBayes()
	# classifier.train('house-votes-84.data')
	classifier.train('tiny.data')
							#some_dem=['y','y','y','n','y','y','n','n','n','n','y','?','y','y','y','y']
	#some_rep=['n','y','n','y','y','y','n','n','n','y','?','y','y','y','n','y']

	#print(classifier.predict(some_dem))
	#print(classifier.predict(some_rep))  


if __name__ == "__main__":
	main()

