import os
import shutil
import csv

# Function to organize files in a folder by file type
def organize_files_by_type(folder_path):
    # Define common file type categories
    file_categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xls', '.xlsx'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.tar', '.rar']
    }

    # Create subfolders for each category
    for category in file_categories:
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

    # Move files into respective subfolders
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False
            for category, extensions in file_categories.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(folder_path, category, file))
                    moved = True
                    print(f"Moved: {file} → {category}")
                    break
            if not moved:
                other_folder = os.path.join(folder_path, 'Others')
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))
                print(f"Moved: {file} → Others")

# Function to sort lines in a text file
def sort_file_contents(file_path, numeric=False):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if numeric:
        lines.sort(key=lambda x: float(x.strip()))
    else:
        lines.sort()

    with open(file_path, 'w') as file:
        file.writelines(lines)
    
    print(f"Sorted file: {file_path}")

# Function to sort a CSV file based on a specified column
def sort_spreadsheet(file_path, column_index=0, reverse=False):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Save the header
        rows = list(reader)

    # Sort rows by the specified column index
    rows.sort(key=lambda x: x[column_index], reverse=reverse)

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)  # Write header
        writer.writerows(rows)
    
    print(f"Sorted spreadsheet: {file_path} by column {column_index + 1}")

# Main function to interact with user
def main():
    print("Welcome to the data arrangement automation tool.")
    print("Select an option:")
    print("1. Organize files in a folder")
    print("2. Sort contents of a file")
    print("3. Sort a spreadsheet (CSV)")
    choice = input("Enter 1, 2, or 3: ")

    if choice == '1':
        folder_path = input("Enter the folder path: ")
        organize_files_by_type(folder_path)
    elif choice == '2':
        file_path = input("Enter the text file path: ")
        numeric = input("Sort numerically? (yes/no): ").lower() == 'yes'
        sort_file_contents(file_path, numeric)
    elif choice == '3':
        file_path = input("Enter the CSV file path: ")
        column_index = int(input("Enter the column index (starting from 0): "))
        reverse = input("Sort in descending order? (yes/no): ").lower() == 'yes'
        sort_spreadsheet(file_path, column_index, reverse)
    else:
        print("Invalid option. Please restart the script.")

if __name__ == "__main__":
    main()
