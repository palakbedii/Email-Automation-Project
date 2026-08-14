# 📧 Email Automation and Scheduling System

A web-based **Email Automation and Scheduling System** developed as an industrial internship project at the **Centre for Development of Telematics (C-DOT)**.

The system provides a centralized web interface for composing, scheduling, sending, and managing emails. It supports reusable email templates, SMTP configuration, file attachments, recurring emails, calendar-based email tracking, delivery-status management, and automated infrastructure monitoring reports.

---

## 🏢 Project Information

| Category               | Details                                              |
| ---------------------- | ---------------------------------------------------- |
| **Project Title**      | Email Automation and Scheduling System               |
| **Organization**       | Centre for Development of Telematics (C-DOT)         |
| **Project Domain**     | Web Development / Backend Development                |
| **Frontend Framework** | Flask                                                |
| **Backend Framework**  | FastAPI                                              |
| **Database**           | SQLite                                               |
| **Email Service**      | Gmail SMTP                                           |
| **Scheduling**         | Custom Background Scheduler / APScheduler dependency |
| **Calendar**           | FullCalendar.js                                      |
| **UI Framework**       | Bootstrap + AdminLTE                                 |
| **Monitoring**         | Prometheus + Windows Exporter                        |
| **Report Generation**  | OpenPyXL                                             |
| **Version Control**    | Git & GitHub                                         |
| **Language**           | Python, HTML5, CSS3, JavaScript                      |

---

# 📌 Project Overview

The **Email Automation and Scheduling System** is a web-based application designed to simplify and automate email communication.

The system allows users to:

* Log in securely to the application
* Manage reusable email templates
* Compose emails using existing templates
* Configure SMTP sender settings
* Send emails immediately
* Schedule emails for a future date and time
* Schedule recurring emails
* Attach files to emails
* View scheduled emails
* View sent emails
* View failed emails
* Retry failed email deliveries
* Visualize email activity through a calendar
* Search and filter email history
* Monitor system resources using Prometheus
* Generate automated Excel monitoring reports
* Attach monitoring reports to scheduled emails
* Archive generated monitoring reports

The project combines **web development, REST API development, database management, email automation, scheduling, monitoring, and automated reporting** into a single application.

---

# 🎯 Objectives

The major objectives of the project are:

1. To develop a centralized web-based email automation platform.
2. To reduce repetitive manual email-sending tasks.
3. To provide reusable email templates.
4. To allow users to schedule emails for specific dates and times.
5. To support recurring email delivery.
6. To provide attachment support.
7. To maintain records of scheduled, sent, and failed emails.
8. To provide a calendar-based visualization of email activity.
9. To securely manage SMTP configuration.
10. To integrate infrastructure monitoring with automated email reporting.
11. To generate Excel reports containing CPU, RAM, disk, node name, and IP information.
12. To provide a scalable foundation for future automation and monitoring features.

---

# ✨ Key Features

## 🔐 1. Login & Authentication

The application provides a login interface for accessing the system.

The authentication workflow includes:

* Login page
* Credential validation
* Session handling
* Protected application pages
* Logout functionality

```text
User
  ↓
Login
  ↓
Credential Validation
  ↓
Session Created
  ↓
Application Dashboard
```

---

# 📊 2. Dashboard

The dashboard provides a centralized overview of email activity.

It includes statistics such as:

* Total emails
* Scheduled emails
* Sent emails
* Failed emails
* Template count

The dashboard retrieves live counts from the FastAPI backend.

### Dashboard capabilities

* Live email statistics
* Summary cards
* Quick navigation
* Email activity overview
* Responsive AdminLTE interface

---

# 📝 3. Email Template Management

The Email Templates module allows users to create and manage reusable email templates.

### Supported operations

* Create template
* View templates
* Edit template
* Delete template
* Search templates
* Select a template while composing an email

When a template is selected during email composition, its subject and body can be automatically populated into the compose form.

This reduces repetitive work and ensures consistency across recurring communications.

