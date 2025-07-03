import time
import os
from datetime import datetime

TEST_DIR = "."
DUMMY_FILES = [f"dummy{i}.py" for i in range(1, 11)]

def make_tiny_change(file_path):
    # Create the file if it doesn't exist, then append
    with open(file_path, "a") as f:
        f.write(f"# Auto-change at {datetime.now()}\n")

def main():
    while True:
        for filename in DUMMY_FILES:
            file_path = os.path.join(TEST_DIR, filename)
            make_tiny_change(file_path)
        print("Made tiny changes to all dummy files. Commit and push now!")
        time.sleep(120)  # 5 minutes

if __name__ == "__main__":
    main()