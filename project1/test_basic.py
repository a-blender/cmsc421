#!/usr/bin/env python3

"""
Project 1 public tests
You can (and should) write additional tests!
"""

import unittest
import p1

class BasicTests(unittest.TestCase):

    def test_island(self):
        candidate_sol = p1.find_path(p1.parse_map("island.txt"), 1, 1, 3, 4)
        true_sol = ['d', 'd', 'r', 'r', 'r']

        self.assertEqual(candidate_sol, true_sol)

    def test_hill(self):
        candidate_sol = p1.find_path(p1.parse_map("hill.txt"), 0, 0, 0, 3)
        true_sol = ['r', 'r', 'r']

        self.assertEqual(candidate_sol, true_sol)

    def test_mountain(self):
        candidate_sol = p1.find_path(p1.parse_map("mountain.txt"), 0, 0, 0, 2)
        true_sol = ['d', 'd', 'd', 'r', 'r', 'u', 'u', 'u']

        self.assertEqual(candidate_sol, true_sol)


if __name__ == "__main__":
    unittest.main()

