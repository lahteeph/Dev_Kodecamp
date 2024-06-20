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

if __name__ == "__main__":
    # User input for file creation
    user_input_file_creation(company_directories)

