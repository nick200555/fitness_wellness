# Fitness & Wellness Management System — Frappe / ERPNext v15+

> **Version:** 1.0 | **Year:** 2026 | **Framework:** Frappe v15+ / ERPNext v15+

A comprehensive custom Frappe application that manages the complete fitness business value chain — from member onboarding and subscription management through class scheduling, trainer management, equipment maintenance, health assessments, nutrition planning, and billing — natively integrating with ERPNext's Accounts, HR, Stock, and CRM modules.

---

## 📋 System Overview

| Metric | Value |
|--------|-------|
| Core Modules | 8 |
| Total DocTypes | 58+ |
| Script Reports | 11 |
| ERPNext Integrations | 6 modules |
| Custom Roles | 7 |
| Build Phases | 5 phases / ~22 weeks |

---

## ✨ Features

### 👥 Module 1 — Member & Subscription Management
Member registry, subscription plans, renewals, attendance, freeze/cancel, and referral programs. Members are modelled as ERPNext Customers with extended custom fields.

- **Member** — Core member register with full personal and fitness profile
- **Membership Plan** — Available plans with pricing, duration, and entitlements
- **Member Subscription** — Active subscription with auto end-date and credit tracking
- **Member Attendance** — Daily check-in/check-out via biometric, QR or manual
- **Subscription Freeze** — Temporary suspension with auto end-date extension
- **Referral Record** — Referral reward tracking

### 📅 Module 2 — Class & Schedule Management
Class types, timetables, batch enrollment, trainer assignment, and waitlists.

- **Class Type** — Yoga, Zumba, HIIT, Spinning, Aqua Aerobics and more
- **Class Schedule** — Recurring or one-off timetable with capacity management
- **Class Enrollment** — Member booking with credit deduction and waitlist support
- **Class Attendance** — Post-session attendance and rating capture
- **Waitlist Entry** — Auto-notification queue with expiry deadline
- **Class Package** — Standalone class packs for non-members or add-on credits

### 🏋️ Module 3 — Trainer & Staff Management
Trainer profiles, certifications, availability slots, member assignments, commission calculations, all linked to ERPNext Employee.

- **Trainer Profile** — Specialisation, ratings, PT rates, commission type
- **Trainer Certification** — ACE-CPT, NASM, RYT certificates with expiry tracking
- **Trainer Availability** — Weekly slots for PT and group class booking
- **Trainer Assignment** — PT member linking with session progress tracking
- **Trainer Commission** — Auto-calculated with TDS deduction; creates Journal Entry

### 🏢 Module 4 — Facility & Equipment Management
Equipment register, maintenance schedules, AMC contracts, locker management. Linked to ERPNext Fixed Assets.

- **Equipment Register** — Full asset lifecycle with warranty and AMC linkage
- **Maintenance Schedule** — Preventive/corrective schedule with vendor assignment
- **Maintenance Log** — Breakdown records with cost and downtime tracking
- **AMC Contract** — Annual Maintenance Contracts covering multiple equipment
- **Locker Master** — Locker inventory with size, zone, and rental charge
- **Locker Assignment** — Member locker allocation history

### 🩺 Module 5 — Health & Fitness Assessment
Body metrics, fitness tests, goal tracking, and progress photos. Linked to trainer assignments and diet plans.

- **Health Profile** — Initial health assessment with PAR-Q and goals
- **Body Metric Log** — Weight, BMI, body fat %, measurements over time
- **Fitness Test** — Push-ups, VO2 Max, 1RM, 5KM run, composite score
- **Fitness Goal** — Quantified goals with progress % auto-calculation
- **Progress Photo** — Before/after photo tracking

### 🍏 Module 6 — Nutrition & Diet Management
Diet plans, meal templates, supplement tracking, and nutrition goal monitoring.

- **Food Item** — Database with macros (protein, carbs, fat, fibre, sodium per serving)
- **Meal Template** — Pre-defined meals (Breakfast, Pre-Workout, Dinner etc.)
- **Diet Plan** — Personalised 7–30 day plans with daily meal schedule
- **Nutrition Goal** — Caloric deficit/surplus targets with compliance %
- **Supplement Log** — Supplement tracking with frequency and recommending trainer

### 💸 Module 7 — Billing & Finance
Full ERPNext integration — Sales Invoice, POS Invoice, Payment Entry, Credit Note, Journal Entry.

