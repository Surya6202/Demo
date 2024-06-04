import ast

import requests


class Microservice:
    def __init__(self):
        self.response = requests

    def post_request(self, endpoint, payload):
        response = self.response.post(url=endpoint, json=payload)
        assert response.status_code == 200
        print(response.status_code)
        print('Added successfully')

    def get_request(self, endpoint):
        response = self.response.get(url=endpoint)
        assert response.status_code == 200
        print(response.status_code)
        print(response.text)

    def get_a_request(self, endpoint, data):
        response = self.response.get(url=endpoint)
        assert response.status_code == 200
        print(response.status_code)
        getdata = response.text
        assert getdata.__contains__(data)
        print(getdata)

    def update_request(self, endpoint, updated_payload):
        response = self.response.put(url=endpoint, json=updated_payload)
        assert response.status_code == 200
        print(response.status_code)
        print('Updated successfully')

    def delete_request(self, endpoint):
        response = self.response.delete(url=endpoint)
        assert response.status_code == 200
        print(response.status_code)
        print('Deleted successfully')

    @staticmethod
    def json_data(data:str):
        file = ast.literal_eval(open('testdata.json').read())
        data = data.split(',')
        if len(data) == 2:
            return file[data[0]]["payload"][int(data[1])]
        elif len(data) == 3:
            return file[data[0]]["payload"][int(data[1])][data[2]]


req = Microservice()

# category scenario:
url = req.json_data('category,0,url')
id = str(req.json_data('category,1,categoryId'))
data = req.json_data('category,1,categoryName')
updated_data = req.json_data('category,2,categoryName')
payload = req.json_data('category,1')
updated_payload = req.json_data('category,2')

req.post_request(url, payload)
req.get_request(url)
req.get_a_request(url+id,data)
req.update_request(url+id, updated_payload)
req.get_a_request(url+id, updated_data)
req.delete_request(url+id)
req.get_request(url)

# product scenario:
url = req.json_data('product,0,url')
id = str(req.json_data('product,1,productId'))
data = req.json_data('product,1,productName')
updated_data = req.json_data('product,2,productName')
payload = req.json_data('product,1')
updated_payload = req.json_data('product,2')

req.post_request(url, payload)
req.get_request(url)
req.get_a_request(url+id,data)
req.update_request(url+id, updated_payload)
req.get_a_request(url+id, updated_data)
req.delete_request(url+id)
req.get_request(url)