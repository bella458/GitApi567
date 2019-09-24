""" Bella Manoim 
    Testing git567
    Unit tests to check the functions getCommits and getRepositories
"""
import unittest

from GitApi567 import getCommits, getRepositories

class Test(unittest.TestCase):

    def test_getCommits1(self):
        assert getCommits('bella458', 'SSW-555') == 4

    def test_getCommits2(self):
        assert getCommits('bella458', 'SSW567') == 3
        
    def test_getRepositories1(self):
        self.assertIn("SSW-555", getRepositories("bella458"))
    
    def test_getRepositories2(self):
        self.assertIn("SSW567", getRepositories("bella458"))

if __name__ == '__main__':
    print('Running Unit Tests')
    unittest.main()