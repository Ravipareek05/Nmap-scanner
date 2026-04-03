# 🔍 Python Nmap Scanner

A simple command-line based Nmap scanner written in Python. This tool automates basic port scanning tasks using Nmap and is intended for learning and authorized penetration testing.

---

## 🚀 Features

- Scan open ports on a target
- Supports multiple scan types (SYN, UDP, Full scan)
- Custom port range
- Save scan results to a file
- Simple CLI interface

---

## 🔧 Requirements

- Python 3.x
- Nmap installed

---

## 📦 Installation

```bash
git clone https://github.com/Ravipareek05/Nmap-scanner
cd Nmap-scanner
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Usage

**Basic scan:**
```bash
sudo python scanner.py -t scanme.nmap.org
```

**Custom port range:**
```bash
sudo python scanner.py -t 127.0.0.1 -p 20-100
```

**Save output to file:**
```bash
sudo python scanner.py -t 127.0.0.1 -o results/output.txt
```

---

## 📄 Sample Scan Result

Example output from scanning localhost:

```
Host: 127.0.0.1 is up
Protocol: tcp
Port 22: open (ssh)
Port 80: open (http)
```

---

## 🎬 Demo

```
(venv) ravipareek@Ravis-MacBook-Air Nmap % sudo python scanner.py -t 127.0.0.1 -p 20-100 -o results/local_scan.txt
Password:
============================
  Python Nmap Scanner
============================
Target: 127.0.0.1
Ports: 20-100
Scan type: syn
============================

Starting scan...

Nmap version: (7, 90)
Host: 127.0.0.1 is up

Protocol: tcp
Port 22: open (ssh)
```

---

## 🗂️ Project Structure

```
nmap-scanner/
├── scanner.py
├── README.md
├── requirements.txt
├── .gitignore
├── results/
│   └── local_scan.txt
├── docs/
│   ├── usage.md
│   └── screenshots/
│       └── image.png
```

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐
