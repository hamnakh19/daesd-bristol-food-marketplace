# Sprint 1 – Business Analysis

**Project:** Bristol Regional Food Network Digital Food Marketplace  
**Assigned use case:** Use Case 1 – Producer Product Listing and Inventory Management  
**Contributor:** Tomi  
**Purpose:** to Support the group's enterprise-level strategic BPMN and Sprint 1 analysis.

## 1. Major Business Processes

| Major business process | Purpose | Main participants |
|---|---|---|
| Product Management and Inventory Control | Manage product submission, validation, publication, stock quantities and seasonal availability. | Producer; Marketplace System |
| Customer Browsing and Ordering | Enable customers to browse or search products, select items from multiple producers and submit orders. | Customer; Marketplace System |
| Payment Processing and Producer Settlements | Submit payment requests, calculate amounts attributable to producers and the marketplace's 5% commission. | Marketplace System; Payment Service |
| Order Management and Fulfilment | Check item availability, create overall and producer-specific order elements, notify producers and determine delivery or collection arrangements. | Customer; Producer; Marketplace System |
| Food Quality Assurance and Traceability | Record food-quality incidents, identify affected products and customer orders, coordinate notifications and review incident closure. | Customer; Producer; Marketplace Administrator; Marketplace System |
| Sustainability and Community Engagement | Represent the broader local-food and sustainability aims identified in the group's enterprise analysis. | Marketplace stakeholders (specific responsibilities to confirm) |

**Scope note:** The first five processes are grounded in the supplied use cases. Sustainability and Community Engagement is a broader process identified in the group's analysis; the supplied use-case descriptions do not specify its detailed workflow. The case study requires producer allocations and a 5% commission calculation but does not prescribe a settlement schedule.

## 2. Actors and Organisational Responsibilities

| Actor or participant | Responsibility | Related processes |
|---|---|---|
| Producer | Submit and correct product information; update stock and seasonal availability; provide information during food-quality investigations. | Product Management; Food Quality |
| Customer | Browse and order products, make payments, report potential food-quality concerns and receive notifications. | Browsing and Ordering; Payments; Food Quality |
| Marketplace Administrator / authorised representative | Report or review food-quality incidents and decide whether further action is needed. | Food Quality Assurance |
| Marketplace System | Validate product information; publish eligible listings; control stock availability; check orders; maintain traceability records; coordinate service interactions. | Multiple processes |
| Organic Certification Verification Service | Verify claimed organic certification information and return a result. | Product Management |
| Payment Service | Process payment requests and return success, decline or unavailable outcomes. | Payment Processing |



## 3. External Service Interactions

| External service | Trigger | Interaction | Exception handling required |
|---|---|---|---|
| Organic Certification Verification Service | A producer claims organic certification when submitting a product. | The marketplace checks certification details through an external or simulated service and receives a verification outcome. | Handle unsuccessful verification or service unavailability; do not assume the product can be published without successful required validation. |
| Payment Service | A customer confirms an order and payment is submitted. | The marketplace sends the payment request to an external or simulated service and receives an outcome. | Inform customer of declined payment and allow retry; handle temporary service unavailability through an exception or retry path. |

