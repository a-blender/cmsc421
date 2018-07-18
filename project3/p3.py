#!/usr/bin/env python3

# YOUR NAME HERE

class NaiveBayes():
    """TODO: implement Naive Bayes"""
    def train(self, datafile):
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
        Return map of {'class': probability, ...}, based on evidence
        """
        return {'democrat': 0.5, 'republican': 0.5}


def main():
    """Example usage"""

    classifier = NaiveBayes()
    
    classifier.train('house-votes-84.data')

    some_dem=['y','y','y','n','y','y','n','n','n','n','y','?','y','y','y','y']
    some_rep=['n','y','n','y','y','y','n','n','n','y','?','y','y','y','n','y']

    print(classifier.predict(some_dem))
    print(classifier.predict(some_rep))  


if __name__ == "__main__":
    main()

