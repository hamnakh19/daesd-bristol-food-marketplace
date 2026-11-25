# Sprint 3 – Legal, Ethical, Social and Professional (LESP) Evaluation

**Project:** Bristol Regional Food Network  
**Module:** Distributed and Enterprise Software Development (UFCFTR-30-3)  
**Group:** 31  
**Use Case:** Producer Product Listing and Inventory Management  
**Author:** Tomisin  
**Date:** 25 November 2026  
**Status:** Preliminary evaluation completed – implementation verification pending

## 1. Introduction

This document evaluates the Legal, Ethical, Social and Professional (LESP) considerations associated with the design, development and implementation of the Bristol Regional Food Network marketplace.

The evaluation focuses on two selected functionalities:

- Product Listing and Validation.
- Inventory and Seasonal Availability Management.

The purpose is to identify potential risks, assess their consequences, recommend appropriate mitigation measures and establish traceability between LESP considerations, business requirements and technical implementation.

The evaluation also considers the limitations of automated processes and identifies areas requiring further testing and verification before the system can be considered ready for wider deployment.

## 2. Evaluation Objectives

The objectives of this evaluation are to:

- Identify relevant legal and regulatory responsibilities.
- Promote fair, transparent and responsible automated decisions.
- Evaluate the potential impact on producers, customers and local communities.
- Encourage professional software development practices.
- Identify, assess and prioritise risks.
- Recommend appropriate mitigation measures.
- Connect LESP findings to business requirements and technical implementation.
- Establish verification methods for future testing.
- Support the maintainability and integration readiness of the system for Task 2.

## 3. Legal Considerations

### 3.1 L1 – Data Protection and Privacy

Relevant legislation includes:

- UK General Data Protection Regulation (UK GDPR).
- Data Protection Act 2018, as amended.

The Information Commissioner's Office (ICO, n.d.) identifies principles governing the lawful, secure and accountable processing of personal information.

The marketplace may process personal information associated with registered producers, including names, contact details, account identifiers and farm addresses where these identify individuals.

**Potential risks:**

- Unauthorised access to personal information.
- Unauthorised modification of producer listings.
- Collection of unnecessary personal information.
- Disclosure of confidential information.

**Recommended mitigation measures:**

- Authenticate registered producers.
- Apply ownership-based authorisation.
- Collect only necessary personal information.
- Protect stored and transmitted information.
- Establish appropriate retention periods and lawful processing arrangements.
- Avoid exposing confidential information through process logs.

**Critical evaluation:**

Authentication establishes a user's identity but does not independently prevent unauthorised actions. Ownership-based authorisation must also be enforced by the underlying services.

The use of access controls does not demonstrate complete GDPR compliance, as additional organisational and data governance responsibilities remain necessary.

**Related requirements:** REQ-01, REQ-06.

### 3.2 L2 – Food Safety and Allergen Information

Relevant legislation includes:

- Food Safety Act 1990.
- Food Information Regulations 2014.
- Regulation (EU) No. 1169/2011 on food information to consumers, as applicable in Great Britain.

The Food Standards Agency (FSA, n.d.) explains that mandatory allergen information for food sold through distance selling must be made available before purchase and at delivery.

The marketplace should therefore support the collection and communication of accurate allergen information where applicable.

**Potential risks:**

- Publication of incomplete product information.
- Customers purchasing products containing undeclared allergens.
- Health consequences and loss of customer confidence.
- Potential regulatory non-compliance.

**Recommended mitigation measures:**

- Require applicable allergen information.
- Validate mandatory fields through Camunda Forms and underlying business logic.
- Prevent publication of incomplete listings.
- Provide correction and resubmission opportunities.
- Ensure relevant information can be communicated to downstream ordering and delivery processes.

**Critical evaluation:**

Mandatory fields and automated validation can reduce the likelihood of missing information. However, they cannot independently establish whether producer-supplied information is factually accurate.

Producer accountability and appropriate verification procedures remain necessary. Compliance at delivery must also be considered during wider system integration.

**Related requirements:** REQ-02, REQ-03, REQ-05.

### 3.3 L3 – Organic Certification

