import sys
import datetime
from agent.planner import should_post_today
from agent.researcher import research_topic
from agent.writer import generate_post
from agent.poster import post_to_linkedin
from agent.post_approver import save_for_approval, get_approved_post
from agent.topic_fetcher import get_trending_topic
import csv
import os

POST_LOG_FILE = "post_log.csv"

def generate_and_save_post():
    # if should_post_today():
    topic = get_trending_topic('Leadership')  # Or use research_topic()
    post = generate_post(topic, tone="professional")
    save_for_approval(post)
    print(f"[{datetime.datetime.now()}] Post saved for approval:\n{post}")
    # else:
    #     print("Skipping today. Not scheduled to post.")

def post_approved_post():
    # Get approved post content and source file path
    approved_post, source_file = get_approved_post()
    if approved_post and source_file:
        try:
            # Post to LinkedIn
            post_to_linkedin(approved_post)
            
            # Create posted directory if it doesn't exist
            posted_dir = os.path.join("memory", "posted")
            os.makedirs(posted_dir, exist_ok=True)
            
            # Generate timestamped filename for the posted content
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = os.path.join(posted_dir, f"posted_{timestamp}.txt")
            
            # Save the posted content to the file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(approved_post)
            
            # Rename the source file to mark it as posted
            posted_source_file = f"{source_file}.posted"
            os.rename(source_file, posted_source_file)
            
            print(f"[{datetime.datetime.now()}] Posted to LinkedIn, saved to {filename}, and marked source as posted")
        except Exception as e:
            print(f"Error during posting: {e}")
            return
    else:
        print("No approved post found. Skipping posting.")


def log_post_to_csv(post_content: str, filename: str):
    log_exists = os.path.isfile(POST_LOG_FILE)
    with open(POST_LOG_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not log_exists:
            writer.writerow(["Date", "Filename", "Snippet"])
        writer.writerow([
            datetime.datetime.now().isoformat(),
            filename,
            post_content[:60].replace('\n', ' ')  # Short snippet
        ])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py [generate|post]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "generate":
        generate_and_save_post()
    elif command == "post":
        post_approved_post()
    else:
        print("Invalid command. Use 'generate' or 'post'.")


## python main.py generate
## python main.py post
