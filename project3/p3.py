#!/usr/bin/env python3

import csv
import random

# Anna Blendermann

class NaiveBayes():

	"""TODO: implement Naive Bayes"""

	def __init__(self):
		self.classProbs = []
		self.demProbs = []
		self.repProbs = []


	def computeClassProbs(self, data):
		dems = 0
		reps = 0		
		for line in data:
			if line[0] == 'democrat':
				dems += 1
			else:
				reps += 1
		total = len(data)
		return {'democrat':dems/total,'republican':reps/total} 
	
	
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

			# apply add-one laplace smoothing
			probs[i]["y"] = num_y+1/len(data[i])*1
			probs[i]["n"] = num_n+1/len(data[i])*1
			probs[i]["?"] = num_q+1/len(data[i])*1		

		return probs
		 			

	def train(self, datafile):

		# load class and voting data from the datafile
		data = []
		with open(datafile, "r") as file:
			for line in file:
				data.append(line.strip().split(","))

		# compute probability of each class
		self.classProbs = self.computeClassProbs(data)

		# separate the data by class
		democrat, republican = self.separateByClass(data)

		# separate each class set by attribute	
		demAttributes = self.separateByAttribute(democrat)
		repAttributes = self.separateByAttribute(republican)

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

		To make a prediction, check out the probabilities based on
		the trained data and get P(x1|c)*P(x2|c)... P(x16|c)*P(c) 			for each class.
		"""
		results = {}
		dem_final = 1
		rep_final = 1
		for i in range(16):
			vote = evidence[i]
			dem_final *= self.demProbs[i][vote]
		
		dem_final *= self.classProbs['democrat']

		for i in range(16): 
			vote = evidence[i]
			rep_final *= self.repProbs[i][vote]

		rep_final *= self.classProbs['republican']

		# normalize the results
		dem_normal = dem_final / (dem_final + rep_final)
		rep_normal = rep_final / (dem_final + rep_final)

		results['democrat'] = dem_normal
		results['republican'] = rep_normal
		return results


def main():

	"""Example usage"""
	classifier = NaiveBayes()
	classifier.train('house-votes-84.data')
	some_dem=['y','y','y','n','y','y','n','n','n','n','y','?','y','y','y','y']
	some_rep=['n','y','n','y','y','y','n','n','n','y','?','y','y','y','n','y']

	# secret tests
	input1 =  ['y','n','y','n','y','n','y','n','y','n','y','n','y','n','y','n']
	input2 = ['n','n','n','?','?','y','y','n','n','?','?','y','y','y','n','y']
	intpu3 = ['n','n','n','n','n','n','y','y','y','n','n','n','y','y','n','n']

	dem1 = ['n','?','y','n','n','n','y','y','y','n','n','n','n','n','y','?']
	rep1 = ['n','n','n','y','y','y','?','n','n','n','n','?','y','y','y','?']

	dem2 = ['n','n','y','n','n','y','y','?','y','y','y','?','n','n','y','?']
	rep2 = ['n','y','n','y','y','y','n','?','n','n','?','n','?','y','n','?']

	dem3 = ['y','y','?','n','n','?','?','?','?','y','n','?','?','?','?','y']
	rep3 = ['y','?','?','y','y','?','?','n','?','n','n','y','y','?','n','y']

	print(classifier.predict(some_dem))
	print(classifier.predict(some_rep))

	print("secret tests")

	print(classifier.predict(input1))
	print(classifier.predict(input2))
	print(classifier.predict(intpu3))

	print("\ndemocrat, republican")
	print(classifier.predict(dem1))
	print(classifier.predict(rep1))

	print("\ndemocrat, republican")
	print(classifier.predict(dem2))
	print(classifier.predict(rep2))

	print("\ndemocrat, republican")
	print(classifier.predict(dem3))
	print(classifier.predict(rep3))
	

if __name__ == "__main__":
	main()

