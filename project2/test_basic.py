#!/usr/bin/env python3

"""
Project 2 public tests

You can (and should) write additional tests!
"""

import unittest
import p2

class BasicTests(unittest.TestCase):

    def test_play_ipd(self):
        """TFTBot vs DefectBot for 3 rounds"""
        tft_utility, defect_utility = p2.play_ipd(p2.TFTBot(), p2.DefectBot(), 3)
        self.assertEqual(tft_utility, 2)
        self.assertEqual(defect_utility, 6)


    def test_play_tournament(self):
        """Round-robin tournament with one Cooperate, Defect and TFT Bot"""
        b = [p2.CooperateBot(), p2.DefectBot(), p2.TFTBot()]
        result = p2.play_tournament(b, 3)
        cooperate_utility = result[0][0]
        defect_utility = result[1][0]
        tft_utility = result[2][0]

        self.assertEqual(cooperate_utility, 9)
        self.assertEqual(defect_utility, 18)
        self.assertEqual(tft_utility, 11)


    def test_evolutionary_ipd(self):
        """
        Round-robin tournament of 5 Cooperate and 5 Defect bots
        
        At the end of each tournament, the lowest 2 bots are removed;
        the highest 2 bots are copied

        After a few generations, only DefectBots are left
        """
        population = ([p2.CooperateBot() for i in range(5)] 
                    + [p2.DefectBot() for i in range(5)])

        result = p2.count_bots(p2.evolutionary_ipd(population, 10, 5))

        self.assertEqual(result["DefectBot"], 10)


if __name__ == "__main__":
    unittest.main()

