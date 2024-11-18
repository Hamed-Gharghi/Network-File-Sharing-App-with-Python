# Network File Sharing App with Python

![Python version](https://img.shields.io/badge/python-3.6%2B-blue) ![GitHub license](https://img.shields.io/github/license/Hamed-Gharghi/Network-File-Sharing-App) ![GitHub stars](https://img.shields.io/github/stars/Hamed-Gharghi/Network-File-Sharing-App?style=social) ![](https://komarev.com/ghpvc/?username=Hamed-Gharghi&color=green&style=flat-square) ![Version](https://img.shields.io/badge/version-1.0.0-brightgreen)

## Overview

**Network File Sharing App** is a Python-based tool designed to allow users to share files easily over a local network. This app runs a simple HTTP server and provides a user-friendly graphical interface for selecting directories, starting/stopping the server, and sharing files with other devices on the same network.

### Key Features

- **Easy File Sharing**: Share files and directories over your local network using a simple HTTP server.
- **Graphical User Interface (GUI)**: An intuitive interface to easily start and stop the file sharing server.
- **Network Link**: Displays the network IP address for easy access from other devices.
- **Link Copying**: A button to easily copy the server URL for sharing with others.
- **Cross-Platform Support**: Compatible with Windows, macOS, and Linux.

## Badges

- **Build Status**: ![Build Status](https://img.shields.io/github/workflow/status/Hamed-Gharghi/Network-File-Sharing-App/CI)
- **Version**: ![Version](https://img.shields.io/badge/version-1.0.0-brightgreen)
- **License**: ![License](https://img.shields.io/github/license/Hamed-Gharghi/Network-File-Sharing-App)

## Tags

- **File Sharing**
- **Network Tools**
- **Python GUI**
- **HTTP Server**
- **Cross-Platform**
- **Local Network**

## Python Version

- **Python 3.6 or higher** is required to run this application. Ensure your Python environment meets this requirement.

## Getting Started

Follow these steps to set up and use the Network File Sharing App:

### Clone the Repository

```sh
git clone https://github.com/Hamed-Gharghi/Network-File-Sharing-App.git
cd Network-File-Sharing-App
```

### Install Dependencies

1. Make sure to install the required dependencies.

#### On Ubuntu

If you're using Ubuntu or any other Linux-based OS, you can install the dependencies with the following command:

```sh
pip install -r requirements.txt
```

#### On Windows

If you're using Windows, the process is the same. Open a Command Prompt or PowerShell window, navigate to your project directory, and run:

```sh
pip install -r requirements.txt
```

### Running the Application

1. **Activate Virtual Environment** (if using `myenv`):

   - **Linux/macOS**:
     ```sh
     source myenv/bin/activate
     ```
   - **Windows**:
     ```sh
     myenv\Scripts\activate
     ```

2. **Run the Application**:
   ```sh
   python file_sharing_network_gui.py
   ```

   This will start the server and display a link to access the shared files.

3. **GUI**:
   - Use the "Start Server" button to start the file sharing server.
   - The server link (your local network IP address) will appear below the button. 
   - You can copy this link using the "Copy Link" button to easily share it with others on the same network.

4. **Stop the Server**:
   - Click "Stop Server" to stop the running server.

### How to Use

- **Connect to the same WiFi network**: Ensure all devices are connected to the same local network.
- **Turn off VPNs**: VPNs may block local network connections, so they should be disabled.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

We welcome contributions to improve the Network File Sharing App. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. Your help is much appreciated!

## Contact

- **Author**: Hamed Gharghi
- **Email**: [Hamedgharghi1@gmail.com](mailto:Hamedgharghi1@gmail.com)
- **GitHub Profile**: [Hamed-Gharghi](https://github.com/Hamed-Gharghi)

## Additional Resources

- **Python Documentation**: [https://docs.python.org/](https://docs.python.org/)
- **Tkinter Documentation**: [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)

---

Thank you for using the Network File Sharing App! If you have any questions or feedback, feel free to reach out through the contact details provided above.
