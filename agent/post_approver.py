import os
from datetime import datetime

PENDING_DIR = "memory/pending/"
APPROVED_DIR = "memory/approved/"

# Ensure both directories exist
os.makedirs(PENDING_DIR, exist_ok=True)
os.makedirs(APPROVED_DIR, exist_ok=True)

def save_for_approval(post_text):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(PENDING_DIR, f"post_{timestamp}.txt")
    
    # Avoid overwriting
    counter = 1
    original_filename = filename
    while os.path.exists(filename):
        filename = original_filename.replace(".txt", f"_{counter}.txt")
        counter += 1

    with open(filename, "w") as f:
        f.write(post_text)
    
    print(f"✅ Post saved for approval: {filename}")

def get_approved_post():
    pending_posts = sorted(os.listdir(PENDING_DIR))
    for file in pending_posts:
        # Skip files that are already marked as posted
        if ".posted" in file:
            continue
            
        if file.endswith(".approved.txt"):
            file_path = os.path.join(PENDING_DIR, file)
            with open(file_path, "r") as f:
                content = f.read()

            # Archive to approved dir
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            archive_filename = f"approved_post_{timestamp}.txt"
            archive_path = os.path.join(APPROVED_DIR, archive_filename)

            # Avoid overwriting
            counter = 1
            original_archive_path = archive_path
            while os.path.exists(archive_path):
                archive_filename = f"approved_post_{timestamp}_{counter}.txt"
                archive_path = os.path.join(APPROVED_DIR, archive_filename)
                counter += 1

            with open(archive_path, "w") as f:
                f.write(content)

            print(f"✅ Approved post archived to: {archive_path}")
            return content, file_path  # Return both content and source file path

    return None, None  # Return None for both values if no post found
