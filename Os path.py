import os

current_dir = os.getcwd()
for filename in os.listdir(current_dir):
    if os.path.isfile(os.path.join(current_dir, filename)):
        print(f"File: {filename}")
    else:
        print(f"Directory: {filename}")
    
