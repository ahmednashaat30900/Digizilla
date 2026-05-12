# Digizilla

![Odoo Version](https://img.shields.io/badge/Odoo-19.0%20Community-7C3AED)
![License](https://img.shields.io/badge/License-LGPL--3-blue)
![Version](https://img.shields.io/badge/Version-19.0.1.0.0-green)

A custom Odoo addon that introduces the **Digizilla** model — a complete record management application with form, kanban, list, and pivot views, PDF reporting, role-based access control, and a custom JavaScript enhancement.

---

## 📋 Table of Contents

- [Features](#features)
- [Module Structure](#module-structure)
- [Requirements](#requirements)
- [Security](#security)
- [PDF Reports](#pdf-reports)


---

## ✨ Features

- **10 model fields** including computed age, relational fields, and an HTML notes editor
- **4 views**: Form, Kanban, List (with optional columns), and Pivot
- **PDF Report** accessible directly from the form view — includes all model fields
- **Security group** `Digizillians` — only members can access the application
- **Chatter integration** — full message log and activity tracking on every record
- **Auto-computed Age** — calculated from birth date in real time
- **Sales Order count** — automatically counts related sales orders for the linked customer
- **Hide Create button** — JavaScript patch removes the New/Create button from the form view

---

## 🗂️ Module Structure

```
digizilla/
├── __manifest__.py                         # Module metadata and dependencies
├── __init__.py
├── models/
│   ├── __init__.py
│   └── digizilla.py                        # Main model with all fields and compute methods
├── views/
│   ├── digizilla_views.xml                 # Form, Kanban, List, Pivot views + action
│   └── digizilla_menu.xml                  # App menu (restricted to Digizillians group)
├── security/
│   ├── digizilla_security.xml              # Security group definition
│   └── ir.model.access.csv                 # Model access rights
├── report/
│   ├── digizilla_report.xml                # Report action (PDF)
│   └── digizilla_report_template.xml       # QWeb PDF template
└── static/
    └── src/
        └── js/
            └── digizilla_form.js           # Hides Create button in form view
```

---

## ⚙️ Requirements

| Dependency | Version |
|---|---|
| Odoo | 19.0 Community Edition |
| Python | 3.10+ |
| PostgreSQL | 14+ |
| wkhtmltopdf | 0.12.6 (for PDF reports) |

**Odoo module dependencies** (standard — no third-party modules):
- `base`
- `mail`
- `sale_management`

---



### Views

| View | Description |
|---|---|
| **List** | Columns: Name, Birth Date, Age, Tags. Optional: Country, Gender |
| **Kanban** | Cards showing Name, Age, Tags, Customer, Sales Order count |
| **Form** | Full record detail with Notes tab, Comments tab, and Chatter |
| **Pivot** | Cross-table analysis by Customer × Gender, measuring Age and Sales Orders |

### Model Fields

| Field | Type | Notes |
|---|---|---|
| Name | Char | Required |
| Gender | Selection | Male / Female |
| Country | Many2one | Links to `res.country` |
| Birth Date | Date | |
| Age | Float | Computed from Birth Date |
| Tags | Many2many | Links to `res.partner.category` |
| Customer | Many2one | Required — links to `res.partner` |
| No. of Sales Orders | Float | Computed from linked customer's sales |
| Notes | HTML | Rich text editor |
| Comments | Char | Plain text |

---

## 🔐 Security

Access to the entire Digizilla application is restricted to the `Digizillians` group:

- Users **not** in this group will not see the app in the menu
- Direct URL access will be redirected
- The report action is also restricted to the same group
- Group is defined under the custom **Digizilla** module category

---



## 📝 License

This module is licensed under the **LGPL-3** (GNU Lesser General Public License v3).

---

## 👤 Author

**Ahmed Nashaat**
