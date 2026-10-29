# Sprint 1 – Risk Register

**Project:** Bristol Regional Food Network – Digital Food Marketplace  
**Group:** 31  
**Use Case:** Producer Product Listing and Inventory Management  
**Prepared by:** Tomi  
**Sprint:** Sprint 1 – Strategic Process Analysis and Project Setup  


## 1. Purpose

This register identifies and assesses business, technical, development and teamwork risks that could affect the development and operation of the Bristol Regional Food Network marketplace. It supports prioritisation, monitoring, proposed ownership and mitigation planning. Although the group focuses on Use Case 1, project delivery and collaboration risks are also included.

## 2. Risk Assessment Method

Likelihood (L) and impact (I) are scored from 1 to 5. **Risk score = L × I.**

| Score | Likelihood | Impact |
|---|---|---|
| 1 | Rare | Negligible |
| 2 | Unlikely | Minor |
| 3 | Possible | Moderate |
| 4 | Likely | Major |
| 5 | Almost certain | Critical |

| Score range | Priority | Recommended response |
|---|---|---|
| 1–5 | Low | Monitor during routine reviews |
| 6–14 | Medium | Plan mitigation and review regularly |
| 15–25 | High | Prioritise mitigation and monitor closely |



## 3. Business Risks

| ID | Risk | L | I | Score | Priority | Proposed owner | Status |
|---|---|---:|---:|---:|---|---|---|
| B1 | Invalid or fraudulent organic certification | 3 | 5 | 15 | High | Product Listing lead | Open |
| B2 | Incorrect stock information | 4 | 4 | 16 | High | Inventory lead | Open |
| B3 | Incorrect seasonal availability | 3 | 4 | 12 | Medium | Inventory lead | Open |
| B4 | Expired organic certification | 3 | 4 | 12 | Medium | Product Listing lead | Open |
| B5 | Producer usability difficulties | 4 | 3 | 12 | Medium | Product Listing lead | Open |

### Business risk mitigation

| ID | Potential impact | Mitigation action |
|---|---|---|
| B1 | Misleading organic claims could reduce customer trust and create compliance concerns. | Verify organic claims through the external or simulated certification service before successful publication. |
| B2 | Products may appear available despite insufficient stock. | Validate quantities and automatically mark products unavailable when stock reaches zero. |
| B3 | Products may appear available outside their permitted seasonal period. | Check current dates against availability periods and test boundary conditions. |
| B4 | Listings may display outdated certification information. | Record relevant expiry information and consider re-verification or renewal handling. |
| B5 | Producers may submit incomplete or incorrect information. | Use clear forms, field validation and understandable correction messages. |

## 4. Technical Risks

| ID | Risk | L | I | Score | Priority | Proposed owner | Status |
|---|---|---:|---:|---:|---|---|---|
| T1 | Certification verification service unavailable | 3 | 5 | 15 | High | Product Listing lead | Open |
| T2 | Marketplace system downtime | 3 | 4 | 12 | Medium | Technical integration lead | Open |
| T3 | Inventory update failure | 3 | 4 | 12 | Medium | Inventory lead | Open |
| T4 | Incorrect availability logic | 4 | 4 | 16 | High | Inventory lead | Open |

### Technical risk mitigation

| ID | Potential impact | Mitigation action |
|---|---|---|
| T1 | Producers may be unable to complete certification verification and publish affected listings. | Handle unavailable-service outcomes, consider controlled retries and avoid treating unverified claims as verified. |
| T2 | Producers may be unable to submit products or update stock. | Implement appropriate error handling, backups, monitoring and recovery arrangements. |
| T3 | Stock updates may fail or produce inconsistent information. | Validate updates, handle failed operations and verify that changes are stored correctly. |
| T4 | Products may be shown as available with zero stock or outside seasonal dates. | Test zero stock, positive stock, replenishment and seasonal boundary scenarios. |

## 5. Development Risks

