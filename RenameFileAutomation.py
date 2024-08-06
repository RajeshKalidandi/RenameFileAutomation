import os

folder_path = "C:/Users/krish/Pictures/Screenshots"

for index, filename in enumerate(os.listdir(folder_path)):

    new_name = f"{index:02}.png"

    old_file_folder = os.path.join(folder_path, filename)
    new_file_folder = os.path.join(folder_path, new_name)

    os.rename(old_file_folder, new_file_folder)

    print(f"Renamed : {filename} to {new_name}")



