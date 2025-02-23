**Kasongo2** is an advanced upgrade from **KasongoDDoS**, rewritten in Python for improved performance, flexibility, and enhanced attack capabilities. Designed for educational and security research purposes, Kasongo2 implements a multithreaded approach to generate high-volume HTTP requests, simulating real-world stress testing scenarios.  

Key features include:  
- **Tor Support:** Optional integration with the Tor network for anonymized traffic (requires PySocks).  
- **Randomized User-Agent Rotation:** Helps bypass basic anti-bot protections.  
- **Threaded Attack Mechanism:** Enables high concurrency for better efficiency.  
- **Improved Error Handling:** Prevents crashes and ensures stable execution.  

Kasongo2 is optimized for performance, making it a powerful tool for understanding denial-of-service (DoS) attack methodologies while emphasizing responsible and ethical usage. 🚀

### **Steps to Run Kasongo2 on Kali Linux**  

#### **1. Install Required Dependencies**  
Ensure Python is installed and install `PySocks` if you plan to use Tor.  

```bash
sudo apt update && sudo apt install python3 python3-pip -y
pip3 install pysocks
```

#### **2. Download Kasongo2**  
Clone the repository or download the script manually.  

```bash
git clone https://github.com/your-repo/kasongo2.git
cd kasongo2
```

#### **3. Start the Tor Service (Optional for Tor Mode)**  
If using Tor, ensure the Tor service is running.  

```bash
sudo apt install tor -y
sudo systemctl start tor
sudo systemctl enable tor
```

#### **4. Run Kasongo2**  
Execute the script with the required parameters:  

```bash
python3 kasongo2.py <target> <port> <connections> <useTor[true/false]>
```

**Example Usage:**  
- Without Tor:  
  ```bash
  python3 kasongo2.py example.com 80 50 false
  ```
- With Tor:  
  ```bash
  python3 kasongo2.py example.com 80 50 true
  ```

#### **5. Stop the Attack**  
To stop the script, press **`CTRL + C`** in the terminal. If using Tor, you can stop it with:  

```bash
sudo systemctl stop tor
```
