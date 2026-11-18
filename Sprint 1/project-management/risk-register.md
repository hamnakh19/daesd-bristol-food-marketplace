
# Sprint 1 – Project Risk Register

## Define Risk mitigation strategies

This Risk Register identifies potential technical, business and development risks associated with the project. Each risk is assessed according to its likelihood and impact, with mitigation strategies identified to reduce potential disruption.

| Risk | Explanation | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| GitHub merge conflicts | Multiple team members may edit the same files, causing conflicts when merging their work. | Medium | Medium | Use separate branches and review pull requests. |
| Inaccurate or incomplete strategic BPMN model | Important business processes, actors or interactions may be missing or incorrectly represented. | Medium | High | Review the model against the case study and use group feedback to identify and correct errors before submission. |
| False organic certification | A producer could submit a certificate that isn't genuine. | Medium | High | Verify certification details using an external or simulated verification service and reject invalid claims. |
| Certification service unavailable | The system can't verify a certificate. | Medium | High | Add an exception/retry path and don't automatically publish until the required verification is resolved. |
| Certificate expires / needs renewal | A previously valid certification may no longer be valid. | Medium | High | Store certificate/expiry information and require re-verification or renewal. |
| Server/system goes down | Technical failures may prevent producers from listing products or updating inventory. | Low | High | Use error handling, backups, monitoring and a recovery procedure. |
| Incorrect stock information | Inventory quantities may be inaccurate, allowing customers to order unavailable products. | Medium | High | Validate stock updates and automatically change availability when stock reaches zero. |
| Seasonal availability error | Products may remain available outside their permitted seasonal period. | Medium | High | Check the current date against product availability dates and automatically update listing availability. |
| Development risk | Technical difficulties or underestimated workloads may prevent planned tasks from being completed on time. | Medium | High | Prioritise essential tasks, maintain a realistic sprint backlog and review progress regularly. |
| Farmer/producer usability | Producers may struggle to complete forms or understand validation errors. | Medium | Medium | Keep forms clear, validate input and provide useful error messages. |
| Missed sprint deadlines | Delayed contributions may prevent the group from completing assessment deliverables before submission. | Medium | High | Set internal deadlines, track task progress through Notion and raise delays during group meetings. |
| Unclear team responsibilities | Overlapping or poorly assigned tasks may cause duplicated work or incomplete deliverables. | Medium | Medium | Assign clear task ownership and update responsibilities through group discussions. |
| Incomplete product information | Producers may forget mandatory details such as price, stock quantity, product origin or availability dates. | High | Medium | Validate mandatory product fields before approving product publication. |
