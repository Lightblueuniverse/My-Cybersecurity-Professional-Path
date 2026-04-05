# Simple Network Scanner 🌐

A lightweight Python script designed to perform a basic scan of a local network using system commands.

## 🚀 Description

This project is a simple automation tool that utilizes the **ICMP (Ping)** protocol to verify which devices are active within a specific range of IP addresses on a local network.

I built this to practice Python's interaction with OS-level commands and network fundamentals as part of my Cybersecurity learning journey.

## 🛠️ Technologies

* **Python 3.x**
* **`os` & `platform` libraries**: Used to execute system commands and ensure cross-platform compatibility (Windows, Linux, and macOS).

## 📋 How It Works

The script iterates through a range of numbers (1-10) to construct IP addresses. It then triggers a `ping` command:

- **Exit Code 0**: The device is reachable.
- **Non-zero Exit Code**: The device is offline or blocking ICMP requests.

## ⚙️ Installation & Usage

1. **Clone the entire repository:**
   ```bash
   git clone https://github.com/lightblueuniverse/Cybersecurity-Professional-Path.git
2. **Navigate to this specific project folder:**
   ```bash
   cd "02-Security-Automation-Scripts/01-Network-Ping-Sweeper"
3. **Run the script:**
   ```bash
   python3 ping_sweeper.py

## 💻 Compatibility

The script automatically detects your Operating System and adjusts the ping parameters:

- Windows: Uses -n 1
- Linux/macOS: Uses -c 1

⚡ Project created for educational purposes in network automation and cybersecurity. Always ensure you have permission to scan a network.
