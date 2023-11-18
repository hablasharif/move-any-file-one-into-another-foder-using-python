import os
import shutil

# Path to the directory containing the ZIP files
source_folder = r'C:\Users\style\Desktop\Movies srt files Zip Over 38k Files'

# Path to the new folder where ZIP files will be moved
destination_folder = r'C:\Users\style\Desktop\myzipmesrt'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Counter to keep track of the number of ZIP files moved
zip_files_count = 0

# Move all ZIP files from the source folder to the destination folder
for filename in os.listdir(source_folder):
    if filename.endswith('.srt'):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        zip_files_count += 1
        print(f"Moved: {filename} to {destination_folder}")

print(f"Total ZIP files moved: {zip_files_count}")
