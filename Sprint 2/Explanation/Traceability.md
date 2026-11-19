# Traceability Between i\*, Strategic BPMN and Operational BPMN

## 1. Overview

For Sprint 2, my responsibility was to create two detailed Operational BPMN models and show how they connect to the stakeholder requirements identified in our group's earlier models.

Another group member developed the i\* Strategic Dependency (SD) and Strategic Rationale (SR) models. I reviewed these models to understand the relationships between stakeholders, their goals and their responsibilities.

I then compared these requirements with the Strategic BPMN I created during Sprint 1 and the two Operational BPMNs I developed for Sprint 2.

The purpose of this traceability analysis is to show how the requirements identified in the i\* models are represented in our business processes.

## 2. Traceability Table

| i\* Dependency                                 | Strategic BPMN                                                           | Operational BPMN                                                                                                 |
| ---------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Valid Product Listing Published**            | Product Management and Inventory Control                                 | BPMN 1: Validate Product Details → Publish Product                                                               |
| **Product Information**                        | Product Management and Inventory Control                                 | BPMN 1: Enter Product Information → Validate Product Details                                                     |
| **Organic Certification Verification Result**  | Product Management and Inventory Control                                 | BPMN 1: Request Organic Certification Verification → Certification Result?                                       |
| **Updated Inventory and Seasonal Information** | Product Management and Inventory Control                                 | BPMN 2: Update Stock and Seasonal Information → Validate Inventory Update → Save Inventory Update                |
| **Product Availability Correctly Updated**     | Product Management and Inventory Control                                 | BPMN 2: Stock Greater Than Zero? → Within Seasonal Period? → Set Product Available/Unavailable                   |
| **Product Availability Information**           | Product Management and Inventory Control; Customer Browsing and Ordering | BPMN 2: Set Product Available/Unavailable, which determines the availability information used by the marketplace |

## 3. Connection to the i\* Models

The i\* SD model shows how different actors depend on each other. For example, the Producer depends on the Marketplace System to publish valid product listings, while the Marketplace depends on the Producer to provide product information.

The i\* SR model goes into more detail by showing the goals and tasks involved in achieving these requirements.

I used the models developed by another group member as references when checking whether my two Operational BPMNs covered the main requirements of Use Case 1.

## 4. Operational BPMN 1 — Product Listing and Validation

The first Operational BPMN focuses on how producers submit products to the marketplace.

In the i\* models, one of the main goals is to have a valid product listing published. This is represented in the Strategic BPMN under Product Management and Inventory Control.

In my Operational BPMN, I developed the detailed steps showing how the producer enters product information and how the marketplace validates it.

I added gateways to check whether the information is valid. If it is incorrect, the producer is asked to correct it.

I also included organic certification verification. If the certificate is valid, the product can be published. If it is invalid, the producer must correct the information. If the verification service is unavailable, the listing is kept pending.

This connects the stakeholder requirements from the i\* models to the detailed product listing process.

## 5. Operational BPMN 2 — Inventory and Seasonal Availability Management

The second Operational BPMN focuses on how producers update their stock quantities and seasonal information.

The i\* models identify the need for accurate inventory information and correctly updated product availability.

In my Operational BPMN, I included a process where producers update their stock information and the marketplace validates it.

I added decision gateways to check whether stock is greater than zero and whether the product is within its seasonal period.

If both conditions are met, the product becomes available. If there is no stock or the product is out of season, it becomes unavailable.

This shows how the requirements for accurate product availability are represented in the detailed inventory management process.

## 6. How the Models Connect

The models represent the same business requirements at different levels.

The *i SD model*\* identifies the dependencies between stakeholders.

The *i SR model*\* explains the stakeholders' goals and how they can achieve them.

The **Strategic BPMN** shows the main business processes of the marketplace.

The **Operational BPMNs** show the detailed tasks, decisions and alternative paths needed to carry out the two selected functionalities.

For example, the Producer's goal of having a valid product listing published is identified in the i\* models. This connects to Product Management and Inventory Control in the Strategic BPMN. Operational BPMN 1 then shows how the product is submitted, checked and published.

The inventory process follows the same approach by connecting the need for accurate product availability to the stock and seasonal checks in Operational BPMN 2.

The second BPMN models how availability status is updated, while displaying that information to customers will require integration with the marketplace's customer-facing functionality.

## 7. Conclusion

This traceability analysis shows how the stakeholder requirements identified in the i\* models developed by another group member connect to our Strategic BPMN and the two Operational BPMNs I created.

The first Operational BPMN supports Product Listing and Validation, while the second supports Inventory and Seasonal Availability Management.

By linking the models together, I have shown how the stakeholder requirements are represented through detailed business processes.

These operational models also provide a foundation for the group's Camunda automation work, including user forms, service tasks, process variables and business logic.