The Department for Environment, Food & Rural Affairs (Defra, 2025) provides guidance on the certification, labelling and advertising requirements applicable to organic food.

Producers making organic claims must satisfy the applicable certification and production requirements.

The proposed marketplace incorporates an Organic Certification Verification Service to support this responsibility.

**Potential risks:**

- Publication of false organic claims.
- Acceptance of invalid certification.
- Incorrect approval following external service failure.
- Misleading customers and damaging marketplace credibility.

**Recommended mitigation measures:**

- Verify certification when a producer makes an organic claim.
- Prevent publication of unverified organic claims.
- Distinguish invalid certification from external service failure.
- Notify producers when further information or action is required.
- Provide an appropriate mechanism for resolving unsuccessful verification.

**Critical evaluation:**

External certification verification can improve the reliability of organic claims. However, the marketplace depends on the accuracy and availability of the verification service.

A service failure should not automatically result in approval or permanent rejection. The affected listing should be held for resolution.

If the verification service is simulated for the assessment, successful execution demonstrates workflow behaviour rather than genuine regulatory certification.

**Related requirements:** REQ-04, REQ-05, REQ-12.

## 4. Ethical Considerations

### 4.1 E1 – Honesty and Transparency

Customers should receive accurate information about products, prices, allergens, organic claims and availability.

**Risk:** Customers make purchasing decisions based on misleading or outdated information.

**Mitigation:** Validate product information, maintain accurate inventory records and communicate availability status clearly.

**Critical evaluation:** Automated validation improves consistency but cannot guarantee that all information supplied by producers is truthful.

**Related requirements:** REQ-06, REQ-07, REQ-08, REQ-11.

### 4.2 E2 – Fair Treatment of Producers

All producers should be subject to consistent validation and approval criteria regardless of their business size or reputation.

**Risk:** Preferential treatment disadvantages smaller or less established producers.

**Mitigation:** Apply consistent business rules and provide equivalent correction opportunities for comparable submissions.

**Critical evaluation:** Identical validation rules promote fairness, but differences in technical ability may still disadvantage some producers. Accessible forms and meaningful guidance are therefore also necessary.

**Related requirements:** REQ-02, REQ-03, REQ-04, REQ-05.

### 4.3 E3 – Accountability and Responsibility

The marketplace should maintain appropriate records of important product listing and inventory decisions.

**Risk:** Incorrect modifications cannot be investigated or attributed to responsible parties.

**Mitigation:** Maintain appropriate audit records, timestamps, authorised user identifiers and process execution histories.

**Critical evaluation:** Audit records support accountability but may contain personal information. Access restrictions and appropriate retention policies must therefore be considered.

**Related requirements:** REQ-06, REQ-07, REQ-11.

### 4.4 E4 – Responsible Automated Decision-Making

Automated validation and certification decisions should not unnecessarily disadvantage producers.

**Risk:** Producers lose legitimate business opportunities because of unclear validation failures or technical errors.

**Mitigation:** Provide understandable error messages, correction opportunities and appropriate escalation mechanisms.

**Critical evaluation:** Automation improves efficiency and consistency, but exceptional cases may require human intervention. A technical failure should not be treated as evidence of producer misconduct.

**Related requirements:** REQ-03, REQ-12.

## 5. Social Considerations

### 5.1 S1 – Accessibility and Digital Inclusion

Producers may have different levels of technical knowledge and digital accessibility requirements.

**Risk:** Complicated or inaccessible forms exclude less technically experienced producers.

**Mitigation:**

- Provide clear field labels and instructions.
- Use understandable validation messages.
- Support keyboard navigation.
- Avoid unnecessary technical terminology.
- Evaluate form accessibility and usability.

**Critical evaluation:** Simplifying forms can improve accessibility, but necessary validation requirements must remain in place to protect customers and maintain information quality.

**Related requirements:** REQ-01, REQ-03, REQ-06.

### 5.2 S2 – Supporting the Local Economy

The marketplace can provide local producers with opportunities to promote and sell their products to a wider customer base.

**Potential benefits:**

