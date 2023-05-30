## Prerequisites

- Python 3.8+ (and pip)
- Git
- PostgreSQL
- psycopg2
- python-decouple

Before starting the setup process, ensure that you have installed Python, pip, Git, PostgreSQL, psycopg2, and python-decouple. follow the official installation guides for each prerequisite.

## 1. Clone the Project

Clone the repository from GitHub. In the terminal, navigate to the directory where you want to store the project and run:

```bash
git clone https://github.com/ladi-of/technical-test.git
```

## 2. Set Up Virtual Environment

In the project directory, create a new virtual environment using venv. Replace 'venv' with the name you want to give to your virtual environment.

```bash
python3 -m venv scratch
```

Activate the virtual environment. On Unix or MacOS, run:

```bash
source scratch/bin/activate
```

On Windows, run:

```bash
scratch\Scripts\activate
```

If you encounter a "command not found" error on Windows, make sure Python is added to your PATH environment variable.

## 3. Install Dependencies

With the virtual environment activated, install the project dependencies. Ensure that the `requirements.txt` file is in your current directory and run:

```bash
pip install -r requirements.txt
```

## 4. Database Setup

Before proceeding, make sure you have PostgreSQL command line client (psql) installed and configured.

Switch to the PostgreSQL user (usually by executing `sudo -u postgres psql`), then create a new database and user in PostgreSQL and grant all privileges to the user. Replace `<dbname>`, `<dbuser>`, and `<dbpass>` with your database name, database user, and database password, respectively.

```bash
psql -U postgres -c "CREATE DATABASE <dbname>;"
psql -U postgres -c "CREATE USER <dbuser> WITH PASSWORD '<dbpass>';"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE <dbname> TO <dbuser>;"
```

## 5. Setup Local Environment
Replace `<dbname>`, `<dbuser>`, and `<dbpass>` in the `setup.py` file with your database name, database user, and database password, respectively. Then run:

```bash
python setup.py
```

The `setup.py` script creates a virtual environment, installs project dependencies, and sets up your database.

## 6. Environment Variables

We are using `python-decouple` to manage environment variables. Create a `.env` file in the root directory of your Django project to store your environment variables. It should contain:

```
SECRET_KEY=your_secret_key
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost (or your database host)
DB_PORT=5432 (or your database port)
```

Replace the values with your actual data.

## 7. Making and Running Migrations

Apply migrations to the database. This process creates tables in your database according to the models defined in your Django application.

Make migrations for the `api` app:

```bash
python manage.py makemigrations api
```

Apply migrations

:

```bash
python manage.py migrate api
```

## 8. Load Data

Load data from the provided CSV file. Ensure you have a Python script, `load_users.py`, that loads data from a CSV file to your User model.

```bash
python manage.py load_users path_to_your_csv_file
```

Replace `path_to_your_csv_file` with the actual path to your CSV file.

## 9. Running the Server
Apply migrations

```bash
python manage.py migrate api
```

Run the server:

```bash
python manage.py runserver
```

The server should be accessible at `localhost:8000`.

To stop the server, simply press `CTRL+C` in the terminal where the server is running.

## 10. Testing the API

You can use `curl` or any API testing tool (like Postman) to send requests to your API.

To fetch a list of all users:

```bash
curl http://localhost:8000/api/v1/users/
```

To fetch the details of a specific user (replace `<id>` with the id of the user):

```bash
curl http://localhost:8000/api/v1/users/<id>/
```

Replace `<id>` with the actual ID of the user you want to fetch.

This guide should help you set up and run your Django REST API project successfully on Unix and Windows systems. Please replace all placeholder values with your actual data.