---

# ✉️ 4. Compose Mail

The Compose Mail module is the primary interface for preparing emails.

Users can:

* Select an existing template
* Enter recipients
* Enter/edit subject
* Compose email content
* Add attachments
* Select a scheduled date and time
* Configure recurring delivery
* Enable automatic monitoring-report attachment
* Send immediately
* Schedule the email

---

# 📎 5. File Attachments

The system supports file attachments for outgoing emails.

The attachment workflow includes:

```text
Select File
    ↓
Upload
    ↓
Store in Upload Directory
    ↓
Associate with Email
    ↓
MIME Attachment
    ↓
SMTP Delivery
```

Attachments are handled through:

```text
BACKEND/attachments_manager.py
```

and uploaded files are maintained through the frontend upload directory.

---

# 🔁 6. Recurring Email Scheduling

The application supports recurring email workflows.

Available recurrence options include:

* Every Hour
* Every Day
* Every Week
* Every Month

Recurring emails can be configured with appropriate scheduling conditions such as an end date.

The scheduler determines when the next occurrence should be processed.

```text
Initial Email
     ↓
Email Sent
     ↓
Calculate Next Occurrence
     ↓
Create / Update Next Schedule
     ↓
Wait
     ↓
Send Next Email
```

---

# 📅 7. Scheduled Calendar

The project integrates **FullCalendar.js** to provide a visual calendar representation of email activity.

The calendar displays:

* Scheduled emails
* Sent emails
* Failed emails

This provides users with a convenient way to understand email activity based on date and time.

### Calendar flow

```text
SQLite Database
      ↓
FastAPI Calendar API
      ↓
Calendar Events
      ↓
FullCalendar.js
      ↓
Visual Calendar
```

---

# 📋 8. Scheduled Email Page

The Scheduled Email page displays emails that are waiting to be processed.

Information can include:

* Recipient
* Subject
* Scheduled date/time
* Recurrence information
* Attachment information
* Current status

---

# 📤 9. Sent Email Page

The Sent Email page provides a history of successfully delivered emails.

It helps users review previously processed email records.

---

# ❌ 10. Failed Email Page

The Failed Email page maintains records of unsuccessful email deliveries.

It can display:

* Recipient
* Subject
* Date/time
* Failure status
* Error information

The system also supports retry functionality as part of the application's email-history and failure-handling workflow.

---

# ⚙️ 11. SMTP Settings

The SMTP Settings page allows users to configure the sender account used for email delivery.

Configuration may include:

* SMTP server
* SMTP port
* Sender email
* SMTP credentials
* Encryption/security settings

The project includes a dedicated security module for handling sensitive SMTP information.

Relevant files include:

```text
BACKEND/secret.py
BACKEND/security.py
BACKEND/smtp.py
```

> **Security Note:** Sensitive credentials and encryption keys should never be committed to a public Git repository. Production deployments should use environment variables or a dedicated secrets-management solution.

---

# 📈 12. Infrastructure Monitoring

The project contains a dedicated monitoring subsystem that integrates:

* Windows Exporter
* Prometheus
* PromQL
* Prometheus HTTP API
* Python
* OpenPyXL

The monitoring package is located at:

```text
BACKEND/monitoring/
```

It contains:

```text
monitoring/
│
├── __init__.py
├── config.py
├── metrics.py
├── prometheus_api.py
├── monitoring_service.py
└── report_generator.py
```

---

# 🖥️ Monitoring Architecture

```text
┌─────────────────────────┐
│     Windows Machine     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│    Windows Exporter     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       Prometheus        │
└────────────┬────────────┘
             │
             │ PromQL
             ▼
┌─────────────────────────┐
│  Prometheus HTTP API    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Monitoring Service      │
│        Python           │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│    Report Generator     │
│        OpenPyXL         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Excel Monitoring Report │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│    Email Attachment     │
└─────────────────────────┘
```

---

# 📊 13. Monitoring Metrics

The monitoring system collects information about the monitored machine.

