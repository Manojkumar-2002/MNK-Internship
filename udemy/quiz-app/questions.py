import requests

class Questions:

    def __init__(self):

        params = {
            "amount":10,
            "type":"boolean"
        }
        res = requests.get("https://opentdb.com/api.php",params=params)
        self.results = res.json()["results"]


    def get_questions(self):
        return self.results
