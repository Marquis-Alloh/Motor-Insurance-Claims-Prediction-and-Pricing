import os
from pathlib import Path
import psycopg2
import getpass
from dotenv import load_dotenv


# Locate the project root and load configuration
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = PROJECT_ROOT / "sql" / "schema.sql"

load_dotenv(PROJECT_ROOT / ".env")


def get_connection():
    """
    Establish a connection to the PostgreSQL database.

    Returns
    -------
    psycopg2.extensions.connection
        An active connection to the configured database.
    """
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "motor_insurance"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def apply_schema() -> None:
    """
    Create database tables by executing the SQL schema file.

    Reads the SQL statements from sql/schema.sql and executes them
    against the configured PostgreSQL database.

    Raises
    ------
    FileNotFoundError
        If the schema file does not exist.
    psycopg2.Error
        If the database connection or SQL execution fails.

    Returns
    -------
    None
        Database changes are committed if execution succeeds.
    """
    if not SCHEMA_PATH.is_file():
        raise FileNotFoundError(
            f"Schema file not found: {SCHEMA_PATH}"
        )

    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")

    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(schema_sql)
    finally:
        conn.close()


if __name__ == "__main__":
    apply_schema()
    print("Database schema applied successfully.")