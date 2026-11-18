# Sprint 2 – Testing Evidence

## 1. Inventory Update Tests

| Test ID | Test scenario | Test input | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| INV-01 | Valid inventory update | Organic Apples, stock 10, valid availability dates | Form submits and inventory update is processed | Form submitted successfully. Process reached Validate Inventory Update but stopped because no service-task worker was available. | Blocked |
| INV-02 | Zero stock | Stock quantity 0 | Product should become unavailable | Not tested yet | Not tested |
| INV-03 | Negative stock | Stock quantity -5 | Invalid quantity should be rejected or sent for correction | Not tested yet | Not tested |
| INV-04 | Missing required information | Leave a required field empty | Form should show a validation message | Not tested yet | Not tested |
| INV-05 | Outside seasonal availability | Dates outside the current availability period | Product should follow the unavailable route | Not tested yet | Not tested |

## 2. Product Listing Tests

| Test ID | Test scenario | Expected result | Actual result | Status |
|---|---|---|---|---|
| PROD-01 | Submit valid product information | Form submits successfully | Not recorded yet | Not tested |
| PROD-02 | Leave required fields empty | Validation messages appear | Not tested yet | Not tested |
| PROD-03 | Select organic certification | Certification number field appears when applicable | Not tested yet | Not tested |

## 3. Evidence

Screenshots are stored in the relevant Sprint 2 folders.

## 4. Issues Identified

- Inventory Update process reached the Validate Inventory Update service task but could not continue because a job worker was not available.
- Service-task execution requires a worker implementation before the full process can be tested.