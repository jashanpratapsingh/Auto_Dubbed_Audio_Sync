import os
import shutil

def move_folders_to_repository():
    # Define the base directory
    base_directory = os.path.join(os.path.dirname(__file__), "..")

    # Find the highest number in the existing database repositories
    database_directory = os.path.join(base_directory, "database")
    os.makedirs(database_directory, exist_ok=True)

    database_directories = [name for name in os.listdir(database_directory) if name.startswith("video_")]
    if database_directories:
        highest_number = max([int(name.split("_")[1]) for name in database_directories])
    else:
        highest_number = 0

    # Create the new repository directory with an incremented number
    new_repository_number = highest_number + 1
    new_repository_directory = os.path.join(database_directory, f"video_{new_repository_number}")

    # Copy the "Outputs" and "final_videos" directories to the new repository
    outputs_directory = os.path.join(base_directory, "Outputs")
    final_videos_directory = os.path.join(base_directory, "final_videos")

    shutil.copytree(outputs_directory, os.path.join(new_repository_directory, "Outputs"))
    shutil.copytree(final_videos_directory, os.path.join(new_repository_directory, "final_videos"))

    # Remove the original directories
    shutil.rmtree(outputs_directory)
    shutil.rmtree(final_videos_directory)

    print(f"Moved folders to repository: {new_repository_directory}")

move_folders_to_repository()