The generated report contains:

| NODE NAME    | IP         |     CPU % |     RAM % |     DISK % |
| ------------ | ---------- | --------: | --------: | ---------: |
| Host Machine | IP Address | CPU Usage | RAM Usage | Disk Usage |

### CPU

CPU utilization is calculated from Prometheus CPU metrics.

### RAM

RAM usage is calculated using total and available physical memory.

```text
RAM Usage (%) =
(Total Memory - Available Memory)
-------------------------------- × 100
        Total Memory
```

### Disk

Disk utilization is calculated using total and free disk space.

### Node Information

The report also records:

* Node / Host Name
* IP Address

---

# 📑 14. Automated Excel Monitoring Report

The monitoring system generates an Excel file using **OpenPyXL**.

Reports are stored in:

```text
BACKEND/Reports/
```

A generated report follows a timestamped naming convention such as:

```text
Monitoring_Report_YYYYMMDD_HHMMSS.xlsx
```

The report contains structured monitoring data suitable for sharing through email or reviewing independently.

---

# 📧 15. Automatic Monitoring Report Attachment

One of the major integrations in the project connects the monitoring system directly with email scheduling.

When automatic monitoring-report attachment is enabled:

```text
Scheduled Email
      ↓
Scheduler Detects Due Email
      ↓
Monitoring Service Starts
      ↓
Prometheus Metrics Retrieved
      ↓
CPU / RAM / Disk Calculated
      ↓
Excel Report Generated
      ↓
Report Attached to Email
      ↓
Email Sent Through Gmail SMTP
      ↓
Email Status Updated
      ↓
Generated Report Archived
```

This allows scheduled emails to contain a **fresh monitoring report generated as part of the email-processing workflow**.

---

# 🗂️ 16. Archive Management

Generated monitoring reports can be moved to:

```text
BACKEND/Archive/
```

after successful processing.

The archive mechanism helps prevent the Reports directory from becoming cluttered with previously delivered reports.

The overall workflow is:

```text
Generate Report
      ↓
BACKEND/Reports/
      ↓
Attach to Email
      ↓
Successful Email Delivery
      ↓
Move Report
      ↓
BACKEND/Archive/
```

---

# 🛡️ 17. Monitoring Error Handling

The monitoring subsystem accounts for possible failures such as:

* Prometheus unavailable
* Connection errors
* Request timeouts
* HTTP failures
* Invalid API responses
* Empty metric results
* Missing metric values
* Invalid metric data
* Excel report-generation errors

The purpose of this handling is to prevent invalid monitoring data from being silently included in generated reports.

---

# 🏗️ System Architecture

The project follows a two-layer web application architecture.

```text
                    ┌──────────────────┐
                    │      User        │
                    │     Browser      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     Flask        │
                    │    Frontend      │
                    └────────┬─────────┘
                             │
                             │ REST API
                             ▼
                    ┌──────────────────┐
                    │     FastAPI      │
                    │     Backend      │
                    └───────┬──────────┘
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
        ┌────────┐    ┌───────────┐   ┌──────────┐
        │ SQLite │    │ Scheduler │   │   SMTP   │
        │Database│    │           │   │  Gmail   │
        └────────┘    └─────┬─────┘   └──────────┘
                            │
                            ▼
                    ┌─────────────────┐
                    │   Monitoring    │
                    │    Service      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Prometheus    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Windows Exporter│
                    └─────────────────┘
```

---

# 📂 Project Structure

The project is organized into separate frontend, backend, monitoring, configuration, database, and documentation components.

