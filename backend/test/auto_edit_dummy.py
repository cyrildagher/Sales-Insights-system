import time
import os
import subprocess
from datetime import datetime

TEST_DIR = "."
DUMMY_FILES = [f"dummy{i}.py" for i in range(1, 6)]  # Reduced from 10 to 5 files

def make_tiny_change(file_path):
    # Create the file if it doesn't exist, then append
    with open(file_path, "a") as f:
        f.write(f"# {datetime.now().strftime('%H:%M')}\n")  # Shorter timestamp

def git_commit_and_push():
    try:
        # Add all changes
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit with shorter timestamp
        commit_message = f"Update {datetime.now().strftime('%H:%M')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Push to main branch
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print(f"✅ Pushed: {commit_message}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Git operation failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🤖 Starting automated dummy file editor (5-minute mode)")
    print("📝 Will make changes every 5 minutes to 5 files")
    print("🛑 Press Ctrl+C to stop the script")
    
    while True:
        try:
            # Make changes to dummy files
            for filename in DUMMY_FILES:
                file_path = os.path.join(TEST_DIR, filename)
                make_tiny_change(file_path)
            
            print(f"📝 Updated files at {datetime.now().strftime('%H:%M')}")
            
            # Auto commit and push
            if git_commit_and_push():
                print("🎉 Changes pushed to GitHub!")
            else:
                print("⚠️  Failed to push - check manually")
            
            print("⏰ Waiting 5 minutes...")
            time.sleep(300)  # 5 minutes
            
        except KeyboardInterrupt:
            print("\n🛑 Script stopped by user")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()