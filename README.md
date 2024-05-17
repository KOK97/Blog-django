# My Django Project

This is a sample Django project that includes instructions for setting up a virtual environment, installing dependencies, and running the development server.

## Project Description

This project is a social blog web application where users can post blogs. Each blog post must be approved by an admin before being published. The website also includes functionality for users to comment on blog posts and view detailed product information.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)

## Installation

Follow these steps to set up and run the project:

1. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment:**

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source .venv/bin/activate
     ```

3. **Upgrade pip to the latest version:**

   ```bash
   python -m pip install --upgrade pip
   ```

4. **Install Django and Pillow:**

   ```bash
   python -m pip install django
   python -m pip install Pillow
   ```

## Running the Development Server

To start the development server, run the following command:

```bash
python manage.py runserver
```