```text
EMAIL_AUTOMATION_PROJECT/
│
├── FRONTEND/                              ← Flask Application
│   │
│   ├── app.py
│   │
│   ├── templates/
│   │   ├── layout.html
│   │   │
│   │   ├── dashboard.html
│   │   ├── email_templates.html
│   │   ├── new_template.html
│   │   ├── edit_template.html
│   │   ├── compose.html
│   │   ├── calendar.html
│   │   ├── schedule.html
│   │   ├── sent.html
│   │   ├── failed.html
│   │   └── smtp_settings.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── calendar.css
│   │   │
│   │   ├── js/
│   │   │   └── email_table.js
│   │   │
│   │   ├── assets/
│   │   ├── images/
│   │   ├── plugins/
│   │   └── AdminLTE/
│   │
│   └── uploads/
│
│
├── BACKEND/                               ← FastAPI
│   │
│   ├── app.py
│   ├── attachments_manager.py
│   ├── check_db.py
│   ├── models.py
│   ├── database.py
│   ├── scheduler.py
│   ├── secret.py
│   ├── security.py
│   ├── smtp.py
│   ├── templates_api.py
│   │
│   ├── emails.db
│   ├── templates.db
│   │
│   ├── Archive/
│   ├── Reports/
│   │
│   └── monitoring/
│       │
│       ├── __init__.py
│       ├── config.py
│       ├── metrics.py
│       ├── prometheus_api.py
│       ├── monitoring_service.py
│       └── report_generator.py
│
│
├── prometheus.yml
│
├── .gitignore
│
├── notes.txt
│
├── README.md
│
└── requirements.txt
```

---

# 🧩 Project Portfolio

The application consists of the following major pages and modules:

```text
Login
  ↓
Dashboard
  ↓
Email Templates
  ↓
Compose Mail
  ↓
Scheduled Calendar
  ↓
Scheduled Emails
  ↓
Sent Emails
  ↓
Failed Emails
  ↓
SMTP Settings
  ↓
Logout
```

---

# 📱 Application Modules

| Module                 | Description                                  |
| ---------------------- | -------------------------------------------- |
| **Login**              | Authentication and session handling          |
| **Dashboard**          | Email statistics and live counts             |
| **Email Templates**    | Template CRUD operations                     |
| **Compose Mail**       | Compose, schedule, and send emails           |
| **Attachments**        | Upload and manage email attachments          |
| **Scheduled Calendar** | Visualize Scheduled, Sent, and Failed emails |
| **Scheduled Email**    | View pending/scheduled emails                |
| **Sent Email**         | View successfully sent emails                |
| **Failed Email**       | View failed email deliveries                 |
| **SMTP Settings**      | Configure sender account                     |
| **Monitoring**         | Collect system metrics                       |
| **Reports**            | Store generated Excel monitoring reports     |
| **Archive**            | Store processed generated reports            |
| **Logout**             | End authenticated session                    |

---

# 🛠️ Technology Stack

## HTML5

Used to structure the application's web pages and forms.

## CSS3

Used for custom styling and UI improvements.

## JavaScript

Used for:

* Dynamic page behavior
* API requests
* Email table operations
* Calendar integration
* UI interactions

## Bootstrap

Provides responsive layouts and reusable UI components.

## AdminLTE

Provides the primary dashboard interface, including:

* Sidebar
* Navbar
* Cards
* Tables
* Navigation
* Responsive layout

## Flask

Flask is used for the frontend web application.

It handles:

* Page rendering
* Routes
* Sessions
* User interface
* Communication with FastAPI

## FastAPI

FastAPI provides the backend REST API.

It handles:

* Email operations
* Template operations
* Database interactions
* Dashboard statistics
* Calendar data
* Backend services

## SQLite

SQLite is used as the lightweight relational database.

The project currently maintains:

```text
emails.db
templates.db
```

## Gmail SMTP

Gmail SMTP is used for actual email delivery.

The application constructs MIME email messages and sends them through the configured SMTP server.

## Scheduler

The scheduler continuously checks stored email records and processes emails whose scheduled time has been reached.

It also supports recurring email processing.

## FullCalendar.js

FullCalendar.js provides the interactive calendar interface for email events.

## Prometheus

Prometheus collects and stores system metrics exposed by the Windows Exporter.

## Windows Exporter

Windows Exporter exposes Windows operating-system metrics in a format that can be scraped by Prometheus.

