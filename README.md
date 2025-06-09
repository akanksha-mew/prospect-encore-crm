# prospect-encore-crm
A terminal-based CRM solution for car dealerships, designed to manage customer prospects, streamline sales data, and provide actionable insights through role-based access.

🔧 Tech Stack
Language: Python
Database: MySQL
Interface: Command-Line Interface (CLI)
Libraries Used: pymysql, matplotlib (for analysis/plotting)

💡 Features
🔐 Authentication & Role-Based Access
Admin:
Create & manage employee accounts (Admin/Monitor)
Activate/Deactivate users
Change any password
Access sales analysis dashboards

Monitor:
Add, update, view, and search customer prospect data
Change own password
Access data analysis tools

📊 Prospect Management
Insert new customer leads with car preferences and visit details
Update prospect info (phone, model, color, priority)
Search leads by ID or priority
View all prospects in a tabulated format

📈 Data Analysis
Visual analysis of bookings by:
Car model
Color preference
Priority level
Visit day
Income group
Generates sales trends and helps in business decision-making

🔒 Secure Database Operations
Uses parameterized SQL queries to prevent SQL injection
Relies on pymysql for all database interactions

🗂️ File Structure
common.py – Shared functions for user/prospect management and DB operations
admin.py – Admin dashboard logic
monitor.py – Monitor dashboard logic
saleanalysis.py – Handles data analysis and visualizations
pencoreanalysis.py – Main entry point
DB schema.sql – (Optional: Include DB setup script if available)

🚀 Getting Started
Set up a MySQL database named prospencore.
Create tables employees and prospect with relevant schema.
Clone the repo and run pencoreanalysis.py.
Use Admin credentials to begin.

📌 Future Enhancements
Web-based UI using Flask or Django
Export reports in CSV/PDF
Email alerts for high-priority prospects
