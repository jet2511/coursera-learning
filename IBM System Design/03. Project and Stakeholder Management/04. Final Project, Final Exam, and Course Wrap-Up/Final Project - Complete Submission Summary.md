# Final Project: Shop Ease Online AI Chatbot (Toàn bộ Bài làm 5 Task)

Dưới đây là chi tiết toàn bộ nội dung hoàn chỉnh của 5 Task cho bài tập lớn Final Project (đã được tạo thành 5 file `.docx` định dạng chuẩn sẵn sàng nộp).

---

## 📄 Task 1: Business Case Review (`Task1_BusinessCaseReview.docx`)

| Goal | Challenge | Assumption | Data Gap | Clarification Question |
| :--- | :--- | :--- | :--- | :--- |
| **Reduce customer service operating costs by 30%** through automated routine inquiry resolution. | Surge in customer inquiry volume overwhelming live agents and causing long email response backlogs. | Shop Ease Online's CRM and Order Management Systems (OMS) have modern, robust REST/GraphQL APIs ready for chatbot integration. | Current volume and breakdown of routine vs. complex inquiries (e.g., % of order tracking vs. technical complaints). | What specific APIs or database access protocols are currently exposed by the CRM and OMS? |
| **Improve CSAT from 78% to 90%** by eliminating wait times and improving service consistency. | Inconsistent service quality and prolonged wait times currently damaging customer trust. | A response time of under 10 seconds and 24/7 availability will directly boost customer satisfaction and loyalty. | Detailed baseline metrics on peak traffic hours, inquiry categories, and root causes of customer dissatisfaction. | What criteria will determine whether an inquiry is resolved successfully by AI vs. transferred to a human agent? |
| **Achieve sub-10s response times** with 24/7 automated support availability. | High operational costs associated with staffing live agents 24/7 and during non-business hours. | Customers are receptive to interacting with an AI chatbot for routine transactions like order tracking. | Historical data on multi-language distribution across international and non-English customer segments. | Which primary languages must be supported in Phase 1 vs. subsequent rollout phases? |
| **Increase sales conversion during off-hours** by answering pre-purchase questions instantly. | Risk of user frustration and drop-off if complex issues are not handed off seamlessly to human agents. | Live agents can be effectively retrained within 4 weeks to handle complex, escalated customer cases. | Cost baseline per support ticket (live agent vs. email) to accurately measure the 30% cost reduction target. | What is the agreed fallback mechanism and SLA for human handoff during off-hours when live agents are unavailable? |

---

## 📄 Task 2: Gather Requirements (`Task2_Requirements.docx`)

| Requirement Name | Type | Priority (MoSCoW) | Rationale |
| :--- | :--- | :--- | :--- |
| **24/7 Real-Time Automated Q&A** | Functional | **Must Have** | Provides instant answers to routine inquiries and product questions at any time, reducing baseline ticket volume. |
| **Real-Time Order Tracking & Status Lookup** | Functional | **Must Have** | Integrates with OMS to allow customers to check real-time order and shipping status without human assistance. |
| **CRM Integration for Customer History** | Functional | **Must Have** | Enables personalized support by retrieving customer profile, purchase history, and open tickets directly from CRM. |
| **Seamless Live Agent Escalation & Handoff** | Functional | **Must Have** | Transfers complex or sensitive inquiries to human agents with full conversation context to avoid customer frustration. |
| **Multi-Language Support (Top 3 Languages)** | Functional | **Should Have** | Broadens accessibility and improves CSAT for non-native speaking and international customer segments. |
| **Off-Hours Pre-Purchase Recommendation** | Functional | **Should Have** | Suggests relevant electronics products based on customer queries to directly drive off-hours sales conversion. |
| **Automated Post-Chat CSAT Survey** | Functional | **Should Have** | Collects immediate customer feedback post-interaction to measure and track the target 90% CSAT goal. |
| **Automated Return & Refund Guidance** | Functional | **Nice to Have** | Guides users step-by-step through self-service return and refund requests, further lowering agent workloads. |
| **Sub-10 Second Response Latency** | Non-Functional | **Must Have** | Ensures high responsiveness and smooth conversational experience, directly meeting the core business KPI. |
| **GDPR & Data Privacy Compliance** | Non-Functional | **Must Have** | Protects sensitive customer PII and payment data, ensuring regulatory adherence and preventing legal liabilities. |
| **High System Availability (99.9% Uptime)** | Non-Functional | **Should Have** | Guarantees 24/7 reliability and minimal downtime during peak shopping hours and promotional campaigns. |
| **High Concurrent Scalability (5,000 Users)** | Non-Functional | **Should Have** | Maintains performance stability and fast response times during major traffic spikes such as Black Friday. |

---

## 📄 Task 3: Develop a RACI Chart (`Task3_RACI.docx`)

