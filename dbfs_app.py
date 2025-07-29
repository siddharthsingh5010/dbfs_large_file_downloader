import tkinter as tk
from tkinter import filedialog, messagebox

# Auto-install databricks-sdk if not present
try:
    from databricks.sdk import WorkspaceClient
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "databricks-sdk"])
    from databricks.sdk import WorkspaceClient  # retry import

from databricks.sdk.core import Config
import pathlib
import base64

# Global Client object
dbx_client = None

def connect_with_token():
    global dbx_client
    try:
        config = Config(
            host=host_entry.get(),
            token=token_entry.get(),
            auth_type="pat"
        )
        dbx_client = WorkspaceClient(config=config)
        dbx_client.current_user.me()  # verify connection
        messagebox.showinfo("Connection", "Successfully connected using token!")
    except Exception as e:
        messagebox.showerror("Connection Error", f"Token authentication failed:\n{str(e)}")

def connect_with_browser():
    global dbx_client
    try:
        config = Config(
            host=host_entry.get(),
            auth_type="external-browser"
        )
        dbx_client = WorkspaceClient(config=config)
        dbx_client.current_user.me()  # verify connection
        messagebox.showinfo("Connection", "Successfully authenticated via browser!")
    except Exception as e:
        messagebox.showerror("Connection Error", f"Browser authentication failed:\n{str(e)}")

def browse_destination():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("All Files", "*.*")]
    )
    if file_path:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(0, file_path)

def download_file():
    global dbx_client

    if not dbx_client:
        messagebox.showerror("Not Connected", "Please connect to Databricks first.")
        return

    dbfs_path = dbfs_entry.get()
    destination_path = destination_entry.get()

    if not dbfs_path or not destination_path:
        messagebox.showwarning("Missing Info", "Please enter both DBFS path and destination path.")
        return

    try:
        local_path = pathlib.Path(destination_path)
        offset = 0
        MAX_CHUNK = 1 * 1024 * 1024  # 1MB

        with open(local_path, "wb") as f:
            while True:
                resp = dbx_client.dbfs.read(path=dbfs_path, offset=offset, length=MAX_CHUNK)
                if not resp.data:
                    break
                chunk = base64.b64decode(resp.data)
                f.write(chunk)
                offset += len(chunk)

        messagebox.showinfo("Success", f"Downloaded to:\n{local_path.resolve()}")
    except Exception as e:
        messagebox.showerror("Download Error", f"Failed to download file:\n{str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Databricks DBFS Downloader")
root.geometry("650x360")

tk.Label(root, text="Databricks Host URL:").pack()
host_entry = tk.Entry(root, width=80)
host_entry.pack()
host_entry.insert(0, "https://adb-xxxxx.azuredatabricks.net")

tk.Label(root, text="Personal Access Token (optional):").pack()
token_entry = tk.Entry(root, width=80, show="*")
token_entry.pack()

# DBFS Path
tk.Label(root, text="DBFS File Path (e.g., dbfs:/FileStore/abc.csv):").pack()
dbfs_entry = tk.Entry(root, width=80)
dbfs_entry.pack()

# Destination Path
tk.Label(root, text="Destination File Path:").pack()
destination_entry = tk.Entry(root, width=80)
destination_entry.pack()

browse_button = tk.Button(root, text="Browse...", command=browse_destination)
browse_button.pack(pady=3)

# Auth Buttons
auth_frame = tk.Frame(root)
auth_frame.pack(pady=6)

connect_button = tk.Button(auth_frame, text="Connect with Token", command=connect_with_token, width=25)
connect_button.grid(row=0, column=0, padx=10)

browser_auth_button = tk.Button(auth_frame, text="External Browser Authentication", command=connect_with_browser, width=30)
browser_auth_button.grid(row=0, column=1, padx=10)

# Download Button
download_button = tk.Button(root, text="Download File", command=download_file)
download_button.pack(pady=10)

# Footer / Contact Info
footer_label = tk.Label(
    root,
    text="In case of any error contact Siddhart Singh (siddharthsingh5010@icloud.com)\nVersion 1.0",
    font=("Arial", 9),
    fg="gray"
)
footer_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()