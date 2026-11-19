# Traceability Between i*, Strategic BPMN and Operational BPMN


## 1. Overview

For Sprint 2, I worked on connecting our i* Strategic Dependency (SD) and Strategic Rationale (SR) models with the Strategic BPMN from Sprint 1 and the two Operational BPMN models developed in Sprint 2.

The i* SD model identifies the main actors and what they depend on each other for. The SR model explains the actors' goals and the tasks they need to carry out to achieve them.

The Strategic BPMN shows the main business processes within the Bristol Regional Food Network, while the Operational BPMNs show the detailed steps involved in Product Listing and Validation, and Inventory and Seasonal Availability Management.

The aim of this traceability analysis is to show how the stakeholder requirements are represented across the different models.

## 2. Traceability Table

| i* SD Dependency | i* SR Model | Strategic BPMN | Operational BPMN |
|---|---|---|---|
| **Valid Product Listing Published** (Goal) | Valid Product Listing Published, Validate Product Information and Publish Approved Listing | Product Management and Inventory Control | BPMN 1: Validate Product Details → Publish Product |
| **Product Information** (Resource) | Provide Product Information and Product Details | Product Management and Inventory Control | BPMN 1: Enter Product Information → Validate Product Details |
| **Organic Certification Verification Result** (Resource) | Verify Organic Certification and Organic Certification Status Verified | Product Management and Inventory Control | BPMN 1: Organic Certification Claimed? → Request Organic Certification Verification → Certification Result? |
| **Updated Inventory and Seasonal Information** (Resource) | Update Inventory and Seasonal Availability, and Stock and Seasonal Availability Details | Product Management and Inventory Control | BPMN 2: Update Stock and Seasonal Information → Validate Inventory Update → Save Inventory Update |
| **Product Availability Correctly Updated** (Goal) | Product Availability Correctly Updated, Validate Inventory Update and Determine Product Availability | Product Management and Inventory Control | BPMN 2: Stock Greater Than Zero? → Within Seasonal Period? → Set Product Available/Unavailable |
| **Product Availability Information** (Resource) | Browse Available Products and Available Products Identified | Product Management and Inventory Control; Customer Browsing and Ordering | BPMN 2: Set Product Available/Unavailable, providing the availability status needed by the customer-facing marketplace |

## 3. Connection to Operational BPMN 1

The first Operational BPMN focuses on Product Listing and Validation.

The Producer depends on the Marketplace System to publish valid product listings. This requirement is identified in the i* models and represented in the Strategic BPMN under Product Management and Inventory Control.

In the Operational BPMN, I developed the detailed steps for entering product information, validating the details and requesting corrections when information is invalid.

I also included the organic certification verification process. If certification is valid, the product can be published. If it is invalid, the information must be corrected. If the verification service is unavailable, the listing is kept pending verification.

This shows how the stakeholder goals and dependencies are represented through tasks, gateways and alternative paths.

## 4. Connection to Operational BPMN 2

The second Operational BPMN focuses on Inventory and Seasonal Availability Management.

The Producer depends on the Marketplace to maintain accurate product availability. The i* models identify the need for updated inventory information and correctly updated product availability.

In the Operational BPMN, I included the steps for updating stock quantities and seasonal information, validating the updates and correcting invalid details.

I also added decision gateways to check whether stock is greater than zero and whether the product is within its seasonal availability period.

If both conditions are satisfied, the product can be made available. Otherwise, it becomes unavailable.

This connects the stakeholder requirements to the detailed inventory management process.

## 5. Relationship Between the Models

All the models focus on the same two functionalities but represent them at different levels.

The i* SD model shows the dependencies between the Producer, Marketplace System, Customer and Organic Certification Verification Service.

The i* SR model shows the actors' goals and how they intend to achieve them.

The Strategic BPMN represents Product Management and Inventory Control as one of the marketplace's major business processes.

The two Operational BPMNs develop this business process into detailed workflows with user tasks, service tasks, exclusive gateways, correction loops and different outcomes.

The Operational BPMNs provide a foundation for the Camunda automation work, including Forms, service-task implementation, process variables and business logic.

## 6. Remaining Implementation Considerations

The second Operational BPMN updates product availability, but the customer-facing display of that information has not been modelled as a separate task.

The first Operational BPMN handles unavailable certification by setting a pending status, but an automatic retry mechanism still needs to be implemented.

The inventory process also needs a scheduled availability check so that seasonal changes can be applied without requiring the producer to submit another update.

These are areas for further implementation and testing.

## 7. Conclusion

The traceability analysis shows how the requirements identified in the i* models connect to the Strategic BPMN and the two Operational BPMNs.

The first operational model supports the goal of publishing valid product listings, while the second supports accurate inventory and seasonal availability management.

By connecting these models, the group can demonstrate how stakeholder requirements have been translated into detailed business processes that can be developed further in Camunda.