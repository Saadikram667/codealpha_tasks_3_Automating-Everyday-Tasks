# codealpha_tasks_3_Automating-Everyday-Tasks

```markdown
# 🛠️ Python Automation Suite (CodeAlpha - Task 3)

A Python automation toolkit built to simplify common file system operations, text processing, and web page data extraction.

This project was created as part of the **CodeAlpha** Python Programming Internship.

---

## 📌 Features

### 1. File & Directory Manager (`img_mover`)
* **Flexible Operations:** Handles both individual files and entire directory structures.
* **Smart Directory Handling:** Automatically creates missing parent directories using `pathlib.Path`.
* **Metadata Preservation:** Uses `shutil.copy2` to preserve file creation timestamps and attributes during copy operations.
* **Safe Error Handing:** Validates source paths prior to execution to avoid runtime crashes.

### 2. Email Address Extractor (`email_extractor`)
* **Regex Pattern Matching:** Scans text documents line-by-line using regular expressions (`re.findall`).
* **Deduplication:** Utilizes a Python `set` structure to filter out duplicate addresses automatically.
* **Organized Output:** Exports unique emails in alphabetical order (`sorted()`) to a targeted text file.

### 3. Web Title Scraper (`website_titles`)
* **URL Normalization:** Ensures `https://` protocol prefixes are added automatically.
* **Browser Emulation:** Sends standard browser `User-Agent` headers to prevent HTTP 403 Forbidden blocks.
* **HTML Parsing:** Extracts clean `<title>` contents using `BeautifulSoup`.
* **Robust Networking:** Features explicit timeouts (10s) and exception handling for invalid URLs, HTTP errors, or timeouts.

---

## 📂 Project Structure

```text
├── Task_3_Automation_with_Python_Scripts.py   # Main Python automation module
├── README.md                                  # Project documentation
└── requirements.txt                           # Project dependencies

```

---

## ⚙️ Installation & Setup

### Prerequisites

* Python 3.8 or higher installed on your system.

### Install Dependencies

Install the required third-party libraries using `pip`:

```bash
pip install requests beautifulsoup4

```

---

## 🚀 Usage Guide

Import the functions into your Python script or interactive session:

```python
from Task_3_Automation_with_Python_Scripts import (
    img_mover,
    email_extractor,
    website_titles
)

# 1. Copy or Move Files/Folders
img_mover("source_folder", "destination_folder")

# 2. Extract Unique Emails from a File
email_extractor("raw_text_report.txt", "output/extracted_emails.txt")

# 3. Fetch Web Page Title
title = website_titles("[https://www.codealpha.tech](https://www.codealpha.tech)")
print("Page Title:", title)

```

---

## 🎬 Video Explanation

To make this project easy to understand, a complete slide-by-slide explanation video was generated using **Claude AI**. The video visually breaks down:

* Module imports (`shutil`, `pathlib`, `re`, `requests`, `bs4`).
* Code execution flow and logic for each tool.
* Demonstration of error handling and real terminal outputs.

---

## 🤝 Acknowledgments

* **CodeAlpha** for providing the internship task framework.
* **Claude AI** for assistance in producing the visual presentation walkthrough.

```

```
