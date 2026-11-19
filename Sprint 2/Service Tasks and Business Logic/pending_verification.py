def mark_pending_verification(product):

    if (
        product.get("productValid") is True
        and product.get("isOrganicCertified") is True
        and product.get("certificationStatus") == "UNAVAILABLE"
    ):
        return {
            "listingStatus": "PENDING_VERIFICATION"
        }

    return {"listingStatus": "NOT_PUBLISHED"}


# Test 1: Certification unavailable
print("Test 1:", mark_pending_verification({
    "productValid": True,
    "isOrganicCertified": True,
    "certificationStatus": "UNAVAILABLE"
}))

# Test 2: Invalid certification
print("Test 2:", mark_pending_verification({
    "productValid": True,
    "isOrganicCertified": True,
    "certificationStatus": "INVALID"
}))