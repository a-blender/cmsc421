#!/usr/bin/env python3

"""
Project 3 public tests

You can (and should) write additional tests!
"""

import unittest
import p3

all_yes = ['y' for i in range(16)]
all_no = ['n' for i in range(16)]
all_abstain = ['?' for i in range(16)]

class BasicTests(unittest.TestCase):

    def test_all_normalization(self):
        """Sanity check; test against full dataset"""
        classifier = p3.NaiveBayes()
        classifier.train('house-votes-84.data')

        prediction = classifier.predict(all_yes)
        self.assertAlmostEqual(prediction['democrat']
                               + prediction['republican'], 1)

        prediction = classifier.predict(all_no)
        self.assertAlmostEqual(prediction['democrat']
                               + prediction['republican'], 1)


    def test_tiny(self):
        """Tests on tiny.data"""
        classifier = p3.NaiveBayes()
        classifier.train('tiny.data')

        all_yes_prediction = classifier.predict(all_yes)
        all_no_prediction = classifier.predict(all_no)
        all_abstain_prediction = classifier.predict(all_abstain)

        self.assertAlmostEqual(all_abstain_prediction['democrat'], 0.5)
        self.assertAlmostEqual(all_abstain_prediction['republican'], 0.5)
        self.assertGreater(all_yes_prediction['democrat'], 0.9)
        self.assertGreater(all_no_prediction['republican'], 0.9)


if __name__ == "__main__":
    unittest.main()