## OpenPyXL

OpenPyXL is used to create and format Excel monitoring reports.

## Git

Git is used for:

* Version control
* Branch management
* Commit history
* Tracking project changes

## GitHub

GitHub is used to host and manage the project repository.

---

# 🔌 API Design

The FastAPI backend provides REST endpoints for communicating with the frontend.

Important application endpoints include:

| Method     | Endpoint            | Purpose                       |
| ---------- | ------------------- | ----------------------------- |
| `GET`      | `/dashboard`        | Retrieve dashboard statistics |
| `GET`      | `/calendar/events`  | Retrieve calendar events      |
| `GET`      | `/emails/scheduled` | Retrieve scheduled emails     |
| `GET`      | `/emails/sent`      | Retrieve sent emails          |
| `GET`      | `/emails/failed`    | Retrieve failed emails        |
| `POST`     | `/emails/send_now`  | Send email immediately        |
| `GET/POST` | `/templates`        | Retrieve/create templates     |
| `PUT`      | `/templates/{id}`   | Update template               |
| `DELETE`   | `/templates/{id}`   | Delete template               |
| `GET`      | `/templates/search` | Search templates              |

> Endpoint availability may evolve as development continues.

---

# 🗄️ Database Structure

The application currently uses two SQLite databases:

```text
BACKEND/
├── emails.db
└── templates.db
```

### Email Database

The email database maintains information associated with:

* Recipients
* Subject
* Body
* Schedule time
* Email status
* Error information
* Attachments
* Recurrence information

### Template Database

The template database stores reusable email templates.

Typical template information includes:

* Template ID
* Template name
* Subject
* Body
* Template metadata

---

# 🔄 Email Scheduling Workflow

```text
User
 ↓
Compose Email
 ↓
Select Template
 ↓
Add Recipient
 ↓
Add Subject / Body
 ↓
Add Attachment
 ↓
Set Date & Time
 ↓
Set Recurrence (Optional)
 ↓
Save Email
 ↓
SQLite Database
 ↓
Scheduler
 ↓
Check Current Time
 ↓
Is Email Due?
 ├── No → Continue Checking
 │
 └── Yes
       ↓
  Process Email
       ↓
  Generate Monitoring Report
       ↓
  Attach Files
       ↓
  Gmail SMTP
       ↓
  Update Status
       ↓
  Archive Generated Report
```

---

# 🧪 Testing

The project includes testing of different parts of the application, particularly the monitoring and reporting subsystem.

Monitoring-related test files include:

```text
BACKEND/
│
├── test_prometheus.py
├── test_monitoring_service.py
├── test_report_generator.py
└── test_monitoring_attachment.py
```

Testing areas include:

* Prometheus connectivity
* PromQL queries
* Metric extraction
* Metric calculation
* Empty/invalid metric handling
* Monitoring service execution
* Excel report generation
* Monitoring report attachment
* Scheduler behavior
* Email delivery
* Failure handling
* Recurring email processing

---

# 🐛 Challenges Addressed

During development, several technical challenges were encountered.

### 1. SMTP Authentication

Gmail requires appropriate authentication configuration for SMTP-based applications.

### 2. Scheduled Email Accuracy

The scheduler needs to compare stored schedule times with the current system time accurately.

### 3. Recurring Emails

Recurring emails require calculation of subsequent execution times while avoiding unintended duplicate deliveries.

### 4. Attachment Handling

Attachments require correct file paths, MIME encoding, and cleanup/archive handling.

### 5. Frontend–Backend Communication

The Flask frontend communicates with the FastAPI backend through HTTP requests.

### 6. Calendar Synchronization

Calendar events must accurately represent the current email status stored in the database.

### 7. Prometheus Integration

The monitoring service must correctly query Prometheus and interpret its API responses.

### 8. Invalid or Missing Metrics

Prometheus may return empty or unexpected metric results, requiring validation before report generation.

### 9. Automated Report Generation

The Excel report must be generated dynamically using current monitoring values.

