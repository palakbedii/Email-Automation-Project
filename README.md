# 📧 Email Automation and Scheduling System

An Email Automation System developed during my internship at **C-DOT (Centre for Development of Telematics)**.

The application allows users to schedule emails, manage reusable templates, monitor email status in real time, and visualize scheduled emails using an interactive calendar.

---

## 🚀 Features

### 📩 Email Scheduling
- Schedule emails for a future date and time
- Send emails through Gmail SMTP
- Automatic email delivery using a background scheduler

### 📝 Template Management
- Create new email templates
- Edit existing templates
- Delete templates
- Search templates instantly
- Reuse templates while composing emails

### 📊 Dashboard
- Total Emails
- Scheduled Emails
- Sent Emails
- Failed Emails
- Real-time statistics

### 📅 Calendar View
- Interactive calendar using FullCalendar.js
- View scheduled emails by date
- Click events to see email details

### 📜 Email Tracking
- View all scheduled emails
- View sent emails
- View failed emails
- Display error messages for failed emails

### 🔒 Security
- SMTP credentials stored securely
- Password encryption using Fernet Cryptography

---

# 🛠 Tech Stack

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Jinja2 Templates
- FullCalendar.js

## Backend
- Flask
- FastAPI
- Python

## Database
- SQLite

## Email Service
- Gmail SMTP

---

# 📂 Project Structure

```
EMAIL AUTOMATION PROJECT
│
├── FRONTEND
│   ├── static
│   │   ├── css
│   │   ├── js
│   │   └── images
│   │
│   ├── templates
│   │   ├── dashboard.html
│   │   ├── compose.html
│   │   ├── calendar.html
│   │   ├── email_templates.html
│   │   ├── sent.html
│   │   ├── scheduled.html
│   │   └── failed.html
│   │
│   └── app.py
│
├── BACKEND
│   ├── api.py
│   ├── database.py
│   ├── scheduler.py
│   ├── smtp.py
│   ├── security.py
│   ├── models.py
│   └── emails.db
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/palakbedii/Email-Automation-Project.git
```

```bash
cd Email-Automation-Project
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Start FastAPI Backend

```bash
uvicorn api:app --reload
```

---

## 5. Start Flask Frontend

```bash
python app.py
```

---

## 6. Open Browser

```
http://127.0.0.1:5000
```

---

# 📦 Database

SQLite is used to store:

- Scheduled emails
- Email status
- Email templates
- SMTP configuration

---

# 🔄 Workflow

```
User
   │
   ▼
Compose Email
   │
   ▼
Choose Template
   │
   ▼
Schedule Email
   │
   ▼
SQLite Database
   │
   ▼
Scheduler
   │
   ▼
SMTP Server
   │
   ▼
Recipient
```

---

# 📸 Screenshots

Will add screenshots here, once the project is completed.

Example:

```
screenshots/
│
├── dashboard.png
├── compose.png
├── calendar.png
├── templates.png
├── scheduled.png
├── sent.png
└── failed.png
```

Then include them:

```md
## Dashboard

![Dashboard](screenshots/dashboard.png)

## Calendar

![Calendar](screenshots/calendar.png)
```

---

# 🎯 Future Improvements

- Multiple SMTP accounts
- Attachment support
- Rich text editor
- Recurring emails
- Email analytics
- User authentication
- Docker deployment
- Cloud database support
- Email open/click tracking
- Dark mode

---

# 📚 Learning Outcomes

This project helped me gain practical experience with:

- Flask
- FastAPI
- REST APIs
- SQLite
- Background Scheduling
- SMTP Email Automation
- Bootstrap
- FullCalendar.js
- CRUD Operations
- API Integration
- MVC Architecture
- Git & GitHub

---

# 👩‍💻 Author

**Palak Bedi**

Third-Year Computer Science Engineering Student @GGSIPU

Built as part of my internship project at **C-DOT (Centre for Development of Telematics).**

---

# 📄 License

This project is intended for educational and internship purposes.
