import requests

url = 'http://localhost:5246/api/product/'

payload = {
    "productId": 9,
    "productName": "Boat Smart watch",
    "categoryId": 4
}

id = str(payload["productId"])

updated_payload = {
    "productId": 9,
    "productName": "Sony Smart Watch",
    "categoryId": 4
}


# Post a product:
def post_product(endpoint, payload):
    response = requests.post(url=endpoint, json=payload)
    assert response.status_code == 200
    print(response.status_code)
    print('Product added successfully')
    print(requests.get(endpoint + id).text)


post_product(url, payload)


# sleep(10)

# get all products
def get_products(endpoint):
    response = requests.get(url=endpoint)
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)


get_products(url)


# get a product
def get_product(endpoint, product_name):
    response = requests.get(url=endpoint)
    assert response.status_code == 200
    print(response.status_code)
    data = response.text
    assert data.__contains__(product_name)
    print(data)


get_product(url + id, payload["productName"])


# update a product
def update_product(endpoint, updated_payload):
    response = requests.put(url=endpoint, json=updated_payload)
    assert response.status_code == 200
    print(response.status_code)
    print('Product updated successfully')
    print(requests.get(endpoint).text)


update_product(url + id, updated_payload)


# delete the product
def delete_product(endpoint):
    response = requests.delete(url=endpoint)
    assert response.status_code == 200
    print(response.status_code)
    print('Product deleted successfully')


delete_product(url + id)

# get all products
get_products(url)
