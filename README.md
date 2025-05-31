
# 🔁 Zoom Bulk Joiner (For Educational Use Only)

This Python script automates the process of **joining a Zoom meeting with multiple attendees using different display names**, primarily using **Selenium WebDriver**.

> ⚠️ **Disclaimer**: This project is developed for **fun and educational purposes only**. It is not affiliated with or endorsed by Zoom, and should not be used for any malicious or unauthorized activities.

---

## 🚀 Features

- Join Zoom meeting by:
  - ✅ Meeting ID and password
  - ✅ Direct meeting link
- Loads multiple names from `names.txt`
- Automatically fills display name and password
- Mutes audio by default
- Skips Zoom app download by using **"Join from Your Browser"**
- Keeps each session open in a new tab (Chrome stays open)

---

## 📦 Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (compatible with your Chrome version)
- Internet connection
- Zoom meeting with "Join from Browser" enabled

---

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/zoom-bulk-joiner.git
cd zoom-bulk-joiner
````

2. Install dependencies:

```bash
pip install selenium
```

3. Make sure `chromedriver` is in your system PATH or same folder as the script.

4. Create a `names.txt` file with one name per line, like:

```
John Doe
Jane Smith
Test Bot 1
```

---

## ▶️ Usage

Run the script:

```bash
python zoom_bulk_joiner.py
```

Choose an option:

* 1: Join using **Meeting ID + Password**
* 2: Join using **Meeting Link**

---

## 📁 File Structure

```
zoom-bulk-joiner/
├── zoom_bulk_joiner.py      # Main script
├── names.txt                # Names to use for joining
└── README.md                # You're reading it!
```

---

## 👮 Disclaimer

> This project was developed by **Fuad Ahammed** for fun and educational exploration only.
> Use responsibly. Don't spam or violate Zoom’s Terms of Service.
> The author is **not liable** for any misuse or consequences arising from the use of this tool.

---

## 🧠 Author

**Fuad Ahammed**
[GitHub](https://github.com/fuadahammed101)

