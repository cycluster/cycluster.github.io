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

    # Ask if the user wants to edit
    edit_choice = input(f"Do you want to edit the file {file_name}? [Y/n]: ").strip().lower()
    
    if edit_choice == "n":
        print(f"No changes made to {file_name}.")
        return  # Exit without making any changes
    
    # If the user wants to edit, we enter the interactive menu loop
    while True:
        # Show the current status
        print("\nChoose what to edit:")
        print(f"[1] Name: {name_line}")
        print(f"[2] Affiliation: {affiliation_line}")
        print(f"[3] Email: {email_line}")
        print(f"[4] URL: {url_line}")
        print(f"[N] Press N to exit")

        choice = input("Enter your choice (1-4 or N to exit): ").strip().lower()

        if choice == "n":
            print(f"No further changes made. Exiting editing mode for {file_name}.")
            break

        elif choice == "1":
            new_name = input(f"Enter new name (current: {name_line}): ").strip()
            if new_name:
                name_line = new_name
            print(f"Name updated to: {name_line}")

        elif choice == "2":
            new_affiliation = input(f"Enter new affiliation (current: {affiliation_line}): ").strip()
            if new_affiliation:
                affiliation_line = new_affiliation
            print(f"Affiliation updated to: {affiliation_line}")

        elif choice == "3":
            new_email = input(f"Enter new email (current: {email_line}): ").strip()
            if new_email:
                email_line = new_email
            print(f"Email updated to: {email_line}")

        elif choice == "4":
            new_url = input(f"Enter new URL (current: {url_line}): ").strip()
            if new_url:
                url_line = new_url
            print(f"URL updated to: {url_line}")

        else:
            print("Invalid choice. Please enter a number between 1-4 or N to exit.")
            continue

        # After editing, ask the user if they want to make more changes
        save_changes = input(f"Do you want to make any other changes to {file_name}? [Y/n]: ").strip().lower()
        if save_changes == "n":
            break
    
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