### 10. Report Archiving

Generated reports need to be moved into the Archive directory after successful processing to prevent unnecessary accumulation.

---

# 🚧 Current Development Status

This project is being developed incrementally as part of an industrial internship.

## Implemented / Integrated

* [x] Login interface
* [x] Session handling
* [x] Dashboard
* [x] Email template CRUD
* [x] Template search
* [x] Template selection during composition
* [x] Send Now
* [x] Scheduled emails
* [x] Sent email records
* [x] Failed email records
* [x] Calendar integration
* [x] SMTP configuration
* [x] File attachments
* [x] Recurring email workflow
* [x] SMTP credential security
* [x] Monitoring module
* [x] Prometheus integration
* [x] Windows Exporter integration
* [x] CPU monitoring
* [x] RAM monitoring
* [x] Disk monitoring
* [x] Node/IP information
* [x] Excel monitoring report
* [x] Monitoring report attachment
* [x] Reports directory
* [x] Archive workflow
* [x] Monitoring error handling
* [x] Monitoring test scripts

## 🔄 Polish / Ongoing Improvements

* [ ] Complete regression testing
* [ ] Extensive failure-path testing
* [ ] Improve email-history search and filtering
* [ ] Retry failed sends
* [ ] Loading spinners
* [ ] User-friendly alerts
* [ ] UI animations
* [ ] Search and pagination refinement
* [ ] Responsive UI refinement
* [ ] Excel formatting polish
* [ ] Logging cleanup
* [ ] Final project structure cleanup
* [ ] Complete README/documentation
* [ ] End-to-end demonstration

---

# 🔮 Future Scope

The system can be extended significantly in future versions.

## 📧 Advanced Email Features

* Multiple SMTP providers
* Microsoft Outlook / Office 365 support
* Rich Text Editor
* HTML email builder
* Email tracking
* Open and click analytics
* Advanced attachment scheduling

## 🤖 Artificial Intelligence

* AI-generated email templates
* AI-generated subject lines
* Tone adjustment
* Automatic email summarization
* Personalized email generation

## 👥 Authentication

* Role-based authentication
* Admin and user roles
* Multi-user support
* User-specific templates
* User-specific SMTP configurations

## 📊 Analytics

* Email analytics dashboard
* Historical email statistics
* Delivery-rate analysis
* Failure-rate analysis
* Monitoring trend graphs

## 🖥️ Advanced Monitoring

* Network monitoring
* Process monitoring
* Service monitoring
* Threshold-based alerts
* Historical infrastructure metrics
* Multi-node monitoring

## ⚡ Scalable Architecture

Future versions could use:

* PostgreSQL
* Redis
* Celery
* Docker
* Kubernetes
* Cloud deployment
* Distributed task queues

---

# 📚 Learning Outcomes

This project provided practical experience in:

* Full-stack web development
* Backend API development
* REST API design
* Python programming
* Flask
* FastAPI
* SQLite
* Database operations
* HTML
* CSS
* JavaScript
* Bootstrap
* AdminLTE
* FullCalendar.js
* SMTP
* MIME email construction
* Email scheduling
* Recurring jobs
* File handling
* Encryption
* Prometheus
* PromQL
* Windows Exporter
* Monitoring systems
* Excel report generation
* OpenPyXL
* Error handling
* Debugging
* Git
* GitHub
* Software documentation

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/palakbedii/Email-Automation-Project.git
cd Email-Automation-Project
```

## 2. Create a Virtual Environment

### Windows

```powershell
python -m venv venv
```

Activate:

```powershell
.\venv\Scripts\Activate.ps1
```

Alternatively:

```cmd
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

The application contains two primary services:

```text
Flask Frontend
      ↕
FastAPI Backend
```

## Start the FastAPI Backend

```bash
cd BACKEND
uvicorn app:app --reload
```

## Start the Flask Frontend

Open another terminal:

```bash
cd FRONTEND
python app.py
```

Then open the frontend in your browser using the configured Flask port.

