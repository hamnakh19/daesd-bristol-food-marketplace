# Functionality Analysis

**Project:** Bristol Regional Food Network Digital Food Marketplace  
**Use Case:** Use Case 1 – Producer Product Listing and Inventory Management  
**Contributor:** Tahiyah 
**Purpose:** **Purpose:** Identify and analyse two key functionalities for the Bristol Regional Food Network Digital Food Marketplace, define their scope and boundaries, and justify why they were selected for the project.

## 1. Identify Two Major Functionalities

### Functionality 1: Product Listing and Validation

This functionality allows registered producers to add new products to the Bristol Regional Food Network marketplace. Producers submit details such as the product name, description, category, price, quantity, farm origin and availability period. The system checks that all required information is provided and valid. If information is missing or incorrect, the producer is asked to make corrections. If a producer claims organic certification, the system checks it using an external or simulated verification service. Once all the required checks are successful, the product is published and becomes available for customers to view.

### Functionality 2: Inventory and Seasonal Availability Management

This functionality allows producers to manage their stock levels and update the seasonal availability of their products. When a product's stock reaches zero, it automatically becomes unavailable for new orders. If the producer replenishes the stock and the product is still within its availability period, it can become available again. This helps keep product listings accurate and prevents customers from ordering products that are out of stock or out of season.

## 2. Define Scope and Boundaries of Both Functionalities

### Functionality 1: Product Listing and Validation

**In scope:**
- Allow registered producers to submit new product listings.
- Collect the required product details, including name, description, category, price, quantity, farm origin and availability period.
- Include relevant information such as harvest date, allergen details, organic certification and best-before date.
- Validate the submitted information and ask producers to correct missing or invalid details.
- Check organic certification using an external or simulated verification service.
- Handle failed validation and situations where the certification service is unavailable.
- Publish products once all required checks have been completed successfully.

**Out of scope:**
- Customer ordering and payment processing.
- Delivery and collection arrangements.
- Managing producer payments and the marketplace's 5% commission.
- Implementing a full external organic certification system. The verification service can be simulated for this project.

### Functionality 2: Inventory and Seasonal Availability Management

**In scope:**
- Allow producers to update product quantities.
- Allow producers to update seasonal availability periods.
- Automatically mark products as unavailable when stock reaches zero.
- Make products available again when stock is replenished and they are still within their seasonal availability period.
- Ensure customers can only order products that are available.
- Keep product availability information up to date on the marketplace.

**Out of scope:**
- Processing customer payments or calculating producer settlements.
- Managing deliveries and order fulfilment.
- Calculating food miles or managing surplus-food discounts.
- Full stock forecasting or automated demand prediction.

## 3. Justify the Selected Functionalities

We selected Product Listing and Validation and Inventory and Seasonal Availability Management because they are essential to the day-to-day operation of the Bristol Regional Food Network marketplace.

Product Listing and Validation ensures that product information is complete and accurate before anything is published. It also allows organic certification claims to be checked, helping maintain customer trust and making the marketplace's listings more reliable. Including validation and handling failed checks also gives us clear processes to model and test.

Inventory and Seasonal Availability Management was selected because the marketplace sells local food, and the availability of products can change depending on stock levels and the season. Automatically making products unavailable when stock reaches zero helps prevent customers from ordering products that cannot be supplied. Allowing products to become available again when stock is replenished also keeps listings up to date.

These functionalities are closely connected because a product must first be listed and validated before its stock and availability can be managed. Together, they cover an important part of the producer's interaction with the marketplace and provide clear workflows for our group to analyse, model and potentially implement using BPMN and Camunda. They also give us a manageable project scope while leaving other areas, such as payments and order fulfilment, as separate business processes.