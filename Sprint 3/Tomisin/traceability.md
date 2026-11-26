# Sprint 3 – Model Consistency and Requirements Traceability

**Project:** Bristol Regional Food Network  
**Group:** 31  
**Use Case:** Producer Product Listing and Inventory Management  
**Author:** Tomisin  
**Date:** 25 November 2026  
**Status:** In Progress

## 1. Introduction

The purpose of this document is to establish traceability between the stakeholder requirements, socio-technical models, strategic BPMN, operational BPMN and Camunda implementation.

This review aims to ensure that the two selected functionalities satisfy the original business requirements and remain consistent throughout the development process.

The two functionalities are:

- Product Listing and Validation.
- Inventory and Seasonal Availability Management.

## 2. Reviewed 

The following artefacts have been reviewed:

- Use Case 1 requirements.
- Strategic Dependency (SD) model.
- Strategic Rationale (SR) model.
- Strategic BPMN model.

The revised operational BPMN diagrams and final Camunda implementation are awaiting review.

## 3. Requirements Traceability Matrix

| ID | Requirement | i* SR Element | Strategic BPMN | Operational BPMN | Implementation |
|---|---|---|---|---|---|
| REQ-01 | Submit product information | Provide Product Information | Submit Product Information | Pending | Pending |
| REQ-02 | Validate product information | Validate Product Information | Product Management and Inventory Control | Pending | Pending |
| REQ-03 | Request correction of invalid information | Partial coverage through validation | Product Management and Inventory Control | Pending | Pending |
| REQ-04 | Verify organic certification where applicable | Check Organic Certification If Applicable | Verify Organic Certification | Pending | Pending |
| REQ-05 | Publish successfully validated products | Publish Approved Listing | Product Management and Inventory Control | Pending | Pending |
| REQ-06 | Update stock and seasonal availability | Update Inventory and Seasonal Availability | Update Stock and Seasonal Availability | Pending | Pending |
| REQ-07 | Validate inventory updates | Validate Inventory Update | Product Management and Inventory Control | Pending | Pending |
| REQ-08 | Mark zero-stock products as unavailable | Determine Product Availability | Product Management and Inventory Control | Pending | Pending |
| REQ-09 | Restore availability when eligible stock is replenished | Determine Product Availability | Product Management and Inventory Control | Pending | Pending |
| REQ-10 | Respect seasonal availability restrictions | Determine Product Availability | Product Management and Inventory Control | Pending | Pending |
| REQ-11 | Provide accurate product availability information | Accurate Product Availability Information | Customer Browsing and Ordering – partial coverage | Pending | Pending |
| REQ-12 | Handle verification service unavailability | Not explicitly represented | Not explicitly represented | Pending | Pending |

Requirement identifiers have been assigned for internal traceability purposes. REQ-07 is a supporting design requirement identified in the SR model.

## 4. Model Consistency Review

### 4.1 Actor Consistency

The Producer, Marketplace System, Customer and Organic Certification Verification Service are represented in both the i* models and strategic BPMN.

The strategic BPMN additionally includes the External Payment Service, which supports the wider marketplace but is outside the primary scope of Use Case 1.

### 4.2 Functionality Consistency

Both selected functionalities align with the Product Management and Inventory Control subprocess identified in the strategic BPMN.

The interaction with the Organic Certification Verification Service is also represented through verification request and response message flows.

### 4.3 Identified Areas for Review

| ID | Observation | Recommended Action | Status |
|---|---|---|---|
| OBS-01 | Customer availability information is not explicitly exchanged in the strategic BPMN. | Review how product availability information is communicated to customers. | Open |
| OBS-02 | Two external quality dependencies in the SD model are not explicitly retained in the SR model. | Review consistency between the SD and SR representations. | Open |
| OBS-03 | The direction of the Valid Product Listing Published dependency requires verification. | Check dependency direction in the editable piStar model. | Open |
| OBS-04 | Certification service failure handling is not explicitly represented in the high-level models. | Verify exception handling in the operational BPMN and Camunda implementation. | Pending |
| OBS-05 | Interactions between marketplace subprocesses are not explicitly represented. | Review how product management supports customer browsing and other relevant processes. | Open |

These observations require further review and do not necessarily indicate implementation defects.

## 5. Outstanding Work

- [x] Review Strategic Dependency model.
- [x] Review Strategic Rationale model.
- [x] Identify requirements for traceability.
- [x] Review strategic BPMN.
- [ ] Review revised Product Listing and Validation operational BPMN.
- [ ] Review revised Inventory and Seasonal Availability operational BPMN.
- [ ] Review Camunda Forms and process variables.
- [ ] Review service tasks and automated business logic.
- [ ] Verify alternative and exception flows.
- [ ] Map requirements to test cases and actual results.
- [ ] Complete end-to-end traceability.
- [ ] Evaluate readiness for Task 2 integration.

## 6. Current Dependencies

The operational BPMN diagrams are currently being revised by Khadija following previous assessment feedback.

Once the updated diagrams are available, the traceability review will continue by comparing the operational workflows with the stakeholder requirements and executable Camunda processes.

## 7. Preliminary Conclusion

The initial review demonstrates conceptual alignment between the stakeholder requirements identified in the i* models and the major business processes represented in the strategic BPMN.

Several areas requiring further review have been identified. Full end-to-end consistency cannot yet be confirmed until the revised operational BPMN diagrams, Camunda implementation and testing evidence have been reviewed.

This document will be updated iteratively throughout Sprint 3.

## 8. Reference 

- Task 1 – Use Cases, Use Case 1.
- UFCFTR-30-3 – Task 1 Assessment Brief.
- DAESD Sprint 2 SD Model.
- DAESD Sprint 2 SR Model.
- Strategic BPMN – Sprint 1.


