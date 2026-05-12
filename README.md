# Digizilla


A custom Odoo addon that introduces the **Digizilla** model — a complete record management application with form, kanban, list, and pivot views, PDF reporting, role-based access control, and a custom JavaScript enhancement.

-----
## Screenshots

### Form View
<p align="center">
<img width="80%"  alt="tr" src="https://github.com/user-attachments/assets/299561d1-59bd-43b4-8dae-333c4c246a82" />


</p>


### List View
<p align="center">
 <img width="80%" alt="list" src="https://github.com/user-attachments/assets/c27a989d-28eb-42d0-9c07-3d9e3d05d2c2" />

</p>

### Piviot & Kanban Views
<p align="center">
<img width="48%" height="500" alt="yu" src="https://github.com/user-attachments/assets/797c178c-ac6f-46ce-a13a-af4bb1f96455" />

<img width="48%" height="316" alt="TT" src="https://github.com/user-attachments/assets/aa47d47a-ad50-4c80-b227-e008e542afef" />


</p>





---
## Demo
Demo: [View Demo](https://drive.google.com/file/d/1yS9de181yWZM2Xdh96U4kiOGJb82XDrU/view?usp=sharing)

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