- **Membership Invoice** — Auto-generated on subscription submit; links to Sales Invoice
- **Walk-In Payment** — POS record for day passes, group classes, merchandise, café
- **EMI Schedule** — Auto-generated instalment schedule with NACH/UPI mandate support
- **Refund Request** — Approval workflow resulting in ERPNext Credit Note
- **Daily Cash Reconciliation** — Opening/closing cash, POS + invoice totals, variance

### 📈 Module 8 — Reports & Analytics
All reports are Frappe Script Reports. Dashboards use ERPNext Number Cards & Charts.

| Report | Purpose |
|--------|---------|
| Member Enrollment & Retention | New joins, renewals, drop-offs, churn rate |
| Revenue Summary | Gross revenue, discounts, net collections, plan-wise split |
| Trainer Performance Report | Sessions, ratings, PT vs group, commission |
| Class Occupancy Report | Enrolled vs attended, avg occupancy %, peak time |
| Member Attendance Report | Visit frequency, avg duration, streaks |
| Equipment Utilization & Downtime | Uptime %, maintenance cost, breakdown frequency |
| Membership Expiry Alert | Members expiring in N days, renewal follow-up |
| Member Progress Dashboard | Weight, BMI, body fat trend, goal achievement % |
| Fitness Manager Dashboard | Active members, today's revenue, class occupancy |
| Daily Cash Collection | POS + invoice collections, reconciliation status |
| Subscription Plan Analysis | Plan-wise popularity, revenue, renewal rate |

---

## 🗂️ Directory Structure

```
fitness_wellness/                  ← Frappe app root
├── setup.py
├── requirements.txt
├── pyproject.toml
├── MANIFEST.in
├── package.json
└── fitness_wellness/              ← Python package
    ├── __init__.py
    ├── hooks.py                   ← Scheduler events, doc events, roles, app_include_js
    ├── patches.txt
    ├── tasks.py                   ← Scheduled tasks (Daily / Weekly / Monthly)
    │
    ├── config/
    │   ├── desktop.py             ← Workspace module tiles
    │   └── docs.py
    │
    ├── utils/
    │   ├── __init__.py
    │   ├── calculations.py        ← Proration, EMI, commission engine
    │   ├── notifications.py       ← SMS/email triggers
    │   └── validators.py
    │
    ├── member_management/
    │   ├── __init__.py            ← handle_subscription_cancel
    │   ├── doctype/
    │   │   ├── member/
    │   │   ├── membership_plan/
    │   │   ├── member_subscription/
    │   │   ├── member_attendance/
    │   │   ├── subscription_freeze/
    │   │   └── referral_record/
    │   └── report/
    │
    ├── class_management/
    │   ├── __init__.py            ← update_class_capacity
    │   ├── doctype/
    │   │   ├── class_type/
    │   │   ├── class_schedule/
    │   │   ├── class_enrollment/
    │   │   ├── class_attendance/
    │   │   ├── waitlist_entry/
    │   │   └── class_package/
    │   └── report/
    │
    ├── trainer_management/
    │   └── doctype/
    │       ├── trainer_profile/
    │       ├── trainer_certification/
    │       ├── trainer_availability/
    │       ├── trainer_assignment/
    │       └── trainer_commission/
    │
    ├── facility_management/
    │   └── doctype/
    │       ├── equipment_register/
    │       ├── maintenance_schedule/
    │       ├── maintenance_log/
    │       ├── amc_contract/
    │       ├── locker_master/
    │       └── locker_assignment/
    │
    ├── health_assessment/
    │   └── doctype/
    │       ├── health_profile/
    │       ├── body_metric_log/
    │       ├── fitness_test/
    │       ├── fitness_goal/
    │       └── progress_photo/
    │
    ├── nutrition/
    │   └── doctype/
    │       ├── food_item/
    │       ├── meal_template/
    │       ├── diet_plan/
    │       ├── nutrition_goal/
    │       └── supplement_log/
    │
    ├── billing/
    │   ├── __init__.py            ← auto_create_membership_invoice, create_sales_invoice
    │   └── doctype/
    │       ├── membership_invoice/
    │       ├── walk_in_payment/
    │       ├── emi_schedule/
    │       ├── refund_request/
    │       └── daily_cash_reconciliation/
    │
    ├── fixtures/
    │   ├── custom_fields.json     ← Custom fields on Customer, Employee, Item, Asset
    │   ├── property_setters.json
    │   └── roles.json
    │
    ├── public/
    │   ├── js/
    │   │   └── fitness_wellness.js
    │   └── css/
    │
    └── templates/
        └── pages/                 ← Member self-service portal pages
```

