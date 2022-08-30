import os
import subprocess
import shutil
import sys
import json

TEST_BUILD = False
INPUT_FILE = "VodSlicer.py"
OUTPUT_FILE = "VodSlicer.exe"

# Specify Paths and Files
cwd = os.getcwd()
ui_path = os.path.join(cwd, "resources", "ui")
destination_file = os.path.join(cwd, "UI_Components.py")
resource_file = os.path.join(cwd, "VodSlicer.rc")
dist_dir = os.path.join(cwd, "dist")
target_env = "windows"
partial = False

if(len(sys.argv)>1):
    if(sys.argv[1] == "partial"):
        partial = True

print("Building VodSlicer")
print(f"Test Build: {TEST_BUILD}")
print(f"Target Env: {target_env}")
print("Reading Version File: version.json")
with open("version.json", "r") as version_file:
    version = json.load(version_file)
print(f"Company Name: {version['company_name']}")
print(f"Product Name: {version['product_name']}")
print(f"Product Ver: {version['version']}")
print()

# Create dist directory if it doesnt exist
if(not os.path.isdir(dist_dir)):
    os.makedirs(dist_dir, exist_ok=True)

# Function to find all files in dir_path 
# with extension (not recursive)
def getFilesWithExtension(dir_path,  extension):
    files = []
    for file in os.listdir(dir_path):
        if file.endswith(f".{extension}"):
            files.append(os.path.join(ui_path, file))
    return files
    
# Function to compile the provided ui_file to py
# and place it in destination_path
def compileUiFile(ui_file, destination_file):
    # uic -g python $ui_file >> destination_file
    ret = subprocess.run(["pyside6-uic", "-g", "python", ui_file], capture_output=True)
    if(ret.returncode != 0):
        print(f"\nError Compiling {ui_file}")
        print(ret.stderr)
        return False
    output = ret.stdout
    with open(destination_file, "ab") as py_file:
        py_file.write(output)
        py_file.write(b"\r\n\r\n")
    return True

# Function to compile the provided ui_file to py
# and place it in destination_path
def compileResources(resources_file, destination_file):
    #rcc -g python -o Resources.py LightPlanStudio.rc
    ret = subprocess.run(["pyside6-rcc", "-g", "python", "-o", destination_file, resources_file], capture_output=True)
    stderr = ret.stderr.decode("utf-8")
    if(ret.returncode != 0):
        print(stderr)
        return False
    return True
    
print("Compiling All UI Files to Single Python File")
print(f"UI File Dir: {ui_path}")
print(f"Destination Python File: {destination_file}")

if(os.path.exists(destination_file)):
    print("Existing Destination File Found")
    destination_file_bak = destination_file + ".bak"
    print(f"Making Backup: {destination_file_bak}")
    try:
        shutil.copyfile(destination_file, destination_file_bak)
        print("\tFile Backup Success")
    except Exception as e:
        print("Error Making Backup File")
        print(e)
        print("Quitting...")
        sys.exit(1)
    print("Removing Old Destination File")
    os.remove(destination_file)
print("=============================================\n")
ui_files = getFilesWithExtension(ui_path, "ui")
for file in ui_files:
    print(f"Compiling {file}...", end="")
    if(compileUiFile(file, destination_file)):
        print("Success")
    else:
        print("Failure")

print("\nUI Files Compiled")
print("=============================================\n")
print("Compiling Resources")

resource_dest = "Resources.py"
if(compileResources(resource_file, resource_dest)):
    print(f"Compiling Resources File: {resource_file} to {resource_dest}")
else:
    print(f"\nError Compiling {resource_file}")

print("=============================================\n")

if(partial):
    print("Partial Build Requested. Not Compiling Binary")
    print("=============================================\n")
    sys.exit(0)

print("Compiling Binary")

if(target_env == "windows"):
    show_cmd = "--windows-disable-console "
    if(TEST_BUILD):
        show_cmd = ""
        
    cmd = f"py -m nuitka --onefile --standalone " \
            f"--enable-plugin=pyside6,numpy --windows-icon-from-ico={version['ico']} " \
            f"{show_cmd}" \
            f" -o dist/{OUTPUT_FILE} " \
            f"{INPUT_FILE}"
    
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for c in iter(lambda: proc.stdout.read(1), b''):
    sys.stdout.write(c.decode("utf-8"))
    
for c in iter(lambda: proc.stderr.read(1), b''):
    sys.stdout.write(c.decode("utf-8"))

proc.communicate()

print("\n=============================================")
if(proc.returncode == 0):
    print("Binary Compiled Successfully")
else:
    print("Error Compiling Binary")
print("=============================================\n")
