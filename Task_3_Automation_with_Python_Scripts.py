import shutil
from pathlib import Path
import requests
import re
from bs4 import BeautifulSoup

#https://www.codealpha.tech/


def img_mover(folder_path_old, folder_path_new):

    src_path = Path(folder_path_old)
    dst_path = Path(folder_path_new)

    # Check if source actually exists
    if not src_path.exists():
        print(f"Error: Source path '{src_path}' does not exist.")
        return

    print("Options")
    print("""
    1) Copy from source to destination
    2) Move from source to destination
    """)
    choices = input("Enter: ").strip()

    if choices == "1":
        if src_path.is_file():
            
            if not dst_path.suffix:
                dst_path.mkdir(parents=True, exist_ok=True)
            
            shutil.copy2(src=src_path, dst=dst_path)
            print("File copied successfully.")
            
        elif src_path.is_dir():
            
            shutil.copytree(src=src_path, dst=dst_path, dirs_exist_ok=True)
            print("Directory copied successfully.")

    elif choices == "2":
        
        if not dst_path.parent.exists():
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            
       
        shutil.move(src=src_path, dst=dst_path)
        print("Item moved successfully.")
        
    else:
        print("You didn't select any valid option.")

def Email_extracter(file_path_old, file_path_new):
    old_path = Path(file_path_old)
    new_path = Path(file_path_new)

    if not old_path.exists():
        print(f"Error: Source path '{old_path}' does not exist.")
        return

    # Regex pattern matching any valid email address
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    extracted_emails = set()  # Use a set to automatically remove duplicates

    with open(old_path, "r", encoding="utf-8") as file:
        for line in file:
            # Find all matching emails in the current line
            matches = re.findall(email_pattern, line)
            extracted_emails.update(matches)

    # Ensure output directory exists
    new_path.parent.mkdir(parents=True, exist_ok=True)

    with open(new_path, "w", encoding="utf-8") as file:
        for email in sorted(extracted_emails):
            file.write(f"{email}\n")

    print(
        f"Successfully extracted {len(extracted_emails)} unique email(s) to '{new_path}'."
    )

def Website_titles(Websit_url):
    # Ensure the URL includes a scheme (http/https)
    if not Websit_url.startswith(("http://", "https://")):
        Websit_url = "https://" + Websit_url

    # Standard browser User-Agent to avoid 403 Forbidden blocks
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        # Fetch the web page with a 10-second timeout
        response = requests.get(Websit_url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises an exception for 4xx/5xx HTTP errors

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract and return the page title
        if soup.title and soup.title.string:
            title = soup.title.string.strip()
            print(f"Successfully extracted title: {title}")
            return title
        else:
            print("No <title> tag found on the website.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL '{Websit_url}': {e}")
        return None