---

## 🏷️ DocType Naming Series

| DocType | Series | Example |
|---------|--------|---------|
| Member | `MEM-.YYYY.-.####` | MEM-2026-0001 |
| Member Subscription | `SUB-.YYYY.MM.-.####` | SUB-2026-06-0088 |
| Membership Invoice | `MINV-.YYYY.MM.-.####` | MINV-2026-06-0042 |
| Class Schedule | `CLS-.YYYY.-.####` | CLS-2026-0015 |
| Class Enrollment | `ENR-.YYYY.MM.DD.-.###` | ENR-2026-06-15-001 |
| Trainer Profile | `TRN-.YYYY.-.###` | TRN-2026-001 |
| Trainer Commission | `TCOM-.YYYY.MM.-.####` | TCOM-2026-06-0007 |
| Equipment Register | `EQP-.YYYY.-.####` | EQP-2026-0099 |
| Maintenance Log | `MLOG-.YYYY.-.####` | MLOG-2026-0033 |
| Refund Request | `REF-.YYYY.MM.-.####` | REF-2026-06-0005 |
| Diet Plan | `DIET-.YYYY.-.####` | DIET-2026-0012 |

---

## 🔗 ERPNext Integration Points

| ERPNext Module | Integration |
|----------------|-------------|
| **Accounts** | Membership Invoice → Sales Invoice; Walk-In → POS Invoice; Commission → Journal Entry; Refund → Credit Note |
| **CRM / Sales** | Member registered as Customer (`customer_group = Fitness Member`); Lead → Member on enrolment |
| **Stock** | Merchandise/supplements as Items; Walk-In triggers Stock Ledger Entry; reorder alerts |
| **HR & Payroll** | Trainers as Employees; Shift Management; Commission as salary component |
| **Fixed Assets** | Equipment → Fixed Asset; depreciation per category; maintenance cost expensed |
| **Quality** | Pool water quality as Quality Inspections; FSSAI compliance for café/supplements |

---

## 🚀 Installation

```bash
# 1. Get the app into your bench
bench get-app fitness_wellness https://github.com/nick200555/fitness_wellness.git

# 2. Install on your ERPNext site
bench --site your-site.local install-app fitness_wellness

# 3. Run database migrations
bench --site your-site.local migrate

# 4. Restart bench services
bench restart

# 5. Clear cache
bench --site your-site.local clear-cache

# 6. (Optional) Load demo fixtures
bench --site your-site.local execute fitness_wellness.setup.load_demo_data
```

---

## 🖥️ Server Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| OS | Ubuntu 20.04 LTS | Ubuntu 22.04 LTS |
| Python | 3.10+ | 3.11+ |
| Node.js | 18.x | 20.x LTS |
| MariaDB | 10.6+ | 10.11+ |
| Redis | 6.x | 7.x |
| RAM | 8 GB | 16 GB |
| Disk | 50 GB SSD | 200 GB SSD |
| ERPNext | v15.0 | v15 latest |
| Frappe | v15.0 | v15 latest |

---

## 👤 Custom Roles

| Role | Primary Access |
|------|----------------|
| **Fitness Manager** | Class scheduling, membership plans, trainer mgmt, all reports |
| **Front Desk Executive** | Create members, check-ins, class bookings, walk-in payments |
| **Trainer** | Class attendance, PT assignments, client health assessments |
| **Dietitian** | Nutrition plans, meal templates, health profiles |
| **Accounts Executive** | Invoices, EMI scheduling, daily cash reconciliation |
| **Facility Supervisor** | Equipment registry, maintenance logs, lockers |
| **Member** | Self-service portal — bookings, diet plans, invoices |

---

## 🗺️ Implementation Roadmap

| Phase | Weeks | Scope |
|-------|-------|-------|
| **Phase 1** | 1–3 | Foundation: DocTypes, hooks, roles, fixtures, ERPNext custom fields |
| **Phase 2** | 4–8 | Member, Class & Attendance Management modules |
| **Phase 3** | 9–13 | Trainer, Facility & Health Assessment modules |
| **Phase 4** | 14–17 | Nutrition, Billing & Finance modules |
| **Phase 5** | 18–22 | Reports, Dashboards, Member Portal & Go-Live |

---

## 📄 License

MIT