- Increased visibility for independent producers.
- Greater opportunities for local businesses.
- Stronger relationships between producers and customers.

**Risk:** Complex listing procedures discourage smaller producers from participating.

**Mitigation:** Provide straightforward submission processes, accessible forms and consistent approval requirements.

**Critical evaluation:** The marketplace has the potential to support local economic activity. However, actual economic improvements cannot be established without evidence of producer participation, sales and customer engagement.

**Related requirements:** REQ-01, REQ-03, REQ-05.

### 5.3 S3 – Environmental Sustainability and Food Waste

Accurate inventory and seasonal availability management can support responsible consumption and potentially reduce unnecessary food waste.

The proposed availability rules include:

- Products with zero stock should be unavailable.
- Replenished products should become available only when eligible.
- Products outside their seasonal availability period should remain unavailable.
- Availability should reflect accurate inventory information.

**Risk:** Incorrect availability information contributes to inefficient stock management and potentially unnecessary waste.

**Mitigation:** Validate inventory updates, enforce seasonal restrictions and maintain accurate availability records.

**Critical evaluation:** Accurate inventory management may support sustainability, but the system does not independently guarantee a reduction in food waste. Actual environmental benefits require further measurement.

**Related requirements:** REQ-06, REQ-07, REQ-08, REQ-09, REQ-10.

### 5.4 S4 – Customer Trust and Public Wellbeing

Customers depend on reliable information when purchasing food products.

**Risk:** Incorrect allergen, origin, certification or availability information negatively affects customer wellbeing and confidence.

**Mitigation:** Validate applicable product information, verify organic claims and maintain accurate availability information.

**Critical evaluation:** Digital information controls support customer confidence, but physical food safety and the accuracy of producer declarations remain dependent on wider organisational responsibilities.

**Related requirements:** REQ-02, REQ-04, REQ-05, REQ-11.

## 6. Professional Considerations

The BCS Code of Conduct provides a relevant professional framework covering public interest, professional competence, responsibilities to relevant authorities and responsibilities to the profession (BCS, n.d.).

### 6.1 P1 – Software Quality and Testing

The development team should verify that the implementation satisfies functional requirements under normal and exceptional conditions.

**Risk:** Undetected defects cause incorrect product publication or availability decisions.

**Mitigation:**

- Functional testing.
- Boundary-value testing.
- Invalid-input testing.
- Exception testing.
- End-to-end process testing.
- Regression testing after corrections.

**Critical evaluation:** Successful tests provide evidence of expected behaviour for the scenarios examined but cannot establish that the software is completely free from defects.

**Related requirements:** REQ-01–REQ-12.

### 6.2 P2 – Security and Secure Development

The marketplace should protect producer accounts, product information and underlying services against unauthorised actions.

**Risk:** An unauthorised user accesses confidential information or modifies another producer's products.

**Mitigation:**

- Authentication and authorisation.
- Ownership-based access control.
- Server-side input validation.
- Secure credential management.
- Appropriate error handling.

**Critical evaluation:** Camunda Form validation alone is insufficient because requests may reach underlying services through other interfaces. Important security and validation rules should also be enforced at the service level.

**Related requirements:** REQ-01, REQ-02, REQ-06, REQ-07.

### 6.3 P3 – Documentation and Maintainability

The implementation should be understandable, maintainable and suitable for further development in Task 2.

**Risk:** Inconsistent models, unclear code and undocumented dependencies create integration difficulties.

**Mitigation:**

- Maintain requirements traceability.
- Use meaningful process and variable names.
- Document service interfaces and dependencies.
- Provide accurate README and setup instructions.
- Maintain meaningful GitHub commit histories.
- Review consistency between modelling artefacts and executable processes.

**Critical evaluation:** Documentation improves maintainability only when it accurately reflects the current implementation. It must therefore be updated whenever significant changes occur.

**Related requirements:** REQ-01–REQ-12.

### 6.4 P4 – Professional Integrity and Teamwork

Team members should communicate progress honestly, acknowledge individual contributions and report limitations accurately.

**Risk:** Misrepresentation of progress, poor coordination and unreliable assessment evidence.

