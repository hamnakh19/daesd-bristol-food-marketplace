# Sprint 2 – Form Testing Evidence

## 1. Overview

This document records testing carried out on the Product Listing Form and Inventory Update Form developed for Sprint 2 of the Bristol Regional Food Network Digital Marketplace project.

Testing focused on form validation, required fields, price and stock constraints, conditional fields, date inputs and optional fields. Screenshots of the tests are stored in the `Testing/Screenshots/` directory.

---

## 2. Product Listing Form Testing

Testing was carried out on the Product Listing Form to verify product input validation, required fields and conditional organic certification behaviour.

| Test ID | Test Description | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| PROD-01 | Submit a valid product listing | Valid product information should be accepted. | The form accepted the submission and reached the product validation service task. | PASS |
| PROD-02 | Submit without Product Name | Product Name should be required. | The form displayed a required-field validation message. | PASS |
| PROD-03a | Enter a price of 0 | Invalid price values should be rejected. | The form rejected the zero price. | PASS |
| PROD-03b | Enter a negative price | Negative prices should be rejected. | The form rejected the negative price. | PASS |
| PROD-04 | Enter negative stock | Negative stock quantities should be rejected. | The form rejected the negative stock quantity. | PASS |
| PROD-05 | Toggle the organic certification option | The certification field should appear when organic is selected and be hidden when it is not selected. | The certification field visibility changed according to the organic option. | PASS |
| PROD-06 | Enter an organic certification number | The certification number field should allow certification information to be entered. | A certification number was entered into the conditional field. | PASS |
| PROD-07 | Enter an availability end date earlier than the start date | Invalid date ordering should be identified or prevented. | The date inputs were tested; full date-order validation was not confirmed. | NEEDS REVIEW |

---

## 3. Inventory Update Form Testing

Testing was carried out on the Inventory Update Form to verify required fields, stock validation, date inputs and optional fields.

| Test ID | Test Description | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| INV-01 | Submit a valid inventory update | Valid inventory information should be accepted. | A valid inventory submission was accepted. | PASS |
| INV-02 | Submit an inventory update with stock quantity of 0 | Zero stock should be accepted as a valid stock quantity. | The form accepted a stock quantity of 0. | PASS |
| INV-03 | Enter negative stock (-5) | Negative stock quantities should be rejected. | The form displayed a minimum value validation message and rejected the negative quantity. | PASS |
| INV-04 | Submit without Product Name | Product Name should be required. | The form displayed a required-field message and prevented submission. | PASS |
| INV-05 | Enter decimal stock (2.5) | Stock quantity should be restricted to whole numbers. | The form rejected the decimal stock quantity and displayed a validation warning. | PASS |
| INV-06 | Enter an end date earlier than the start date | The end date should not precede the start date. | The form accepted the dates without displaying a date-order validation warning. | FAIL |
| INV-07 | Enter a future harvest date | The harvest date should be validated according to the relevant business rules. | A future harvest date was accepted without a validation warning. | NEEDS REVIEW |
| INV-08 | Leave Additional Notes blank | Additional Notes should be optional. | The form accepted the submission with Additional Notes left blank. The variable was recorded as an empty string. | PASS |
| INV-09 | Leave Harvest Date blank | Harvest Date should be optional. | The form accepted the submission with Harvest Date left blank. The variable was recorded as null. | PASS |

---

## 4. Test Results Summary

### Product Listing Form

Testing demonstrated that the Product Listing Form supports required-field validation, price and stock validation, and conditional organic certification field behaviour.

Testing also identified areas where further confirmation of date validation and certification verification behaviour may be required.

### Inventory Update Form

The Inventory Update Form demonstrated successful validation for required Product Name, negative stock quantities and decimal stock quantities. The optional Additional Notes and Harvest Date fields were also tested successfully.

The date-order test demonstrated that an end date earlier than the start date was accepted without a validation warning. A future harvest date was also accepted, requiring further clarification regarding the relevant business rules.

---

## 5. Conclusion

Testing provided evidence of the input validation and functionality implemented within both forms during Sprint 2.

The Product Listing Form was tested for required fields, price and stock constraints, and conditional organic certification behaviour. The Inventory Update Form was tested for required fields, stock quantity constraints, date inputs and optional fields.

Testing also identified potential areas for further improvement, particularly availability date validation. The recorded results and screenshots provide evidence of the form-level testing carried out during Sprint 2.

## 1. Overview

This document records the testing carried out on the Inventory and Seasonal Availability Management form developed for Sprint 2 of the Bristol Regional Food Network Digital Marketplace project.

Testing focused on form validation, required fields, stock quantity constraints, date inputs and optional fields. Screenshots of the tests are stored in the `Testing/Screenshots/` directory.

---

## 2. Inventory Form Testing

| Test ID | Test Description | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| INV-02 | Submit an inventory update with stock quantity of 0 | Zero stock should be accepted as a valid stock quantity. | The form accepted a stock quantity of 0. | PASS |
| INV-03 | Enter negative stock (-5) | Negative stock quantities should be rejected. | The form displayed a minimum value validation message and rejected the negative quantity. | PASS |
| INV-04 | Submit without Product Name | Product Name should be required. | The form displayed a "Field is required" message and prevented submission. | PASS |
| INV-05 | Enter decimal stock (2.5) | Stock quantity should be restricted to whole numbers. | The form rejected the decimal stock quantity and displayed a validation warning. | PASS |
| INV-06 | Enter an end date earlier than the start date | The end date should not precede the start date. | The form accepted the dates without displaying a date-order validation warning. | FAIL |
| INV-07 | Enter a future harvest date | The harvest date should be validated according to the relevant business rules. | A future harvest date was accepted without a validation warning. | NEEDS REVIEW |
| INV-08 | Leave Additional Notes blank | Additional Notes should be optional. | The form accepted the submission with Additional Notes left blank. The variable was recorded as an empty string. | PASS |
| INV-09 | Leave Harvest Date blank | Harvest Date should be optional. | The form accepted the submission with Harvest Date left blank. The variable was recorded as null. | PASS |

---

## 3. Test Results Summary

The Inventory Form demonstrated successful validation for required Product Name, negative stock quantities and decimal stock quantities. The optional Additional Notes and Harvest Date fields were also tested successfully.

The date-order test demonstrated that an end date earlier than the start date was accepted without a validation warning.

A future harvest date was also accepted. Further clarification may be required regarding whether future harvest dates should be permitted under the business rules.

---

## 4. Conclusion

Testing demonstrated that the Inventory Form supports several key validation and input requirements, including required fields, stock quantity validation and optional fields.

Testing also identified a potential issue with availability date ordering, as the form accepted an end date earlier than the start date without displaying a validation warning.

The completed tests provide evidence of the form's validation behaviour and functionality implemented during Sprint 2.