| Stakeholder | Role Description | RACI Designator(s) |
| :--- | :--- | :---: |
| **Executive Sponsor (CEO)** | Provides overarching strategic vision, champions organizational alignment, and holds ultimate executive authority for budget approval and project sign-off. | **Accountable (A)** |
| **Program Manager** | Leads project planning, coordinates cross-functional workstreams, manages schedule, risks, scope, budget, and overall day-to-day execution. | **Responsible (R), Accountable (A)** |
| **IT/AI Lead** | Directs technical architecture, AI model configuration, CRM/OMS system integrations, infrastructure performance, and technical testing. | **Responsible (R)** |
| **Customer Service Manager** | Defines support workflows, knowledge base content, agent handoff protocols, and leads live-agent training and operational adoption. | **Responsible (R), Consulted (C)** |
| **Marketing Manager** | Develops promotional campaigns, drives customer awareness of the new AI chatbot, and aligns conversational tone with brand voice. | **Consulted (C), Informed (I)** |
| **Data Protection Officer (DPO)** | Conducts privacy impact assessments, audits data handling practices, and ensures strict compliance with GDPR and relevant privacy regulations. | **Consulted (C)** |
| **End Customers** | Direct users of the chatbot interface who interact with the system, submit inquiries, and provide CSAT ratings and feedback. | **Informed (I)** |

---

## 📄 Task 4: Map Stakeholder Engagement Strategies (`Task4_StakeholderEngagement.docx`)

| Stakeholder | Power | Interest | Engagement Strategy | Communication Method | Frequency |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **Executive Sponsor (CEO)** | High | High | **Manage Closely:** Provide strategic progress summaries, key milestone achievements, ROI tracking, and seek rapid decisions on major scope/budget changes. | Executive Steering Meetings & Monthly Executive Briefings / Dashboards | Bi-weekly / Monthly |
| **Program Manager** | High | High | **Manage Closely:** Drive daily alignment, monitor workstream dependencies, resolve blockers proactively, and track deliverables against schedule. | Daily Standups, Weekly PMO Reviews, Jira/Project Management Dashboards | Daily / Continuous |
| **IT/AI Lead** | Medium | High | **Keep Satisfied / Active Partner:** Collaborate closely on technical architecture, system integration milestones, API readiness, and security standards. | Sprint Planning, Architecture Review Sessions, Slack/Teams Dedicated Channel | Weekly / As-needed |
| **Customer Service Manager** | Medium | High | **Keep Satisfied / Active Partner:** Engage continuously on chatbot knowledge base training, escalation workflows, change management, and agent feedback. | Bi-weekly Working Sessions, User Acceptance Testing (UAT) Workshops | Bi-weekly |
| **Marketing Manager** | Low | High | **Keep Informed:** Keep updated on launch timelines, brand voice alignment, promotional release dates, and key feature rollouts. | Email Newsletters, Marketing Alignment Meetings | Bi-weekly / Milestone-based |
| **Data Protection Officer (DPO)** | High | Medium | **Keep Satisfied:** Involve proactively in data flow reviews, security audits, privacy policy sign-offs, and compliance checkpoints. | Formal Compliance Review Meetings, Audit Report Sign-offs | Monthly / Milestone Gates |
| **End Customers** | Low | High | **Keep Informed:** Announce new support capabilities, highlight 24/7 self-service convenience, and capture feedback via post-chat surveys. | In-app Announcements, Website Banners, Email Updates, Chatbot Welcome Greetings | At Launch & Continuous |

---

## 📄 Task 5: Reflection (`Task5_Reflection.docx` - 275 words)

> **Reflection on Generative AI in Program & Stakeholder Management**
>
> Generative AI significantly enhanced the efficiency and analytical depth throughout this project. By processing the Shop Ease Online business case, GenAI rapidly generated structured baselines for requirements elicitation, RACI assignment, and stakeholder engagement matrices. It helped overcome the "blank page syndrome," allowing me to transition quickly from initial ideation to structured analysis. Furthermore, GenAI provided creative perspectives on potential edge cases, such as off-hours sales conversion and multi-language support, which enriched the functional scope.
>
> However, several notable limitations were observed in the AI's raw outputs. AI responses often defaulted to generic e-commerce assumptions rather than strictly adhering to the technical and operational boundaries of the scenario. For instance, initial suggestions included complex AI capabilities that exceeded the immediate project timeline or overlooked specific legacy CRM integration constraints. Additionally, AI lacked organizational context regarding internal company politics and actual resource availability, occasionally misallocating stakeholder accountabilities.
>
> To effectively mitigate these limitations, a Business Analyst or Project Manager must exercise professional judgment through a rigorous validation workflow. First, AI outputs must be cross-referenced against business objectives, contractual constraints, and technical architecture specifications. Second, requirements and RACI matrices should be validated through collaborative stakeholder workshops (e.g., UAT sessions and compliance reviews with the DPO and IT Lead). Finally, iterative prompt engineering and human-in-the-loop review are essential to refine AI-generated drafts into actionable, production-ready deliverables that ensure true business alignment and risk governance.
