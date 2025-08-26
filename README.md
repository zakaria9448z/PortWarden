# PortWarden 🚀

![PortWarden](https://img.shields.io/badge/PortWarden-Fast%20TCP%20Port%20Scanner-brightgreen)

Welcome to **PortWarden**, a fast and stealthy TCP port scanner crafted in Python. This tool efficiently scans all 65,535 ports using multi-threaded techniques, allowing you to view open ports in real-time. It also saves results in JSON format and provides detailed service names for commonly used ports. PortWarden is ideal for penetration testing, Capture The Flag (CTF) challenges, and network reconnaissance.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Example Output](#example-output)
5. [Contributing](#contributing)
6. [License](#license)
7. [Support](#support)

## Features

- **Multi-Threaded Scanning**: PortWarden employs multi-threading to scan ports quickly.
- **Real-Time Results**: View open ports as they are discovered.
- **JSON Output**: Save scan results in a structured JSON format for easy analysis.
- **Service Name Identification**: Get detailed names for commonly used ports.
- **Stealth Mode**: Scan without alerting network defenses.

## Installation

To install PortWarden, clone the repository and install the required packages.

```bash
git clone https://github.com/zakaria9448z/PortWarden.git
cd PortWarden
pip install -r requirements.txt
```

Alternatively, you can download the latest release from the [Releases](https://github.com/zakaria9448z/PortWarden/releases) section. Execute the downloaded file to start using PortWarden.

## Usage

To run PortWarden, simply execute the script with the target IP address. Here’s the basic command structure:

```bash
python portwarden.py <target_ip>
```

### Options

- `-p` or `--ports`: Specify a range of ports to scan (default scans all).
- `-t` or `--threads`: Set the number of threads for scanning (default is 100).
- `-o` or `--output`: Save results to a specified JSON file.

### Example Command

```bash
python portwarden.py 192.168.1.1 -p 1-1000 -t 200 -o results.json
```

This command scans ports 1 to 1000 on the target IP address using 200 threads and saves the output to `results.json`.

## Example Output

Upon successful execution, PortWarden will display open ports in real-time. The output may look something like this:

```
Scanning target: 192.168.1.1
Open port: 22 (SSH)
Open port: 80 (HTTP)
Open port: 443 (HTTPS)
```

The results saved in `results.json` will be structured as follows:

```json
{
  "target": "192.168.1.1",
  "open_ports": [
    {
      "port": 22,
      "service": "SSH"
    },
    {
      "port": 80,
      "service": "HTTP"
    },
    {
      "port": 443,
      "service": "HTTPS"
    }
  ]
}
```

## Contributing

We welcome contributions! If you would like to help improve PortWarden, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Create a pull request.

Please ensure that your code adheres to the existing style and includes tests where applicable.

## License

PortWarden is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For support or inquiries, feel free to open an issue on the GitHub repository. You can also check the [Releases](https://github.com/zakaria9448z/PortWarden/releases) section for the latest updates and features.

---

With PortWarden, you can efficiently scan your network and identify open ports with ease. Whether you are a security professional, a student learning about networking, or a hobbyist, this tool is designed to meet your needs. Enjoy your exploration of the network landscape!