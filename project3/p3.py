#!/usr/bin/env python3

import csv
import random

# Anna Blendermann

class NaiveBayes():

	"""TODO: implement Naive Bayes"""

	def __init__(self):
		self.demProbs = []
		self.repProbs = []

	
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
			data[i].pop(0)
		
		attributes = [[]]*16
		for i in range(len(data)):
			for j in range(16):
				attributes[j].append(data[i][j])

		attributes = [[sub[i] for sub in data] for i in range(16)]
		return attributes	


	def computeProbabilities(self, data):
		""" 
		For each attribute, compute a dictionary of probs with 			values P(y), P(n), and P(?)
		"""
		probs = [{}]*16
		for i in range(len(data)):
			num_y = 0
			num_n = 0
			num_q = 0
			for j in range(len(data[i])):
				vote = data[i][j]
				if vote == "y":
					num_y += 1
				elif vote == "n":
					num_n += 1
				else:
					num_q += 1
			probs[i]["y"] = num_y/len(data[i])
			probs[i]["n"] = num_n/len(data[i])
			probs[i]["?"] = num_q/len(data[i])		
		 
		return probs
		 			

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
		Naive bayes uses the frequencies of each attribute
		relative to it's class to compute conditional probs
		using laplace smoothing 
		"""
		self.demProbs = self.computeProbabilities(demAttributes)
		self.repProbs = self.computeProbabilities(repAttributes)
		pass


	def predict(self, evidence):
		"""
		Return map of {'class': probability, ...}, based on 			evidence
		"""

		print("Democrat probabilities***************")
		for line in self.demProbs:
			print(line)
		print("Republican probabilities***************")
		for line in self.repProbs:
			print(line)

		"""
		To make a prediction, check out the probabilities based on
		the trained data and get P(x1|c)*P(x2|c)... P(x16|c) for 
		each class. Then, take the max(d,r).
		"""
		results = {}
		dem_final = 1
		rep_final = 1
		for i in range(16):
			vote = evidence[i]
			print("DEMOCRAT: ",self.demProbs[i][vote])
			dem_final *= self.demProbs[i][vote]

		for i in range(16): 
			vote = evidence[i]
			print("REPUBLICAN: ",self.repProbs[i][vote])
			rep_final *= self.repProbs[i][vote]

		results['democrat'] = dem_final
		results['republican'] = rep_final
		return results


def main():

	"""Example usage"""
	classifier = NaiveBayes()
	# classifier.train('house-votes-84.data')
	classifier.train('tiny.data')

	some_dem=['y','y','y','n','y','y','n','n','n','n','y','?','y','y','y','y']
	dem2=['y','y','y','n','y','y','n','n','n','n','y','n','y','y','y','y']

	some_rep=['n','y','n','y','y','y','n','n','n','y','?','y','y','y','n','y']

	print(classifier.predict(dem2))

	#print(classifier.predict(some_rep))  


if __name__ == "__main__":
	main()

