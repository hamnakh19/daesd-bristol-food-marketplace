# Sprint 2 – Inventory Form Testing Evidence

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