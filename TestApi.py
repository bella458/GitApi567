""" Bella Manoim 
    Test file for GitApi567
    Unit tests to check the functions getCommits and getRepositories
    
    Updated: HW05a_Mocking
    Purpose is to use a mocking package to "mock" this program's external dependence on GitHub
"""
import unittest
from unittest import mock
from unittest.mock import MagicMock
import GitApi567
from GitApi567 import getCommits, getRepositories

class TestApi(unittest.TestCase):
            
    mockedReq = mock.Mock()

    #'requests.get' 
    @mock.patch('GitApi567.getCommits')
    def test_getCommits(self, mockedReq):
        #use side effect 
        mockedReq.side_effect = [3]
        mockedReq.return_value = MagicMock(3)
        # assign value to attribute in the mock
        mockedReq.configure_mock(repo='SSW567')
        assert mockedReq.repo == 'SSW567'
        self.assertEqual(GitApi567.getCommits("Bella458", "SSW567"), 3)

    #'requests.get'
    @mock.patch('GitApi567.getRepositories')   
    def test_getRepositories(self, mockedReq):
        mockedReq.return_value = ["SSW567"]
        mockedReq.side_effect = ["Bella458"]
        self.assertIn(GitApi567.getRepositories("SSW567"), "Bella458")

if __name__ == '__main__':
    print('Running Unit Tests')
    unittest.main()
