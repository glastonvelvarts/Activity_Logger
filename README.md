# Activity Logger

A web application for logging user activities and fetching activity logs and statistics. Built using **Flask** for the backend, **React** for the frontend, and **PostgreSQL** for database management.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Overview

This project provides a user activity logger where users can log their activities, view their logged activities, and retrieve activity statistics over a specific date range.

## Features

- **Log Activity**: Allows users to log activities with a timestamp and optional metadata.
- **View Logs**: Fetches logged activities for a specific user.
- **Fetch Stats**: Retrieves activity statistics such as the most frequent activity and user activity counts over a specified date range.

## Tech Stack

- **Backend**: Flask, Flask-SQLAlchemy, psycopg2
- **Frontend**: React, CSS (Styled Components)
- **Database**: PostgreSQL
- **Deployment**: Docker, Docker Compose

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/activity-logger.git
   cd activity-logger
