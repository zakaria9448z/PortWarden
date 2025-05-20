<p align="center"><img src="https://raw.githubusercontent.com/nfs-tech-bd/PortWarden/refs/heads/main/logo.png" hight="300" width="300" alt="LOGO" border="0"></p>                                                                                                                         
                                                                                        
# 🔐 PortWarden – The Stealthy Port Scanner

> ⚡ Fast, threaded, and hacker-friendly TCP port scanner written in Python

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg )](https://www.python.org/ )
[![Build](https://img.shields.io/badge/status-active-brightgreen.svg )](https://github.com/biplo8/portwarden )

---

## 🛠 What is PortWarden?

**PortWarden** is a powerful network reconnaissance tool designed for ethical hackers and penetration testers. It scans all 65,535 TCP ports using multi-threading, identifies known services running on open ports, and saves results in structured JSON format.

> Perfect for CTFs, bug bounty hunting, or learning how network scanning works under the hood.

---

## 🌟 Features

✅ Multi-threaded scanning (up to 300 threads)  
✅ Real-time open port detection  
✅ Live progress bar with ETA  
✅ Service name lookup for over 100+ common ports  
✅ Auto-saves results to `.json` file (`<target_ip>.json`)  
✅ Final summary: "Found X open ports"  

---

## 📦 Requirements

- Python 3.7+
- Standard libraries only (no external dependencies)

---

## 🚀 Usage

```bash
python port_scanner.py <host>
