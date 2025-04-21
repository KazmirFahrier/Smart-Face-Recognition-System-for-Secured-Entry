#import os

#current_directory = os.getcwd()

#print("Current working directory is: " + current_directory)
##Will  print this:
##Current working directory is: /home/pi/g4/Group-4
##unneccesar 



import os
directory_path = r"F:\4-2\Accuracy\Sakif"
def rename_images(directory_path):
    # Get a list of all files in the directory
    file_list = os.listdir(directory_path)

    # Filter only image files (you may want to customize this based on your file extensions)
    image_files = [file for file in file_list if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Sort the image files to ensure a consistent order
    image_files.sort()

    # Rename images serially
    for i, old_name in enumerate(image_files, start=1):
        # Generate the new name
        new_name = f"Sakif_{i}{os.path.splitext(old_name)[1].lower()}"

        # Construct the full paths
        old_path = os.path.join(directory_path, old_name)
        new_path = os.path.join(directory_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")

# Replace 'your_directory_path' with the path to your image directory
directory_path = r"F:\4-2\Accuracy\Sakif"

# Call the function to rename images in the specified directory
rename_images(directory_path)