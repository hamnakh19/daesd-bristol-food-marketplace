from datetime import date


def update_availability(product):

    stock = product.get("updatedStockQuantity")
    start = product.get("availabilityStartDate")
    end = product.get("availabilityEndDate")

    # Validate stock quantity
    stock_valid = type(stock) is int and stock >= 0

    # Validate seasonal dates
    try:
        start_date = date.fromisoformat(start)
        end_date = date.fromisoformat(end)
        dates_valid = start_date <= end_date
    except (ValueError, TypeError):
        dates_valid = False

    inventory_valid = stock_valid and dates_valid

    # Determine product availability
    if not stock_valid:
        status = "INVALID_STOCK"

    elif not dates_valid:
        status = "INVALID_DATES"

    elif stock == 0:
        status = "OUT_OF_STOCK"

    elif start_date <= date.today() <= end_date:
        status = "AVAILABLE"

    else:
        status = "OUT_OF_SEASON"

    return {
        "inventoryValid": inventory_valid,
        "availabilityStatus": status
    }


# Testing
if __name__ == "__main__":

    # Test 1: Available product
    print("Test 1:", update_availability({
        "updatedStockQuantity": 20,
        "availabilityStartDate": "2026-01-01",
        "availabilityEndDate": "2026-12-31"
    }))

    # Test 2: Out of stock
    print("Test 2:", update_availability({
        "updatedStockQuantity": 0,
        "availabilityStartDate": "2026-01-01",
        "availabilityEndDate": "2026-12-31"
    }))

    # Test 3: Outside season
    print("Test 3:", update_availability({
        "updatedStockQuantity": 15,
        "availabilityStartDate": "2026-01-01",
        "availabilityEndDate": "2026-03-31"
    }))

    # Test 4: Invalid stock
    print("Test 4:", update_availability({
        "updatedStockQuantity": -5,
        "availabilityStartDate": "2026-01-01",
        "availabilityEndDate": "2026-12-31"
    }))

    # Test 5: Invalid seasonal dates
    print("Test 5:", update_availability({
        "updatedStockQuantity": 10,
        "availabilityStartDate": "2026-12-31",
        "availabilityEndDate": "2026-01-01"
    }))