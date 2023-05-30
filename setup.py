import os
import sys
import subprocess
import venv
import psycopg2
from psycopg2 import sql


class DatabaseConfigurator:
    def __init__(self, dbname, user, password, host, postgres_password):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.postgres_password = postgres_password

    def create_database(self):
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password=self.postgres_password,
                host=self.host
            )
            conn.autocommit = True

            cur = conn.cursor()

            if not self.is_database_existing(cur):
                cur.execute(sql.SQL("CREATE DATABASE {};").format(
                    sql.Identifier(self.dbname)))

            if not self.is_user_existing(cur):
                cur.execute(sql.SQL("CREATE USER {} WITH PASSWORD '{}';").format(
                    sql.Identifier(self.user), sql.SQL(self.password)))

            cur.execute(sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {};").format(
                sql.Identifier(self.dbname), sql.Identifier(self.user)))

            conn.close()

        except psycopg2.OperationalError as e:
            print("Could not connect to PostgreSQL: ", e)
            sys.exit(1)

    def is_database_existing(self, cur):
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{self.dbname}'")
        return bool(cur.rowcount)

    def is_user_existing(self, cur):
        cur.execute(f"SELECT 1 FROM pg_roles WHERE rolname='{self.user}'")
        return bool(cur.rowcount)


class EnvironmentBuilder:
    def __init__(self, project_name, venv_name, requirements_file):
        self.project_name = project_name
        self.venv_name = venv_name
        self.requirements_file = requirements_file

    def build(self):
        if not os.path.exists(self.project_name):
            subprocess.check_call(
                ["git", "clone", f"https://github.com/ladi-of/{self.project_name}.git"])

        self.setup_virtualenv()

    def setup_virtualenv(self):
        venv_dir = os.path.join(os.path.dirname(__file__), self.venv_name)
        venv.create(venv_dir, with_pip=True)

        pip_cmd = os.path.join(venv_dir, 'bin', 'pip') if sys.platform != "win32" else os.path.join(
            venv_dir, 'Scripts', 'pip.exe')
        try:
            subprocess.check_call(
                [pip_cmd, "install", "-r", os.path.join(self.project_name, self.requirements_file)])
        except subprocess.CalledProcessError as e:
            print("Could not install requirements: ", e)
            sys.exit(1)


def main():
    host = input("Please enter your PostgreSQL host: ")
    postgres_password = input("Please enter your PostgreSQL password: ")

    database_configurator = DatabaseConfigurator(
        "<dbname>", "<dbuser>", "<dbpass>", host, postgres_password)
    database_configurator.create_database()

    environment_builder = EnvironmentBuilder(
        'technical-test', 'venv', 'requirements.txt')
    environment_builder.build()

    print("Setup complete!")


if __name__ == "__main__":
    main()
