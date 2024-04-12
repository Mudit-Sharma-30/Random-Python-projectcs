import os
import shutil
import json

class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def get_files_in_folder(self):
        if not os.path.exists(self.folder_path):
            print(f"The folder '{self.folder_path}' does not exist.")
            return []

        files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
        return files

    def organize_files_by_extension(self):
        files_in_folder = self.get_files_in_folder()
        
        with open('file_categories.txt', 'r') as file:
            file_categories = json.load(file)


        other_folder = os.path.join(self.folder_path, "Other")  # Create "Other" folder
        os.makedirs(other_folder, exist_ok=True)  # Ensure "Other" folder exists

        for file_name in files_in_folder:
            name, extension = file_name.split()[0],file_name.split(".")[-1]
            
            category = file_categories.get(extension.lower(), extension)  # Use "Other" category for unspecified extensions
            if category == extension:
                print(f"\033[1mNo deafult extension is found the {file_name} so putting this file in {extension} folder\033[0m")
            category_folder = os.path.join(self.folder_path, category)
            os.makedirs(category_folder, exist_ok=True)

            source_path = os.path.join(self.folder_path, file_name)
            destination_path = os.path.join(category_folder, file_name)
            shutil.move(source_path, destination_path)
            print(f"{file_name} file have been moved to the folder named {category}")

        


    def main(self):
        files_in_folder = self.get_files_in_folder()
        
        self.organize_files_by_extension()

# Example usage:
if __name__ == "__main__":

    folder_path = input("Enter the folder path where you want to manage the files:-\n") # Replace with your actual folder path
    organizer = FileOrganizer(folder_path)
    organizer.main()
