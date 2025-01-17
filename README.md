Activity Logger
A web application for logging user activities and fetching activity logs and statistics. Built using Flask for the backend, React for the frontend, and PostgreSQL for database management.

Table of Contents
Overview
Features
Tech Stack
Installation
Usage
API Endpoints
License
Overview
This project provides a user activity logger where users can log their activities, view their logged activities, and retrieve activity statistics over a specific date range.

Features
Log Activity: Allows users to log activities with a timestamp and optional metadata.
View Logs: Fetches logged activities for a specific user.
Fetch Stats: Retrieves activity statistics such as the most frequent activity and user activity counts over a specified date range.
Tech Stack
Backend: Flask, Flask-SQLAlchemy, psycopg2
Frontend: React, CSS (Styled Components)
Database: PostgreSQL
Deployment: Docker, Docker Compose
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/activity-logger.git
cd activity-logger
Set up the backend and frontend dependencies:

Backend: Install Python dependencies.

bash
Copy
Edit
cd backend
pip install -r requirements.txt
Frontend: Install React dependencies.

bash
Copy
Edit
cd frontend
npm install
Set up the database:

Ensure you have PostgreSQL installed or use Docker to run a PostgreSQL container.
Create a database named flask_database with the appropriate user credentials (postgres:root).
Run the app:

Backend: Start the Flask backend server.

bash
Copy
Edit
cd backend
python app.py
Frontend: Start the React development server.

bash
Copy
Edit
cd frontend
npm start
Open your browser and go to http://localhost:5000 to view the application.

Usage
Log Activity: Submit your user ID and activity to log it.
Fetch Logs: Click the "Fetch Logs" button to retrieve logs for a specific user.
Fetch Stats: Click the "Fetch Stats" button to get activity statistics like the most frequent activity and user activity count.
API Endpoints
POST /logs: Logs a new activity for a user.

Request body:
json
Copy
Edit
{
  "user_id": "string",
  "activity": "string"
}
GET /logs/{user_id}: Fetches all logs for a specific user within the last 7 days.

Query parameters:
activity: (Optional) Filter by activity type.
Example:
bash
Copy
Edit
GET /logs/123?activity=login
GET /logs/stats: Retrieves activity statistics between two dates.

Query parameters:
start: Start date in ISO 8601 format (YYYY-MM-DDTHH:MM:SS).
end: End date in ISO 8601 format (YYYY-MM-DDTHH:MM:SS).
Example:
sql
Copy
Edit
GET /logs/stats?start=2023-01-01T00:00:00&end=2023-12-31T23:59:59
License
This project is licensed under the MIT License.
