import requests

url = "https://parasrana7.pythonanywhere.com/api/products/"

response = requests.get(url)                                    # Sending a GET request to the API

if response.status_code == 200:                                 # Checking if the request was successful (status code 200)
    
    data = response.json()                                      # Parse the JSON data from the response
    
    products = data['product']                                  # Extract the list of products
  
    for p in products:                                          # Loop through each product and print details
        product_name = p['productName']
        product_price = p['productPrice']
        product_qty = p['productQty']
        product_image = p['productImage']
        category_name = p['category']['categoryName']
        
        print(f"Product Name: {product_name}")                  # Print out the product details
        print(f"Price: {product_price}")
        print(f"Quantity: {product_qty}")
        print(f"Image: {product_image}")
        print(f"Category: {category_name}")
        print("-" * 40)                                         # Separator line
        
else:
    print(f"Failed to fetch data: {response.status_code}")




url2 = "https://parasrana7.pythonanywhere.com/api/products/?id=1"

response = requests.get(url2)                                   # Sending a GET request to the API

if response.status_code == 200:
    
    data = response.json()                                      # Parse the JSON data from the response
    
    product = data['product']                                   # Extract the single product
    
    product_name = product['productName']                       # Extract product details
    product_price = product['productPrice']
    product_qty = product['productQty']
    product_image = product['productImage']
    category_name = product['category']['categoryName']
    
    print(f"Product Name: {product_name}")                      # Print out the product details
    print(f"Price: {product_price}")
    print(f"Quantity: {product_qty}")
    print(f"Image: {product_image}")
    print(f"Category: {category_name}")
    
else:
    print(f"Failed to fetch data: {response.status_code}")


url3 = "https://parasrana7.pythonanywhere.com/api/categories/"

response = requests.get(url3)                                    # Sending a GET request to the API

if response.status_code == 200:                                 # Checking if the request was successful (status code 200)
    
    data = response.json()                                      # Parse the JSON data from the response
    
    categories = data['categories']                              # Extract the list of products
  
    for c in categories:                                          # Loop through each product and print details
        category_name = c['categoryName']
        category_description = c['categoryDescription']
        category_image = c['categoryImage']
        
        print(f"Category Name: {category_name}")                  # Print out the categories details
        print(f"category Description: {category_description}")
        print(f"Category Image: {category_image}")
        print("-" * 40)                                         # Separator line
        
else:
    print(f"Failed to fetch data: {response.status_code}")