# The portapy build script. RUN ON A ACTUAL INSTALLED VERSION OF PYTHON.
# Anything Python 3.0+ *should* do for building.

from shutil import rmtree
from os import makedirs
from distutils.dir_util import copy_tree
# Imports go here.

try:
    rmtree("./build")
    print("Found a old build and removed it.")
except:
    pass
# Tries removing the build folder and its contents if it exists.

print("Making a brand new build folder.")
makedirs("./build")
# Makes a build folder.

print("Making a brand new folder for the Python library/packages.")
makedirs("./build/pylibs")
# Makes a folder for the Python library/packages.

print("Copying all of the embedded Python files.")
copy_tree("./embedded_python", "./build/pylibs/")
# Copies all of the embedded Python files.

print("Copying all of the Python packages.")
copy_tree("./custom_packages", "./build/pylibs/")
# Copies all of the Python packages.

print("Copying all of the tkinter stuff.")
copy_tree("./tk", "./build/pylibs/")
# Copies all of the tkinter stuff.

print("Writing a batch file to open IDLE.")
idle_bat = "start pylibs\pythonw.exe -m idlelib"
with open("./build/Run IDLE.bat", "w+") as file:
    file.write(idle_bat)
# Creates a batch file to start IDLE.

print("Writing a batch file to open the Python shell.")
shell_bat = "start pylibs\python.exe"
with open("./build/Run Python Shell.bat", "w+") as file:
    file.write(shell_bat)
# Creates a batch file to start the Python shell.
