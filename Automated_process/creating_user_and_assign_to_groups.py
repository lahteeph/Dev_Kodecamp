import subprocess

# Define users and their groups
users_and_groups = {
    'Andrew': 'system_admin',
    'Julius': 'legal',
    'Chizi': 'human_resources',
    'Jeniffer': 'sales',
    'Adeola': 'business_strategy',
    'Bach': 'ceo',
    'Gozie': 'it_intern',
    'Ogochukwu': 'finance'
}

def run_command(command):
    """Run a system command using subprocess."""
    try:
        subprocess.run(command, check=True, text=True)
        print(f"Command '{' '.join(command)}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Command '{' '.join(command)}' failed with error: {e}")

def create_group(group):
    """Create a group if it doesn't already exist."""
    try:
        subprocess.run(['sudo', 'groupadd', group], check=True, text=True)
        print(f"Group '{group}' created successfully.")
    except subprocess.CalledProcessError as e:
        if "already exists" in str(e):
            print(f"Group '{group}' already exists.")
        else:
            print(f"Failed to create group '{group}': {e}")

def create_user(username, group):
    """Create a user and assign them to a group."""
    create_group(group)
    try:
        subprocess.run(['sudo', 'useradd', '-m', '-g', group, username], check=True, text=True)
        print(f"User '{username}' with group '{group}' created successfully.")
    except subprocess.CalledProcessError as e:
        if "already exists" in str(e):
            print(f"User '{username}' already exists.")
        else:
            print(f"Failed to create user '{username}': {e}")

def setup_users(users_and_groups):
    """Setup users from the users_and_groups dictionary."""
    for user, group in users_and_groups.items():
        create_user(user, group)

def main():
    # Setup users
    setup_users(users_and_groups)

if __name__ == "__main__":
    main()