**Mitigation:**

- Participate in sprint stand-ups.
- Communicate blockers and dependencies.
- Maintain individual contribution records.
- Conduct appropriate peer reviews.
- Report actual testing results.
- Disclose AI assistance in accordance with assessment requirements.

**Critical evaluation:** Version control provides evidence of individual contributions, but meaningful collaboration also requires communication, shared understanding and coordination of responsibilities.

### 6.5 P5 – Reliability and Exception Handling

The marketplace depends on automated services, including the Organic Certification Verification Service.

**Risk:** External service failures cause incorrect approvals, interrupted workflows or lost information.

**Mitigation:**

- Handle unsuccessful verification and technical errors separately.
- Apply controlled retry mechanisms where appropriate.
- Maintain clear process states.
- Provide meaningful notifications.
- Monitor process execution.

**Critical evaluation:** Retry mechanisms may reduce temporary service interruptions, but unlimited retries can introduce delays and resource consumption. Appropriate retry limits and resolution mechanisms should be considered.

**Related requirements:** REQ-04, REQ-05, REQ-12.

## 7. Risk Assessment Methodology

A qualitative risk assessment method is proposed to prioritise identified risks according to their likelihood and impact.

**Risk score = Likelihood × Impact**

Both factors are scored between 1 and 5.

| Score | Likelihood | Impact |
|---|---|---|
| 1 | Rare | Negligible |
| 2 | Unlikely | Minor |
| 3 | Possible | Moderate |
| 4 | Likely | Major |
| 5 | Almost certain | Severe |

Risk classification:

| Risk score | Classification |
|---|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–16 | High |
| 17–25 | Critical |

Inherent risk represents the estimated risk before protective controls are applied. Residual risk represents the risk remaining after those controls are applied.

The scores in this evaluation are preliminary qualitative estimates rather than measured incident statistics. They should be reviewed as implementation and testing evidence becomes available.

## 8. LESP Risk Register

| ID | Risk | Category | Likelihood | Impact | Score | Classification |
|---|---|---|---:|---:|---:|---|
| R01 | Missing or incorrect allergen information | L, E, S | 4 | 5 | 20 | Critical |
| R02 | Unauthorised access or product modification | L, P | 3 | 5 | 15 | High |
| R03 | False organic certification claims | L, E | 3 | 5 | 15 | High |
| R04 | Incorrect stock or seasonal availability | E, S, P | 4 | 4 | 16 | High |
| R05 | Certification service failure | L, E, P | 3 | 4 | 12 | High |
| R06 | Unfair automated decisions | E, S | 3 | 3 | 9 | Medium |
| R07 | Inaccessible or complicated forms | E, S | 4 | 3 | 12 | High |
| R08 | Insufficient testing | P | 4 | 4 | 16 | High |
| R09 | Poor documentation and integration | P | 3 | 4 | 12 | High |
| R10 | Insufficient accountability and audit records | E, P | 3 | 3 | 9 | Medium |

### 8.1 Risk Prioritisation

The preliminary assessment identifies the following priorities:

1. Missing or incorrect allergen information.
2. Incorrect inventory and seasonal availability.
3. Insufficient software testing.
4. Unauthorised access and false organic claims.
5. Remaining reliability, accessibility, documentation and accountability risks.

Allergen information receives the highest priority because incorrect information may have severe consequences for customer health.

The numerical rankings are judgement-based and should not be interpreted as confirmed probabilities of failure.

## 9. Risk Mitigation and Verification

| Risk | Proposed mitigation | Verification method |
|---|---|---|
| R01 | Mandatory allergen information where applicable | Submit incomplete product information |
| R02 | Ownership-based authorisation | Attempt to modify another producer's product |
| R03 | Certification verification | Submit invalid organic certification |
| R04 | Stock and seasonal validation | Test zero stock, replenishment and expired seasons |
| R05 | Exception handling | Simulate certification service failure |
| R06 | Consistent validation and correction opportunities | Compare equivalent submissions |
| R07 | Accessible forms and clear feedback | Conduct usability and accessibility checks |
| R08 | Comprehensive software testing | Execute normal, boundary and exception tests |
| R09 | Traceability and interface documentation | Review models, README files and service interfaces |
| R10 | Appropriate audit records | Inspect process history and modification records |

