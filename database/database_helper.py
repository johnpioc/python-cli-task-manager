import sqlite3

# Create table SQL script
create_table_script = """
    CREATE TABLE tasks(
        id INTEGER,
        task_name TEXT,
        is_complete INTEGER,
        PRIMARY KEY(id) 
    );
"""

# Get list of tables SQL script
list_of_tables_script = """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    AND name='tasks'
"""

def setup_database():
    con = sqlite3.connect("tasks.db")
    cursor = con.cursor()

    # Check if tasks table already exists
    list_of_tables = cursor.execute(list_of_tables_script).fetchall()
    if list_of_tables[0] != ('tasks',):
        cursor.execute(create_table_script)

    con.close()

# Get all tasks script
get_all_tasks_script = """
    SELECT *
    FROM tasks
"""

def get_all_tasks():
    con = sqlite3.connect("tasks.db")
    cursor = con.cursor()
    tasks = cursor.execute(get_all_tasks_script).fetchall()
    return tasks


