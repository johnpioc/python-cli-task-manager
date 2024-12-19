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
    FROM tasks;
"""

def get_all_tasks():
    con = sqlite3.connect("tasks.db")
    cursor = con.cursor()
    tasks = cursor.execute(get_all_tasks_script).fetchall()
    return tasks


# Get task by ID script
get_task_by_id_script = """
    SELECT *
    FROM tasks
    WHERE id = ?
"""

def get_task_by_id(task_id):
    con = sqlite3.connect("tasks.db")
    cursor = con.cursor()
    task = cursor.execute(get_task_by_id_script, (task_id,)).fetchone()
    return task

# Update task name script
change_task_name_by_id_script = """
    UPDATE tasks
    SET task_name = ?
    WHERE id = ?
"""

def update_task_name_by_id(task_id):
    con = sqlite3.connect("tasks.db")
    cursor = con.cursor()
    updated_task = cursor.execute(change_task_name_by_id_script, (task_id,)).fetchone()
    return updated_task

# Toggle Task Completion Script
toggle_task_completion_by_id_script = """
    UPDATE tasks
    SET is_complete = case @type when 1 then 0 else 1 end
    WHERE id = ?
"""

def toggle_task_completion_by_id(task_id):
    con = sqlite3.connect("tasks.db")
    cursor = con.cursor()
    updated_task = cursor.execute(toggle_task_completion_by_id_script, (task_id,)).fetchone()
    return updated_task

# Delete Task by ID script
delete_task_by_id_script = """
    DELETE FROM tasks
    WHERE id = ?
"""

def delete_task_by_id(task_id):
    con = sqlite3.connect("tasks.db")
    cursor = con.cursor()
    deleted_task = cursor.execute(delete_task_by_id_script, (task_id,)).fetchone()
    return deleted_task