All mitigation measures remain subject to implementation verification.

### 9.1 Residual Risk Example

Consider the risk of publishing incomplete allergen information.

**Inherent risk:**

- Likelihood: 4.
- Impact: 5.
- Risk score: 20 (Critical).

**Proposed controls:**

- Mandatory allergen information where applicable.
- Server-side validation.
- Correction before publication.

If these controls operate effectively, an illustrative residual risk estimate for missing allergen information could be:

- Likelihood: 1.
- Impact: 5.
- Risk score: 5 (Medium).

The impact remains severe because an allergic reaction may still have serious consequences.

Furthermore, incorrect but completed allergen declarations may pass automated validation. The broader risk of inaccurate allergen information therefore remains and requires separate evaluation.

This estimated reduction is illustrative and has not been established through actual testing.

## 10. Connection to System Design

### 10.1 Product Listing and Validation

The proposed implementation should support:

- Collection of mandatory product information.
- Validation of submitted product details.
- Conditional organic certification verification.
- Correction and resubmission opportunities.
- Appropriate handling of verification failures.
- Publication only after applicable validation checks succeed.

Proposed form and service validation:

| Field | Proposed validation | LESP relevance |
|---|---|---|
| Product name | Required and non-empty | Transparency |
| Description | Required information | Customer trust |
| Category | Valid category | Information quality |
| Price | Valid positive monetary value | Reliability |
| Quantity | Non-negative quantity using the appropriate unit | Inventory accuracy |
| Availability period | Valid date range | Sustainability |
| Farm origin | Required origin information | Transparency |
| Allergens | Required information where applicable | Customer safety |
| Organic certification | Evidence where applicable | Legal compliance |
| Harvest date | Valid date where applicable | Accuracy |
| Best-before date | Valid date where applicable | Food quality |

These validation rules are proposed design controls and require confirmation against the final implementation.

### 10.2 Inventory and Seasonal Availability Management

The proposed implementation should determine product availability using stock quantity, seasonal restrictions and existing listing eligibility.

| Scenario | Expected availability |
|---|---|
| Approved product with positive stock within season | Available |
| Product with zero stock | Unavailable |
| Eligible product replenished within season | Available |
| Product replenished outside season | Unavailable |
| Product not approved for publication | Unavailable |

These rules support accurate customer information and responsible inventory management.

The exact implementation conditions, including how seasonal expiry is detected, must be confirmed during the operational BPMN and Camunda review.

## 11. LESP Implementation Traceability Matrix

The requirement identifiers correspond to the preliminary requirements traceability document.

| Risk | Related requirements | Implementation control | Proposed verification |
|---|---|---|---|
| R01 | REQ-02, REQ-03 | Allergen validation | TC-01 |
| R02 | REQ-01, REQ-06 | Ownership authorisation | TC-02 |
| R03 | REQ-04, REQ-05 | Certification verification | TC-03 |
| R04 | REQ-06–REQ-11 | Inventory and availability logic | TC-04–TC-07 |
| R05 | REQ-12 | Service exception handling | TC-08 |
| R06 | REQ-02, REQ-03 | Consistent validation rules | TC-09 |
| R07 | REQ-01, REQ-03, REQ-06 | Accessible forms | TC-10 |
| R08 | REQ-01–REQ-12 | Comprehensive testing | Full test suite |
| R09 | REQ-01–REQ-12 | Documentation and interface consistency | Artefact review |
| R10 | REQ-06, REQ-11 | Appropriate audit records | TC-11 |

Supporting security, accessibility and audit controls may require additional requirements beyond the original use case.

The test identifiers are provisional and will be finalised during process testing and validation.

## 12. Evidence and Implementation Verification Plan

The following artefacts will be reviewed to establish whether proposed LESP controls are supported by the implementation.

