import psycopg2

db_config = {
    'dbname': 'postgres_db',
    'user': 'user',
    'password': '12345678',
    'host': 'localhost',
    'port': '5433'
}

create_tables_commands = [

    """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (status_id) REFERENCES status(id)
    )
    """
]
def create_tables():
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        for command in create_tables_commands:
            cur.execute(command)

        conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
     create_tables()