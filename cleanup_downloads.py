import os
import shutil
import time


def clean_downloads_folder(folder_path, backup_folder_path, days_threshold):
    # Check if the downloads folder exists
    if not os.path.exists(folder_path):
        print(f"The downloads folder '{folder_path}' does not exist.")
        return

    # Check if the backup folder exists, if not, create it
    if not os.path.exists(backup_folder_path):
        os.makedirs(backup_folder_path)

    # Get the current timestamp
    current_time = time.time()
    # Calculate the threshold time
    threshold_time = current_time - (days_threshold * 24 * 60 * 60)

    # Iterate over files in the downloads folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            # Check if the file is older than the threshold time
            if os.path.isfile(file_path) and os.path.getmtime(file_path) < threshold_time:
                # Move the file to the backup folder
                shutil.move(file_path, os.path.join(backup_folder_path, filename))
                print(f"Moved '{filename}' to backup folder.")
        except Exception as e:
            print(f"Error occurred while processing '{filename}': {e}")

    print("Cleanup completed.")


# usage:
downloads_folder = "C:/Users/USER/Downloads"
backup_folder = "C:/Users/USER/Desktop/Downloadsbackup"
days_threshold = 32 # Adjust this threshold as needed

clean_downloads_folder(downloads_folder, backup_folder, days_threshold)