| Artefact | Verification purpose | Status |
|---|---|---|
| Strategic Dependency model | Stakeholder responsibilities and dependencies | Initial review completed |
| Strategic Rationale model | Stakeholder goals and supporting tasks | Initial review completed |
| Strategic BPMN | Alignment with business processes | Initial review completed |
| Operational BPMN diagrams | Validation, decision logic and exception handling | Pending |
| Camunda Forms | Field validation, accessibility and feedback | Pending |
| Business logic and service code | Validation, security and availability rules | Pending |
| Camunda process execution | Actual workflow behaviour | Pending |
| Test results | Evidence of functional correctness | Pending |
| Process history and audit records | Accountability and traceability | Pending |
| Service interface documentation | Task 2 integration readiness | Pending |

Initial model reviews do not establish that the proposed LESP controls have been implemented.

Actual testing outcomes, screenshots and code references will be documented during process testing and validation.

## 13. Current Limitations and Outstanding Actions

The following limitations have been identified:

- Revised operational BPMN diagrams are awaiting review.
- Camunda Forms and executable business logic have not yet been verified as part of this evaluation.
- Proposed security, accessibility and audit controls may exceed the current prototype scope.
- Risk scores are preliminary qualitative estimates.
- No actual test results have been collected for this evaluation.
- Automated validation cannot guarantee the factual accuracy of producer declarations.
- A simulated certification service cannot establish genuine organic certification.
- Economic and environmental benefits have not been measured.
- Complete legal compliance cannot be established from the selected workflows alone.

Outstanding actions:

- [x] Identify legal considerations.
- [x] Identify ethical considerations.
- [x] Identify social considerations.
- [x] Identify professional considerations.
- [x] Establish a preliminary risk register.
- [x] Propose mitigation measures.
- [x] Map findings to requirements and proposed implementation controls.
- [ ] Review revised operational BPMN diagrams.
- [ ] Verify Camunda Forms and business logic.
- [ ] Finalise test cases.
- [ ] Execute relevant tests.
- [ ] Collect implementation evidence.
- [ ] Reassess residual risks based on available evidence.
- [ ] Update the final LESP evaluation.

## 14. Conclusion

This preliminary evaluation identified 16 Legal, Ethical, Social and Professional considerations and consolidated them into 10 principal risks associated with the Bristol Regional Food Network marketplace.

The highest-priority risks relate to allergen information, inventory accuracy and insufficient software testing.

Proposed mitigation measures include product information validation, organic certification verification, ownership-based authorisation, accessible forms, appropriate exception handling and comprehensive testing.

Although these measures can improve system reliability and responsible operation, limitations remain. Automated validation cannot independently guarantee factual information accuracy, external services may fail, and successful testing cannot establish the absence of all software defects.

The next stage is to verify the proposed controls against the operational BPMN diagrams, Camunda implementation and actual test results.



## 15. References

BCS Code of Conduct. (n.d.). https://www.bcs.org/membership-and-registrations/become-a-member/bcs-code-of-conduct/

Organic food: labelling and advertising rules. (2025, August 20). GOV.UK. https://www.gov.uk/guidance/organic-food-labelling-rules

Food Standards Agency. (2026, November 23). Allergen guidance for food businesses. GOV.UK. https://www.gov.uk/government/publications/allergen-guidance-for-food-businesses

ICO. (n.d.). A guide to the data protection principles. https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/

### Legislation

- Data Protection Act 2018. Available from: https://www.legislation.gov.uk/ukpga/2018/12/contents
- Food Safety Act 1990. Available from: https://www.legislation.gov.uk/ukpga/1990/16/contents
- Food Information Regulations 2014. Available from: https://www.legislation.gov.uk/uksi/2014/1855/contents
- Regulation (EU) No. 1169/2011. Available from: https://www.legislation.gov.uk/eur/2011/1169/contents
- UK GDPR, as amended.

### Internal Project References

- Task 1 – Use Cases: Use Case 1.
- UFCFTR-30-3 – Task 1 Assessment Brief.
- Group 31 Strategic Dependency Model.
- Group 31 Strategic Rationale Model.
- Group 31 Strategic BPMN.
- Sprint 3 – Requirements Traceability and Model Consistency Review (traceability.md).
