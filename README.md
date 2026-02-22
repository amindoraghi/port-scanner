# Advanced Port Scanner

A fast and simple multithreaded port scanner built with Python.  
This project is designed for learning networking fundamentals, socket programming, and basic cybersecurity concepts.

---

## 🚀 Features
- Multithreaded scanning for high speed  
- Custom port range selection  
- Clean and minimal output  
- Beginner‑friendly code structure  
- Fully written in Python using the built‑in `socket` module  

---

## 📌 How It Works
The scanner attempts to connect to each port in the selected range.  
If the connection is successful, the port is considered **open**.  
If not, it is marked as **closed** or filtered.

---

## 🛠 Usage

Run the script:

```bash
python port_scanner.py

You will be asked to enter:

1.Target IP address 

2.Start port

3.End port

For example

Enter target IP: 8.8.8.8
Start port: 1
End port: 100




⚠ Disclaimer
This tool is for educational and ethical testing only.
Do NOT scan systems you do not own or do not have explicit permission to test.
