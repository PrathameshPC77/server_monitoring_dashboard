# Server Monitoring Dashboard
A web-based Server Monitoring Dashboard backend built using Django and Django REST Framework.
It provides APIs to monitor server statistics like CPU, memory, disk usage, and network-level metrics.

![Dashboard Screenshot](https://github.com/PrathameshPC77/server_monitoring_dashboard/blob/main/output.png) 

A lightweight Django-based web application for monitoring server health metrics with SQLite database.
## Live Demo
[Visit Live App](https://server-monitoring-dashboard-gogy.onrender.com/) 

## Key Features
✅ Real-time alert tracking (Critical/Medium/Low)  
✅ Interactive resource usage charts (CPU, RAM, Disk)  
✅ Network traffic visualization  
✅ Server inventory management  
✅ Mock data generation system  

## Technology Stack
- **Backend**: Django 5.2, Django REST Framework
- **Database**: SQLite (no PostgreSQL required)
- **Frontend**: Django Templates + Bootstrap 
- **Deployment**: Render (Free Tier)
- **Others:** Gunicorn, Whitenoise (for static files)

## Project Structure
    server_monitoring_dashboard/
    ├── backend/              # Django project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── monitor/               # Django app for monitoring
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── serializers.py
    │   ├── management/
    │   │   └── commands/
    │   │       └── generate_mock_data.py  # Custom management command
    |   ├── templates/            
    │   └── admin.py
    ├── staticfiles/           # Collected static files
    ├── manage.py              # Django management script
    ├── requirements.txt       # Python dependencies
    └── README.md              # Project documentation

## 📁 Key Files

- `monitor/models.py`
    Defines the `Server` and `Metrics` models used to store server and performance data.
- `generate_mock_data.py`
    Custom Django management command to generate mock server and metric data for testing purposes.
- `dashboard.html`
    Main HTML template for the dashboard, including visual charts to display metrics.
- `settings.py`
    Django settings file, configured with Whitenoise for serving static files.

## Setup Instructions
1. Clone the repository
   ```bash
   git clone https://github.com/PrathameshPC77/server_monitoring_dashboard.git
   cd server_monitoring_dashboard

2. Create virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   
3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   
4. Apply Migrations
   ```bash
   python manage.py migrate

5. Generate Mock Server Monitoring Data
   ```bash
   python manage.py generate_mock_data # This command will seed the database with random server stats for demo/testing purposes.

6. Run Development Server
   ```bash
   python manage.py runserver

## Build & Deployment (Render.com)
- Push code to GitHub
- Create new Web Service on Render
- Configure:
  - Build Command: ./build.sh
  - Start Command: gunicorn backend.wsgi:application

1. Build Command:
   ```bash
    pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python manage.py generate_mock_data

2. Start Command:
   ```bash
    gunicorn backend.wsgi

3. Important:
- The generate_mock_data management command is run during the build phase to populate mock server data.
- Static files are served using Whitenoise.

## Customization Guide
- Modify Alert Thresholds
    Edit monitor/models.py:
   ```bash
  class ServerMetrics(models.Model):
      ALERT_CHOICES = [
          ('critical', 'CPU > 90%'),  # Change thresholds here
          ('medium', 'CPU > 80%'),
          ('low', 'CPU > 70%')
   ]

- Add More Metrics
  1. Extend ServerMetrics model
  2. Update generate_mock_data.py
  3. Add new charts to dashboard.html

## Features
- Monitor:
  - CPU Usage
  - RAM Usage
  - Disk Usage
  - Network Traffic 

- Seed random monitoring data (for testing/demo)
- RESTful API architecture

## Future Improvements
- Real-time updates with Django Channels and WebSockets
- User authentication and dashboards
- Alerts and Notifications (Email, Slack)
- Admin Panel customization
- Production-grade deployment with PostgreSQL & Redis
