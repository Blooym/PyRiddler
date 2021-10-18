"""
Sets up and installs dependancies
"""

import os

# Install Dependancies
print("Installing dependancies from requirements.txt")
os.system("pip3 install -r requirements.txt")

# Ready
print("Setup finished. You may not close this window.")

input("Press Enter to Close")