---

# 📈 Monitoring Setup

The monitoring subsystem requires:

```text
Windows Exporter
        ↓
Prometheus
        ↓
prometheus.yml
        ↓
Monitoring Service
```

The repository contains:

```text
prometheus.yml
```

Prometheus should be configured to scrape the Windows Exporter endpoint.

After starting Prometheus, verify that the Windows Exporter target is available and reporting an **UP** status.

---

# 📊 Generate Monitoring Report

Monitoring components can be tested independently from the backend directory.

Example:

```bash
cd BACKEND
python test_prometheus.py
```

```bash
python test_report_generator.py
```

```bash
python test_monitoring_service.py
```

```bash
python test_monitoring_attachment.py
```

Generated reports are stored in:

```text
BACKEND/Reports/
```

---

# 🔒 Security

Sensitive information must not be committed to GitHub.

Do not expose:

```text
SMTP passwords
Encryption keys
API keys
Authentication secrets
Tokens
Private credentials
```

For production deployment, use:

* Environment variables
* `.env` files excluded through `.gitignore`
* Secret-management services
* Secure deployment configuration

The files:

```text
BACKEND/secret.py
BACKEND/security.py
```

are associated with the project's security implementation and should be handled carefully when publishing the repository.

---

# 📁 Important Directories

| Directory             | Purpose                                   |
| --------------------- | ----------------------------------------- |
| `FRONTEND/templates/` | HTML/Jinja templates                      |
| `FRONTEND/static/`    | CSS, JavaScript, AdminLTE and assets      |
| `FRONTEND/uploads/`   | Uploaded email attachments                |
| `BACKEND/`            | FastAPI backend and core services         |
| `BACKEND/Archive/`    | Archived generated reports                |
| `BACKEND/Reports/`    | Generated monitoring reports              |
| `BACKEND/monitoring/` | Prometheus monitoring and Excel reporting |
| Root directory        | Project configuration and documentation   |

---

# 📷 Screenshots

Screenshots can be added to the repository using a dedicated `screenshots/` directory.

Recommended screenshots:

```text
screenshots/
│
├── login.png
├── dashboard.png
├── email-templates.png
├── new-template.png
├── edit-template.png
├── compose.png
├── schedule.png
├── calendar.png
├── sent.png
├── failed.png
├── smtp-settings.png
├── prometheus.png
├── monitoring-report.png
└── monitoring-email.png
```

Example:

```markdown
## Login

![Login](screenshots/login.png)

## Dashboard

![Dashboard](screenshots/dashboard.png)

## Compose Mail

![Compose Mail](screenshots/compose.png)

## Calendar

![Calendar](screenshots/calendar.png)

## Monitoring Report

![Monitoring Report](screenshots/monitoring-report.png)
```

---

# 📖 References

* Flask Documentation — https://flask.palletsprojects.com/
* FastAPI Documentation — https://fastapi.tiangolo.com/
* Bootstrap Documentation — https://getbootstrap.com/
* AdminLTE Documentation — https://adminlte.io/
* SQLite Documentation — https://sqlite.org/docs.html
* FullCalendar Documentation — https://fullcalendar.io/docs
* Prometheus Documentation — https://prometheus.io/docs/
* Windows Exporter — https://github.com/prometheus-community/windows_exporter
* OpenPyXL Documentation — https://openpyxl.readthedocs.io/
* Git Documentation — https://git-scm.com/doc
* GitHub Documentation — https://docs.github.com/

---

# 👩‍💻 Author

**Olive**

Computer Science Engineering Student

Industrial Internship Project
**Centre for Development of Telematics (C-DOT)**

---

# 📌 Project Status

**🚧 Under Active Development**

This repository represents the ongoing development of the Email Automation and Scheduling System. Features and implementation details may continue to evolve as development, testing, optimization, and deployment work progress.

---

## ⭐ Repository

**Email Automation and Scheduling System**

GitHub:

https://github.com/palakbedii/Email-Automation-Project
