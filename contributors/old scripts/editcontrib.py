import os
import sys

def create_contributor_file(contrib_name):
    # Ask for input to create the contributor file
    print(f"Creating a new file for {contrib_name}...\n")
    name = input("Enter name (cannot be empty): ").strip()
    
    while not name:  # Ensure name is not empty
        print("Name cannot be empty. Please enter a valid name.")
        name = input("Enter name (cannot be empty): ").strip()

    affiliation = input("Enter affiliation (leave blank if not applicable): ").strip()
    email = input("Enter email (leave blank if not applicable): ").strip()
    url = input("Enter URL (leave blank if not applicable): ").strip()
    
    # Prepare content for the .md file
    content = f"---\nname: {name}\naffiliation: {affiliation}\nemail: {email}\nurl: {url}\n---\n"
    
    # Create the .md file directly in the current directory
    file_name = f"{contrib_name.lower()}.md"
    with open(file_name, "w") as f:
        f.write(content)
    
    print(f"{file_name} was created successfully!")


def edit_contributor_file(contrib_name):
    # Convert to lower case for case-insensitivity
    file_name = f"{contrib_name.lower()}.md"
    
    if not os.path.exists(file_name):
        print(f"{file_name} does not exist.")
        create_new = input(f"Do you want to create a new file for {contrib_name}? (Y/N): ").strip().lower()
        if create_new == "y":
            create_contributor_file(contrib_name)
        else:
            print("Exiting without creating a new file.")
        return
    
    print(f"{file_name} already exists.")
    
    # Read the existing file
    with open(file_name, "r") as f:
        content = f.readlines()

    # Extract current values
    name_line = content[1].strip().split(":")[1].strip()
    affiliation_line = content[2].strip().split(":")[1].strip()
    email_line = content[3].strip().split(":")[1].strip()
    url_line = content[4].strip().split(":")[1].strip()

    # Ask if the user wants to overwrite the entire file first
    overwrite_file = input(f"Do you want to overwrite the entire file {file_name}? [Y/n]: ").strip().lower()
    
    if overwrite_file == "n":
        print(f"No changes made to {file_name}.")
        return  # Exit without making any changes
    
    # Proceed with editing individual fields if file is being overwritten
    print(f"Current name: {name_line}")
    overwrite_name = input(f"Do you want to overwrite the name? [Y/n]: ").strip().lower()
    if overwrite_name != "n":
        new_name = input(f"Enter new name (current: {name_line}): ").strip()
        if new_name:
            name_line = new_name
    
    print(f"Current affiliation: {affiliation_line}")
    overwrite_affiliation = input(f"Do you want to overwrite the affiliation? [Y/n]: ").strip().lower()
    if overwrite_affiliation != "n":
        new_affiliation = input(f"Enter new affiliation (current: {affiliation_line}): ").strip()
        affiliation_line = new_affiliation
    
    print(f"Current email: {email_line}")
    overwrite_email = input(f"Do you want to overwrite the email? [Y/n]: ").strip().lower()
    if overwrite_email != "n":
        new_email = input(f"Enter new email (current: {email_line}): ").strip()
        email_line = new_email
    
    print(f"Current URL: {url_line}")
    overwrite_url = input(f"Do you want to overwrite the URL? [Y/n]: ").strip().lower()
    if overwrite_url != "n":
        new_url = input(f"Enter new URL (current: {url_line}): ").strip()
        url_line = new_url
    
    # Update the content with the new values
    updated_content = f"---\nname: {name_line}\naffiliation: {affiliation_line}\nemail: {email_line}\nurl: {url_line}\n---\n"

    # Write the updated content back to the file
    with open(file_name, "w") as f:
        f.write(updated_content)
    
    print(f"{file_name} was edited successfully!")


def main():
    # Ensure there is an argument
    if len(sys.argv) != 2:
        print("Usage: python3 editcontrib.py <contributor_name>")
        sys.exit(1)
    
    # Get the contributor name from the command-line argument
    contrib_name = sys.argv[1].strip().lower()

    # Check if the contributor file exists
    file_name = f"{contrib_name}.md"
    
    print(f"Checking for file: {file_name}")  # Debugging print

    if os.path.exists(file_name):
        print(f"File {file_name} exists.")  # Debugging print
        edit_contributor_file(contrib_name)
    else:
        print(f"File {file_name} does not exist.")  # Debugging print
        create_new = input(f"{file_name} does not exist. Do you want to create a new file for {contrib_name}? (Y/N): ").strip().lower()
        if create_new == "y":
            create_contributor_file(contrib_name)
        else:
            print("Exiting without creating a new file.")
    

if __name__ == "__main__":
    main()
