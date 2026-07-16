email_templates = [

    {
        "id": 1,
        "name": "Interview Invitation",
        "subject": "Interview Invitation - {{company}}",
        "body": """Dear {{name}},

We are pleased to invite you for an interview for the position of {{position}} at {{company}}.

Your interview has been scheduled on {{date}} at {{time}}. Kindly report at the mentioned venue or join using the meeting link shared with this email.

We look forward to meeting you and wish you the very best.

Regards,
HR Team""",
        "last_edited": "8 July 2026",

        "fields":[
            "name",
            "company",
            "position",
            "date",
            "time"
        ]
    },

    {
        "id": 2,
        "name": "Offer Letter",
        "subject": "Offer Letter",
        "body": """Dear {{name}},

Congratulations!

We are delighted to offer you the position of {{position}} at {{company}}.

Your skills and experience impressed us greatly, and we are excited to see the impact you will make on the [Department Name] team.

Your joining date is {{joining_date}}.

Please find the attached offer letter containing your employment details, compensation package, and onboarding instructions.

We are excited to welcome you to our team and wish you a successful career with us.

Regards,
HR Department""",
        "last_edited": "10 July 2026",

        "fields":[
            "name",
            "company",
            "position",
            "joining_date"
        ]
    },

    {
        "id": 3,
        "name": "Welcome Email",
        "subject": "Welcome to {{company}}",
        "body": """Dear {{name}},

Welcome to {{company}}!

We are thrilled to have you join our team. We hope your journey with us is filled with learning, growth, and exciting opportunities.

Please complete your onboarding formalities before {{joining_date}}. If you require any assistance, our HR team is always happy to help.

We wish you great success in your new role.

Warm Regards,
HR Team""",
        "last_edited": "4 July 2026",

        "fields":[
            "name",
            "company",
            "joining_date"
        ]
    },

    {
        "id": 4,
        "name": "Meeting Reminder",
        "subject": "Meeting Reminder",
        "body": """Dear {{name}},

This is a friendly reminder regarding your upcoming meeting.

Meeting Topic:
{{meeting_title}}

Date:
{{date}}

Time:
{{time}}

Please ensure your availability and join the meeting a few minutes before the scheduled time.

We appreciate your punctuality.

Thank you,
{{company}}""",
        "last_edited": "1 July 2026",

        "fields":[
            "name",
            "meeting_title",
            "date",
            "time",
            "company"
        ]
    },

    {
        "id": 5,
        "name": "Happy Retirement",
        "subject": "Happy Retirement!",
        "body": """Dear {{name}},

Congratulations on your retirement!

Your dedication, professionalism, and years of service have been an inspiration to everyone at {{company}}.

As you begin this exciting new chapter, we wish you happiness, good health, and countless memorable moments with your loved ones.

Thank you for everything you have contributed to our organization.

With Best Wishes,
{{company}} Team""",
        "last_edited": "3 July 2026",

        "fields":[
            "name",
            "company"
        ]
    },

    {
        "id": 6,
        "name": "Event Invitation",
        "subject": "You're Invited: {{event_name}}",
        "body": """Dear {{name}},

Thank you for registering for {{event_name}}.

We are pleased to confirm your registration. Here are the event details:

Date: {{date}}
Time: {{time}}
Venue: {{venue}}

We look forward to welcoming you. If you have any questions, feel free to contact our support team.

Thank you, and see you at the event!

With Regards,
Event Management Team""",
        "last_edited": "11 July 2026",

        "fields":[
            "name",
            "event_name",
            "venue",
            "date",
            "time"
        ]
    }

]