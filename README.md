
# 📥 Databricks DBFS Downloader GUI

A simple GUI tool (for macOS and Windows) to connect to a Databricks workspace and download files from DBFS (Databricks File System) directly to your local machine.

This tool supports both **token-based** and **external browser-based** authentication, and provides an easy interface to specify the DBFS path and local destination.

---

## ✨ Features

- ✅ GUI-based interface using `tkinter`
- 🔐 Supports **Personal Access Token (PAT)** or **External Browser Authentication**
- 📂 Browse and select destination file path
- 💾 Download large files from DBFS in chunks
- 🖥 Available as standalone apps for **macOS** and **Windows**
- 🐍 Python script also available for advanced users

---

## 📦 Download

You can use the standalone apps:

- **Windows**: `Databricks_DBFS_Downloader.exe`
- **macOS**: `Databricks_DBFS_Downloader.zip`

> ✅ No need to install Python or dependencies — just run the app directly.

---

## 🧪 For Python Users

If you prefer using the Python script:

### 🔧 Requirements

- Python 3.8+
- Install dependencies:

```bash
pip install databricks-sdk
```

### ▶️ Run the Script

```bash
python dbfs_downloader.py
```

---

## 🖼 Screenshot

*(Insert screenshot of the app window here, if desired)*

---

## ⚠️ Notes

- Ensure your **Databricks host URL** starts with `https://` and includes your workspace info.
- If using **browser-based authentication**, a browser window will open to complete login.
- Make sure the destination file path is valid and writable on your system.

---

## 📬 Contact

If you encounter any issues, feel free to contact:

**Siddhart Singh**  
📧 siddharthsingh5010@icloud.com

---

## 🏷 Version

**v1.0**

---

## 👨‍💻 Author

**Siddhart Singh**
