import os
import socket
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.font import Font
from tkinter import ttk
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def get_network_ip():
    """Fetches the network IPv4 address of the machine."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Connect to an external server
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"  # Fallback to localhost if something goes wrong

class FileSharingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Sharing App")
        self.root.geometry("600x450")
        self.root.configure(bg="#F4F6F7")
        self.directory = ""
        self.server = None
        self.port = 8000
        self.server_link = ""
        self.create_styles()
        self.create_widgets()

    def create_styles(self):
        """Define styles for ttk widgets."""
        style = ttk.Style()
        style.theme_use("clam")
        
        # Custom button style with rounded corners
        style.configure("Rounded.TButton", 
                        padding=10, 
                        relief="flat", 
                        background="#2ECC71", 
                        foreground="white", 
                        font=("Helvetica", 10, "bold"))
        style.map("Rounded.TButton", 
                  background=[("active", "#28B463")],
                  foreground=[("active", "white")])
        
        style.configure("RedRounded.TButton",
                        background="#E74C3C")
        style.map("RedRounded.TButton",
                  background=[("active", "#C0392B")])
        
        style.configure("YellowRounded.TButton",
                        background="#F1C40F",
                        foreground="black")
        style.map("YellowRounded.TButton",
                  background=[("active", "#D4AC0D")])
        
        style.configure("PurpleRounded.TButton",
                        background="#9B59B6")
        style.map("PurpleRounded.TButton",
                  background=[("active", "#7D3C98")])

        style.configure("BlueRounded.TButton",
                        background="#3498DB")
        style.map("BlueRounded.TButton",
                  background=[("active", "#2E86C1")])

    def create_widgets(self):
        # Define fonts
        title_font = Font(family="Helvetica", size=20, weight="bold")
        label_font = Font(family="Helvetica", size=12)
        
        # Title
        tk.Label(self.root, text="File Sharing Application", font=title_font, 
                 fg="#2C3E50", bg="#F4F6F7").pack(pady=15)

        # Directory selection label
        self.directory_label = tk.Label(self.root, text="No directory selected", 
                                        fg="#E74C3C", font=label_font, bg="#F4F6F7")
        self.directory_label.pack(pady=10)

        # Browse button
        browse_button = ttk.Button(self.root, text="Browse Directory", 
                                   command=self.browse_directory, style="BlueRounded.TButton")
        browse_button.pack(pady=10)

        # Start/Stop server buttons
        self.start_button = ttk.Button(self.root, text="Start Server", 
                                        command=self.start_server, style="Rounded.TButton")
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(self.root, text="Stop Server", 
                                       command=self.stop_server, style="RedRounded.TButton")
        self.stop_button.pack(pady=10)

        # Status label
        self.status_label = tk.Label(self.root, text="", fg="#2C3E50", font=label_font, bg="#F4F6F7")
        self.status_label.pack(pady=10)

        # Copy link button (initially hidden)
        self.copy_button = ttk.Button(self.root, text="Copy Link", command=self.copy_link, 
                                      style="YellowRounded.TButton")
        self.copy_button.pack(pady=10)
        self.copy_button.pack_forget()  # Hide the button until the server is running

        # Info guide button
        info_button = ttk.Button(self.root, text="?", command=self.show_info_guide, 
                                 style="PurpleRounded.TButton")
        info_button.pack(side="left", padx=20, pady=10)

        # Exit button
        exit_button = ttk.Button(self.root, text="Exit", command=self.root.quit, 
                                 style="RedRounded.TButton")
        exit_button.pack(side="right", padx=20, pady=10)

    def browse_directory(self):
        self.directory = filedialog.askdirectory()
        if self.directory:
            self.directory_label.config(text=f"Directory: {self.directory}", fg="#2ECC71")
        else:
            self.directory_label.config(text="No directory selected", fg="#E74C3C")

    def start_server(self):
        if self.server:
            messagebox.showwarning("Warning", "Server is already running! Stop it before starting again.")
            return

        if not self.directory:
            messagebox.showerror("Error", "Please select a directory first!")
            return

        def run_server():
            os.chdir(self.directory)
            handler = SimpleHTTPRequestHandler
            self.server = TCPServer(("", self.port), handler)
            ip_address = get_network_ip()
            self.server_link = f"http://{ip_address}:{self.port}"
            self.status_label.config(text=f"Server is running at: {self.server_link}", fg="#2ECC71")
            self.copy_button.pack(pady=10)  # Show the copy button
            try:
                self.server.serve_forever()
            except Exception as e:
                print(f"Server stopped: {e}")

        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()

    def stop_server(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.server = None
            self.status_label.config(text="Server stopped.", fg="#E74C3C")
            self.copy_button.pack_forget()  # Hide the copy button
            messagebox.showinfo("Server Stopped", "Server has been stopped.")
        else:
            messagebox.showwarning("Warning", "Server is not running.")

    def copy_link(self):
        if self.server_link:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.server_link)
            self.root.update()  # Ensure the clipboard is updated
            messagebox.showinfo("Link Copied", "Server link has been copied to clipboard!")

    def show_info_guide(self):
        """Displays a guide on how to use the application."""
        guide_text = (
            "How to Use File Sharing Application:\n\n"
            "1. Make sure all devices are connected to the same Wi-Fi network.\n"
            "2. Turn off any VPNs, as they can interfere with the connection.\n"
            "3. Click 'Browse Directory' to select the folder you want to share.\n"
            "4. Click 'Start Server' to start sharing files. A link will be displayed.\n"
            "5. Share the link with users to download files. Click 'Copy Link' to copy it.\n"
            "6. To stop the server, click 'Stop Server'.\n\n"
            "Note: Users on the same network can access the files by pasting the link into their browser."
        )
        messagebox.showinfo("Information Guide", guide_text)

def main():
    root = tk.Tk()
    app = FileSharingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
