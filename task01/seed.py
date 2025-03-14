from faker import Faker
import psycopg2
import random

fake = Faker()

db_config = {
    'dbname': 'postgres_db',
    'user': 'user',
    'password': '12345678',
    'host': 'localhost',
    'port': '5433'
}

def generate_users(n=30):
    return [(fake.name(), fake.email()) for _ in range(n)]

def generate_statuses():
    return ['new', 'in progress', 'completed']

def generate_tasks(n=30, user_ids=None, status_ids=None):
    if not user_ids or not status_ids:
        return []
    
    return [
        (fake.sentence(), fake.text(), random.choice(status_ids), random.choice(user_ids))
        for _ in range(n)
    ]

def populate_database():
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        conn.autocommit = True
        cur = conn.cursor()
 

        users = generate_users()
        user_ids = []
        for user in users:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id", user)
            user_ids.append(cur.fetchone()[0]) 

        statuses = generate_statuses()
        status_ids = []
        for status in statuses:
            cur.execute("INSERT INTO status (name) VALUES (%s) RETURNING id", (status,))
            status_ids.append(cur.fetchone()[0]) 

        tasks = generate_tasks(n=30, user_ids=user_ids, status_ids=status_ids)
        if tasks:
            cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", tasks)

        conn.commit()
        cur.close()
        print("Дані успішно додані!")
    
    except (Exception, psycopg2.DatabaseError) as error:
        print("Помилка:", error)
    
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    populate_database()
