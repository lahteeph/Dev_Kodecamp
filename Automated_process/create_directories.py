import os

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

if __name__ == "__main__":
    # Setup directories
    setup_directories(company_directories)

