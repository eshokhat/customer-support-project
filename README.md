# Customer Support Performance Analysis

## Overview
This project explores the operational efficiency of a customer support team — tracking ticket volumes, escalation trends, and issue distribution across channels.  
The goal was to model a realistic workflow for a support analytics function: data generation, KPI design, and dashboard creation.

The dataset was created programmatically to mirror one year of customer interactions.  
All analysis and visualization were performed in **Excel**.

---

## Data
The dataset was generated with Python (`dataset.py`) and includes **50,000 simulated tickets** covering a full year.  
Each record contains:
- Ticket ID  
- Date opened  
- Channel (App, Phone, Website)  
- Issue type (Block Card, Limit, Refund, Tech)  
- Time to resolution (minutes)  
- Status (Escalated, Resolved, Reopened)

The structure imitates a standard customer service log, allowing exploration of volume dynamics and escalation patterns.

---

## Tools and Methods
- **Python (pandas, faker)** — data generation and preprocessing.  
- **Excel** — aggregation, analysis, and visualization:
  - Pivot tables for monthly, channel, and issue-level summaries.  
  - `COUNTIFS` / `AVERAGEIFS` formulas for KPI calculation.  
  - Conditional formatting to highlight outliers and SLA breaches.  
  - Stacked and clustered column charts for trends and composition.  
  - KPI cards summarizing overall performance.

---

## Key Results
| Metric | Value | Interpretation |
|--------|--------|----------------|
| Total Tickets | 50,000 | Annual support volume |
| Escalation Rate | 33% | Higher than optimal (<20%) |
| Avg Resolution Time | 37 min | Steady across all months |
| Channel Split | App 34% / Phone 33% / Web 33% | Balanced communication load |
| Issue Types | ~25% each | No dominant category |

---

## Insights
- Roughly one in three tickets is **escalated**, suggesting room to strengthen first-contact resolution.  
- **Even issue and channel distribution** indicates process balance — no single failure point.  
- Ticket flow is **stable month over month** (~5.5K tickets), a sign of consistent demand.  
- The combination of balanced load and high escalation rate points to a **training or SOP optimization opportunity**, not a capacity issue.

---

## Deliverables
- `dataset.py` — Python script that generates the dataset.  
- `dataset.csv` — exported synthetic dataset.  
- `customer-support-project.xlsx` — Excel dashboard with pivots, visuals, and KPIs.  
- `screenshots/` — static exports for portfolio presentation.

---

## Tech Stack
**Python** — pandas, faker  
**Excel** — pivot tables, COUNTIFS, conditional formatting, stacked & clustered charts  

---

## Notes
All data is **synthetic** and created solely for analytical demonstration.  
The purpose of the project is to showcase analytical thinking, business interpretation, and dashboard design using accessible tools.
