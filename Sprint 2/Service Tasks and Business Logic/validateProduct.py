
#For validation, my code checks whether the product has a valid name, a positive price and a non-negative stock quantity.
#  I tested this using valid product information, an invalid price and a negative stock quantity.
#hese tests help me check that the individual business rules behave as expected before they're integrated into the workflow.
def validate_product(product):

    # Check the product name
    name_valid = (
        isinstance(product.get("productName"), str)
        and bool(product["productName"].strip())
    )

    # Check the price
    price = product.get("productPrice")
    price_valid = (
        type(price) in (int, float)
        and 0 < price < float("inf")
    )

    # Check the stock quantity
    stock = product.get("stockQuantity")
    stock_valid = (
        type(stock) is int
        and stock >= 0
    )

    # Check whether everything is valid
    product_valid = name_valid and price_valid and stock_valid

    return {"productValid": product_valid}


# Test 1: Valid product
print("Test 1:", validate_product({
    "productName": "Carrots",
    "productPrice": 3.50,
    "stockQuantity": 20
}))

# Test 2: Invalid price
print("Test 2:", validate_product({
    "productName": "Carrots",
    "productPrice": -2,
    "stockQuantity": 20
}))

# Test 3: Invalid stock
print("Test 3:", validate_product({
    "productName": "Potatoes",
    "productPrice": 2.50,
    "stockQuantity": -5
}))