| ID | Risk | L | I | Score | Priority | Proposed owner | Status |
|---|---|---:|---:|---:|---|---|---|
| D1 | Delays implementing the two selected functionalities | 4 | 5 | 20 | High | Sprint Planning lead | Open |
| D2 | Difficulty learning Camunda and BPMN implementation | 4 | 4 | 16 | High | Technical integration lead | Open |
| D3 | Integration problems | 3 | 4 | 12 | Medium | Technical integration lead | Open |
| D4 | Insufficient testing | 4 | 4 | 16 | High | Testing lead | Open |

### Development risk mitigation

| ID | Potential impact | Mitigation action |
|---|---|---|
| D1 | The group may fail to complete the two required workflows within the sprint deadlines. | Prioritise essential functionality, break work into manageable tasks and monitor progress in Notion. |
| D2 | Workflow modelling and implementation may take longer than expected. | Practise Camunda early and begin with simple executable processes before adding complexity. |
| D3 | Workflow components, forms and simulated services may fail to work together. | Test components separately, integrate incrementally and investigate errors early. |
| D4 | Errors may remain in validation, verification and inventory behaviour. | Create test cases covering normal, invalid and exception scenarios and record results. |

## 6. Teamwork Risks

| ID | Risk | L | I | Score | Priority | Proposed owner | Status |
|---|---|---:|---:|---:|---|---|---|
| TW1 | Unequal workload distribution | 3 | 4 | 12 | Medium | Sprint Planning lead | Open |
| TW2 | Poor communication | 3 | 4 | 12 | Medium | All group members | Open |
| TW3 | Missed deadlines | 4 | 5 | 20 | High | Sprint Planning lead | Open |
| TW4 | GitHub merge conflicts or inconsistent files | 3 | 3 | 9 | Medium | GitHub coordination lead | Open |
| TW5 | Inconsistent documentation between Notion and GitHub | 4 | 3 | 12 | Medium | Documentation lead | Open |

### Teamwork risk mitigation

| ID | Potential impact | Mitigation action |
|---|---|---|
| TW1 | Some members may become overloaded, delaying dependent work. | Allocate tasks clearly in Notion and review workload during meetings. |
| TW2 | Members may misunderstand requirements or make conflicting decisions. | Record decisions, communicate blockers and hold regular progress discussions. |
| TW3 | Delayed individual tasks may affect shared sprint deliverables. | Set realistic due dates, track progress and raise delays early. |
| TW4 | Changes may overwrite one another or introduce conflicting versions. | Use appropriate branches, review changes and coordinate merges. |
| TW5 | Notion pages, GitHub files and BPMN may contain conflicting information. | Link Notion tasks to GitHub artefacts, identify the authoritative version and review documentation consistency. |

## 7. Highest-Priority Risks

| Risk | Score | Priority action |
|---|---:|---|
| D1 – Implementation delays | 20 | Prioritise essential functionality and monitor delivery progress |
| TW3 – Missed deadlines | 20 | Track deadlines and dependencies in Notion |
| B2 – Incorrect stock information | 16 | Validate inventory updates |
| T4 – Incorrect availability logic | 16 | Test stock and seasonal availability rules |
| D2 – Camunda implementation difficulties | 16 | Begin workflow implementation exercises early |
| D4 – Insufficient testing | 16 | Prepare test scenarios before integration |
| B1 – Invalid organic certification | 15 | Verify organic claims |
| T1 – Certification service unavailable | 15 | Design and test exception handling |

## 8. Risk Ownership and Monitoring

Risk owners monitor assigned risks, report changes and coordinate mitigation actions. The owner labels above refer to **proposed project roles**, not confirmed assignments to named group members.



| Status | Meaning |
|---|---|
| Open | Risk identified; mitigation not yet completed |
| Monitoring | Risk is being tracked and mitigation is underway |
| Mitigated | Actions have reduced risk to an acceptable level |
| Closed | Risk is no longer relevant or has been resolved |

## 9. Relationship to Use Case 1

Business and technical risks directly relevant to Use Case 1 concern product information, organic certification, inventory accuracy and seasonal availability.

**Product Listing and Validation:** invalid product information; fraudulent or invalid organic certification; unavailable verification service.

**Inventory and Seasonal Availability Management:** zero stock; incorrect stock updates; replenishment; products outside their seasonal period.

Development and teamwork risks affect the group's ability to complete, test and demonstrate both functionalities.

