def verify_certification(product):

    # Obtain simulated certification result
    result = product.get("verificationResult")

    if result == "VALID":
        status = "VALID"

    elif result == "INVALID":
        status = "INVALID"

    else:
        status = "UNAVAILABLE"

    return {"certificationStatus": status}


# Test 1: Valid certification
print("Test 1:", verify_certification({
    "verificationResult": "VALID"
}))

# Test 2: Invalid certification
print("Test 2:", verify_certification({
    "verificationResult": "INVALID"
}))

# Test 3: Verification unavailable
print("Test 3:", verify_certification({
    "verificationResult": "UNAVAILABLE"
}))