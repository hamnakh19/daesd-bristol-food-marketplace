#For publication, my code uses the validation result and organic certification status to decide whether the product should be published.
#  I tested scenarios including valid non-organic products, verified organic products and cases where certification verification is unavailable.
#I also worked on the logic for handling pending verification, so a product is not automatically published when certification cannot be confirmed.
def publish_product(product):

    # Check if the product details are valid
    product_valid = product.get("productValid") is True

    # Check if organic certification is claimed
    is_organic = product.get("isOrganicCertified")

    # Check the certification result
    certification_status = product.get("certificationStatus")

    # Decide whether the product can be published
    can_publish = (
        product_valid
        and (
            is_organic is False
            or (
                is_organic is True
                and certification_status == "VALID"
            )
        )
    )

    # Return the product's listing status
    if can_publish:
        return {"listingStatus": "PUBLISHED"}
    else:
        return {"listingStatus": "NOT_PUBLISHED"}


# Test 1: Valid non-organic product
print("Test 1:", publish_product({
    "productValid": True,
    "isOrganicCertified": False
}))

# Test 2: Valid organic product with certification
print("Test 2:", publish_product({
    "productValid": True,
    "isOrganicCertified": True,
    "certificationStatus": "VALID"
}))

# Test 3: Invalid product
print("Test 3:", publish_product({
    "productValid": False,
    "isOrganicCertified": False
}))

# Test 4: Organic verification unavailable
print("Test 4:", publish_product({
    "productValid": True,
    "isOrganicCertified": True,
    "certificationStatus": "UNAVAILABLE"
}))
