import requests

url = 'http://localhost:5246/api/category/'

payload = {
    "categoryId": 7,
    "categoryName": "Beauty-products"
}

id = str(payload["categoryId"])

updated_payload = {
    "categoryId": 7,
    "categoryName": "Skincare"
}


# post_category a category:
def post_category(endpoint, payload):
    response = requests.post(url=endpoint, json=payload)
    assert response.status_code == 200
    print(response.status_code)
    print('Category added successfully')
    print(requests.get(endpoint + id).text)


post_category(url, payload)


# get all categories
def get_categories(endpoint):
    response = requests.get(url=endpoint)
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)


get_categories(url)


# get a category
def get_category(endpoint, category_name):
    response = requests.get(url=endpoint)
    assert response.status_code == 200
    print(response.status_code)
    data = response.text
    assert data.__contains__(category_name)
    print(data)


get_category(url + id, payload["categoryName"])


# update a category
def update_category(endpoint, updated_payload):
    response = requests.put(url=endpoint, json=updated_payload)
    assert response.status_code == 200
    print(response.status_code)
    print('Category updated successfully')
    print(requests.get(endpoint).text)


update_category(url + id, updated_payload)


# delete a category
def delete_category(endpoint):
    response = requests.delete(url=endpoint)
    assert response.status_code == 200
    print(response.status_code)
    print('Category deleted successfully')


delete_category(url + id)

# get all categories
get_categories(url)
