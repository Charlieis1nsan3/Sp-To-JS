import zipfile
import json
import os

def print_ascii_art():
    ascii_art = r"""
.-------------------------------------------------------------------.
| ________  ________  _________  ________        ___  ________      |
||\   ____\|\   __  \|\___   ___\\   __  \      |\  \|\   ____\     |
|\ \  \___|\ \  \|\  \|___ \  \_\ \  \|\  \     \ \  \ \  \___|_    |
| \ \_____  \ \   ____\   \ \  \ \ \  \\\  \  __ \ \  \ \_____  \   |
|  \|____|\  \ \  \___|    \ \  \ \ \  \\\  \|\  \\_\  \|____|\  \  |
|    ____\_\  \ \__\        \ \__\ \ \_______\ \________\____\_\  \ |
|   |\_________\|__|         \|__|  \|_______|\|________|\_________\|
|   \|_________|                                        \|_________||
'-------------------------------------------------------------------'                                                  
              Made with love by charlieis1nsan3
    """
    print(ascii_art)

def main():
    print_ascii_art()
    
    # Ask for the .sb3 file
    sb3_file = input("Enter the path to the .sb3 file: ")

    if not os.path.isfile(sb3_file):
        print("File not found. Please check the path and try again.")
        return

    # Create a zip file with the same name as the .sb3 file
    zip_file = sb3_file + ".zip"
    os.rename(sb3_file, zip_file)

    # Extract the zip file
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall()

    # Look for the project.json file in the extracted content
    project_json_file = None
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == "project.json":
                project_json_file = os.path.join(root, file)
                break

    if project_json_file:
        # Convert the project.json file to JavaScript
        with open(project_json_file, 'r') as f:
            project_json = json.load(f)

        js_code = "var project = " + json.dumps(project_json, indent=4) + ";"
        with open("project.js", 'w') as f:
            f.write(js_code)

        print("project.js file created successfully!")
    else:
        print("project.json file not found in the extracted content.")

if __name__ == "__main__":
    main()
