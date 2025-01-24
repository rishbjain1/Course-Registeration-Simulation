# %%
import csv

# User authentication functions

# %%
def load_users(filename="users.csv"):
    # Load existing user credentials from a CSV file.
    # Returns a dictionary where usernames are keys and hashed passwords are values.
    try:
        with open(filename, 'r') as file:
            users = {row[0]: row[1] for row in csv.reader(file)}
            return users
    except FileNotFoundError:
        # If the file doesn't exist, return an empty dictionary.
        return {}

# %%
def save_users(users, filename="users.csv"):
    # Save user credentials to a CSV file. Each row contains a username and a hashed password.
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for user, password in users.items():
            writer.writerow([user, password])

# %%
def register_user(users, username, password):
    # Register a new user with a unique username and a hashed password.
    # Returns True if registration is successful, False if the username already exists.
    if username in users:
        return False
    users[username] = password
    save_users(users)
    return True

# %%
def authenticate(users, username, password):
    # Verify a user's login credentials.
    # Returns True if the username and password match the stored credentials, otherwise False.
    return users.get(username) == password

# %%
# Task management functions
def load_tasks(filename="tasks.csv"):
    # Load tasks from a CSV file.
    # Returns a list of dictionaries, each representing a task with 'id', 'user', 'description', and 'status'.
    try:
        with open(filename, 'r') as file:
            tasks = list(csv.DictReader(file))
            return tasks
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list.
        return []


# %%
def save_tasks(tasks, filename="tasks.csv"):
    # Save tasks to a CSV file. Each task is stored with its 'id', 'user', 'description', and 'status'.
    with open(filename, 'w', newline='') as file:
        fieldnames = ['id', 'user', 'description', 'status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

# %%

def add_task(tasks, user, description):
    # Add a new task for a specific user.
    # Each task has a unique ID, the user's name, a description, and an initial status of 'Pending'.
    task_id = str(len(tasks) + 1)
    tasks.append({'id': task_id, 'user': user, 'description': description, 'status': 'Pending'})
    save_tasks(tasks)

# %%
def main_menu():
    # Main menu for user registration, login, or exit.
    users = load_users()
    tasks = load_tasks()

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            # User registration process.
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            if register_user(users, username, password):
                print("Registration successful.")
            else:
                print("Username already exists.")
        elif choice == '2':
            # User login process.
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if authenticate(users, username, password):
                print("Login successful.")
                user_menu(username, tasks)
            else:
                print("Invalid username or password.")
        elif choice == '3':
            # Exit the program.
            break

# %%
def user_menu(username, tasks):
    # Sub-menu for a logged-in user to manage their tasks.
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Add a new task.
            description = input("Enter task description: ")
            add_task(tasks, username, description)
            print("Task added.")
        elif choice == '2':
            # Display all tasks for the logged-in user.
            print("Your tasks:")
            for task in tasks:
                if task['user'] == username:
                    print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
        elif choice == '3':
            # Exit the user menu.
            break

# %%
if __name__ == "__main__":
    main_menu()

# %%



