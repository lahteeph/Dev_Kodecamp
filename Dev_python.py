import os
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

# Define company directories
company_directories = [
    'Finance_Budgets',
    'Contract_Documents',
    'Business_Projections',
    'Business_Models',
    'Employee_Data',
    'Company_Vision_and_Mission_Statement',
    'Server_Configuration_Script'
]

def run_command(command):
    """Run a system command using subprocess."""
    try:
        subprocess.run(command, check=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command '{' '.join(command)}' failed with error: {e}")
        return False

def create_user(username, group):
    """Create a user and assign them to a group."""
    if run_command(['sudo', 'groupadd', group]):
        run_command(['sudo', 'useradd', '-m', '-g', group, username])

def setup_users(users_and_groups):
    """Setup users from the users_and_groups dictionary."""
    for user, group in users_and_groups.items():
        create_user(user, group)
    
def create_directory(directory_name):
    """Create a directory if it doesn't already exist."""
    try:
        os.makedirs(directory_name, exist_ok=True)
        print(f"Directory '{directory_name}' created successfully.")
    except OSError as e:
        print(f"Failed to create directory '{directory_name}': {e}")

def setup_directories(directories):
    """Setup directories from the directories list."""
    for directory in directories:
        create_directory(directory)
        
def create_file_in_directory(file_name, directory_name, valid_directories):
    """Create a file in the specified directory if it's a valid directory."""
    if directory_name in valid_directories:
        file_path = os.path.join(directory_name, file_name)
        try:
            with open(file_path, 'w') as f:
                f.write("This is a placeholder content.")
            print(f"File '{file_name}' created in '{directory_name}' successfully.")
        except OSError as e:
            print(f"Failed to create file '{file_name}' in '{directory_name}': {e}")
    else:
        print(f"Directory '{directory_name}' is not a valid company directory.")

def user_input_file_creation(valid_directories):
    """Take user input to create a file in one of the valid directories."""
    file_name = input("Enter the name of the file: ")
    directory_name = input("Enter the directory to create the file in: ")
    create_file_in_directory(file_name, directory_name, valid_directories)

def main():
    # Setup users
    setup_users(users_and_groups)
    
    # Setup directories
    setup_directories(company_directories)
    
    # User input for file creation
    user_input_file_creation(company_directories)
    
if __name__ == "__main__":
    main()
