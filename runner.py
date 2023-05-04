from subprocess import call
import os
import sys

# Get the path to the virtual environment
env_path = os.path.dirname(sys.executable)

# Construct the path to the coba.py file relative to the virtual environment directory
script_path = os.path.join(env_path, "coba.py")

# Call the script using the new path
call([sys.executable, script_path])
input("Press Enter to exit")

