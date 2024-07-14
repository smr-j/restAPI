'''
Jayati Samar
Last edited: 07/13/2024
Associated with: CS6620: Cloud Computing - REST API Assignment
Objective: This file contains tests for use with the REST API Assignment.
'''
import unittest
import requests
import os


class RESTTest(unittest.TestCase):
	def test_get_songs(self):
		url = os.environ.get('URL') + '/songs'
		response = requests.get(url)
		self.assertEqual(response.status_code, 200)
          
	def test_add_song(self):
		new_song = {"id": 4,
        "title":"Bethlehem Steel",
        "artist":"Delta Rae",
        "album":"After It All",
        "release":"04-07-2017",
        "spotify link":"https://open.spotify.com/track/0mwXgKxOrmSk2veQkLbWSJ?si=3b0d11732d134fda"
        }
		url = os.environ.get('URL') + '/songs'
		response = requests.post(url,json=new_song)
		self.assertEqual(response.status_code, 201)

	def test_update_song(self):
		updated_song = {
		"id": 2,
        "title":"Storm Song",
        "artist":"PHILDEL",
        "album":"The Disappearance of the Girl",
        "release":"02-04-2014",
        "spotify link":"https://open.spotify.com/track/5GTziJvDhtcCR6kCr6Ir8r?si=c3ef1d4ee015422a"
		}
		url = os.environ.get('URL') + '/songs/2'
		response = requests.put(url, json=updated_song)
		self.assertEqual(response.status_code, 200)
    
	def test_delete_song(self):
		url = os.environ.get('URL') + '/songs/2'
		response = requests.delete(url)
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()