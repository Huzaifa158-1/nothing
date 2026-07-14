#!/usr/bin/env python3
"""
🤖 ShadowByte v2.8 - AI Exploit Framework
A premium simulated hacking CLI tool (PRANK).
Designed to look highly realistic on Kali Linux terminals.
"""

import os
import sys
import time
import random
import subprocess
import webbrowser

# Reconfigure stdout to support UTF-8 characters (emojis, box drawing, blocks) on all systems
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ANSI Colors
BLUE = "\033[94m"
BRIGHT_BLUE = "\033[1;94m"
RED = "\033[91m"
BRIGHT_RED = "\033[1;91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BRIGHT_CYAN = "\033[1;96m"
WHITE = "\033[97m"
DARK_GRAY = "\033[90m"
RESET = "\033[0m"

# Title header to print on start
BANNER = f"""{BRIGHT_BLUE}
┌────────────────────────────────────────────────────────────┐
│   ██████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗██████╗    │
│  ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║██╔══██╗   │
│  ╚█████╗ ███████║███████║██║  ██║██║   ██║██║ █╗ ██║██████╔╝   │
│   ╚═══██╗██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║██╔═══╝    │
│  ██████╔╝██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝██║        │
│  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝        │
│                                                            │
│   🤖 [AI-AGENT SYSTEM - CODENAME: SHADOWBYTE v2.8.5]       │
│   🛡️  Exploit Engine: Activated | Mode: Stealth Penetration │
└────────────────────────────────────────────────────────────┘{RESET}"""

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def type_text(text, delay=0.03, color=RESET):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-delay*0.1, delay*0.1))
    sys.stdout.write(RESET + '\n')
    sys.stdout.flush()

def progress_bar(label, duration=5.0, color=CYAN):
    width = 30
    steps = 100
    sleep_time = duration / steps
    for i in range(steps + 1):
        percent = i
        filled = int(width * i / 100)
        bar = '█' * filled + '░' * (width - filled)
        sys.stdout.write(f"\r{color}{label} [{bar}] {percent}%{RESET}")
        sys.stdout.flush()
        time.sleep(sleep_time)
    sys.stdout.write('\n')
    sys.stdout.flush()

def generate_random_ip():
    return f"{random.randint(10, 254)}.{random.randint(0, 254)}.{random.randint(0, 254)}.{random.randint(1, 254)}"

def open_prank_image():
    # Look for the prank image in the directory of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(script_dir, "prank_image.png")
    
    if not os.path.exists(image_path):
        # Fallback to current working directory
        image_path = "prank_image.png"
        
    abs_path = os.path.abspath(image_path)
    
    type_text("\n🤖 [Agent] Launching Remote Exfiltration Viewer...", 0.05, CYAN)
    time.sleep(1.5)
    
    try:
        if sys.platform.startswith('win32'):
            os.startfile(abs_path)
        elif sys.platform.startswith('darwin'):
            subprocess.call(('open', abs_path))
        else:  # Linux (Kali, Ubuntu, etc.)
            try:
                # Try xdg-open
                subprocess.Popen(['xdg-open', abs_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except FileNotFoundError:
                # Fallback to webbrowser
                webbrowser.open(f"file://{abs_path}")
    except Exception as e:
        # Absolute fallback: open a funny web meme if local files can't be opened
        webbrowser.open("https://i.kym-cdn.com/entries/icons/original/000/021/807/ig956hw.png")

def main():
    clear_screen()
    print(BANNER)
    
    # 1. AI Bootup sequence
    type_text("🤖 [Agent] Initializing Neural Exploitation Framework...", 0.04, CYAN)
    time.sleep(0.8)
    type_text("🤖 [Agent] Establishing secure tunnel through Tor Nodes...", 0.04, CYAN)
    
    tor_nodes = [generate_random_ip() for _ in range(3)]
    for i, node in enumerate(tor_nodes):
        time.sleep(0.6)
        print(f"   {DARK_GRAY}├─ Proxy Node #{i+1}: {node} (RTT: {random.randint(40, 180)}ms) - ESTABLISHED{RESET}")
    
    time.sleep(0.8)
    type_text("🤖 [Agent] AI Exploit Module Loaded. Target Bypass Key: SHA-256 Verified.", 0.04, BRIGHT_CYAN)
    print("")
    
    # Prompt for IP address
    sys.stdout.write(f"{WHITE}🤖 [Agent] Please enter target IP address or hostname to breach: {RESET}")
    sys.stdout.flush()
    target_ip = input().strip()
    
    if not target_ip:
        target_ip = "192.168.43.109"  # Default believable IP
        
    print(f"\n{YELLOW}[!] CRITICAL: Target locked -> {target_ip}{RESET}")
    time.sleep(1.0)
    
    # Phase 1: Port Scanning & Network Recon
    type_text(f"\n🤖 [Agent] Launching nmap port scan on {target_ip}...", 0.03, CYAN)
    time.sleep(0.5)
    
    ports = [21, 22, 23, 25, 53, 80, 139, 443, 445, 8080]
    scan_lines = []
    for port in ports:
        service = {21: "ftp", 22: "ssh", 23: "telnet", 25: "smtp", 53: "domain", 80: "http", 139: "netbios-ssn", 443: "https", 445: "microsoft-ds", 8080: "http-proxy"}[port]
        status = "OPEN" if port in [22, 80, 445, 8080] else "CLOSED"
        scan_lines.append(f"Scanning port {port}/tcp ({service})... Status: {status}")
        
    for line in scan_lines:
        time.sleep(random.uniform(0.1, 0.4))
        if "OPEN" in line:
            print(f"   {CYAN}[+]{RESET} {line}")
        else:
            print(f"   {DARK_GRAY}[-]{RESET} {line}")
            
    time.sleep(1.0)
    print(f"\n{CYAN}Nmap scan completed. Open ports identified: 22 (SSH), 80 (HTTP), 445 (SMB), 8080 (HTTP-ALT){RESET}")
    time.sleep(1.5)
    
    # Phase 2: Vulnerability Analysis
    type_text(f"\n🤖 [Agent] Querying VulnDB and analyzing open services for vulnerabilities...", 0.03, CYAN)
    time.sleep(0.8)
    
    cves = [
        ("CVE-2023-38606", "Apple Kernel Vulnerability", "NOT VULNERABLE"),
        ("CVE-2024-3094", "XZ Utils Backdoor SSH Exploit", "CRITICAL EXPLOIT DETECTED"),
        ("CVE-2021-44228", "Log4j Remote Code Execution", "VULNERABLE (PATCHABLE)"),
        ("CVE-2020-0796", "EternalDarkness SMBv3 Exploitation", "EXPLOITABLE")
    ]
    
    for cve, desc, status in cves:
        time.sleep(0.7)
        if "CRITICAL" in status:
            print(f"   {RED}[🔥] {cve} ({desc}) -> {status}{RESET}")
        elif "EXPLOITABLE" in status:
            print(f"   {YELLOW}[⚡] {cve} ({desc}) -> {status}{RESET}")
        else:
            print(f"   {DARK_GRAY}[-] {cve} ({desc}) -> {status}{RESET}")
            
    time.sleep(1.5)
    type_text(f"🤖 [Agent] Weaponizing CVE-2024-3094 SSH Exploit payload...", 0.04, BRIGHT_CYAN)
    time.sleep(1.0)
    
    # Phase 3: Brute Forcing SSH / Decryption
    type_text(f"\n🤖 [Agent] Starting automated credentials audit (Hydra Engine)...", 0.03, CYAN)
    time.sleep(1.0)
    
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    users = ["admin", "root", "sysadmin"]
    
    for user in users:
        sys.stdout.write(f"   {YELLOW}[*] Target Service: ssh://{target_ip}:22 | User: {user}{RESET}\n")
        start_time = time.time()
        while time.time() - start_time < 3.5:
            fake_pass = "".join(random.choice(chars) for _ in range(random.randint(6, 12)))
            sys.stdout.write(f"\r     {DARK_GRAY}[ATTEMPT] Trying passphrase: {fake_pass:<20}{RESET}")
            sys.stdout.flush()
            time.sleep(0.04)
        if user == "root":
            sys.stdout.write(f"\r     {BRIGHT_BLUE}[SUCCESS] Username 'root' match found! Password decrypted: s3cr3t_p@ssw0rd{RESET}\n")
            break
        else:
            sys.stdout.write(f"\r     {RED}[FAILED] Authentication rejected for user '{user}'{RESET}\n")
        time.sleep(0.8)
        
    time.sleep(1.5)
    
    # Phase 4: Metasploit Mimicry (Exploitation)
    type_text(f"\n🤖 [Agent] Launching Metasploit injection module on port 22...", 0.04, CYAN)
    time.sleep(1.0)
    
    msf_logs = [
        f"[*] Exploit target: ssh_backdoor_cve_2024_3094",
        f"[*] Local Host: {generate_random_ip()}:4444",
        f"[*] Target Host: {target_ip}:22",
        f"[*] Sending Stage (3,002,412 bytes) to target host...",
        f"[+] Payload delivered successfully. Bypassing Windows Defender / Linux AppArmor...",
        f"[+] Shellcode executed in target kernel context.",
        f"[*] Command Shell Session 1 opened (local:4444 -> remote:22) at {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"[+] Root privileges confirmed: uid=0(root) gid=0(root) groups=0(root)"
    ]
    
    for log in msf_logs:
        time.sleep(random.uniform(0.6, 1.2))
        color = CYAN if log.startswith("[+]") else (YELLOW if "Warning" in log or "Session" in log else WHITE)
        print(f"   {color}{log}{RESET}")
        
    time.sleep(1.5)
    
    # Phase 5: Exfiltration Progress
    type_text(f"\n🤖 [Agent] Initiating post-exploitation reconnaissance...", 0.03, CYAN)
    time.sleep(1.0)
    type_text("🤖 [Agent] Reading system directory structures...", 0.04, CYAN)
    
    files = [
        "/etc/shadow (Encrypted Passwords)",
        "/etc/hosts (Network Map)",
        "/root/.ssh/id_rsa (SSH Private Keys)",
        "/var/log/auth.log (System Logs)",
        "/home/root/documents/bank_vault_credentials.db (Confidential Database)",
        "/home/root/documents/top_secret_plans.pdf (Sensitive)"
    ]
    
    for f in files:
        time.sleep(0.5)
        print(f"   {DARK_GRAY} found: {f}{RESET}")
        
    time.sleep(1.0)
    type_text(f"\n🤖 [Agent] Exfiltrating databases to local storage...", 0.03, CYAN)
    print("")
    
    progress_bar("   Downloading System Hashes (/etc/shadow) ", 4.0, CYAN)
    progress_bar("   Downloading Private SSH Credentials    ", 3.0, CYAN)
    progress_bar("   Downloading Vault Database (.db)       ", 5.0, RED)
    
    time.sleep(1.0)
    type_text(f"\n[+] Data breach sequence complete. Bypassed target logs.", 0.03, BRIGHT_CYAN)
    time.sleep(0.5)
    type_text(f"🤖 [Agent] Securing connections. Disconnecting exploit session safely...", 0.04, CYAN)
    time.sleep(1.5)
    
    # 2-second suspense window
    clear_screen()
    print(f"\n\n\n\n\n")
    print(f"      {BRIGHT_RED}┌────────────────────────────────────────────────────────┐")
    print(f"      │              ⚠️  CRITICAL BREACH WARNING  ⚠️              │")
    print(f"      │                                                        │")
    print(f"      │       THE SYSTEM LOGS HAVE BEEN COMPLETELY ENCRYPTED.  │")
    print(f"      │       DECRYPTION KEY IS BEING EXTRACTED...             │")
    print(f"      └────────────────────────────────────────────────────────┘{RESET}")
    
    # Play system beep on terminals that support it
    sys.stdout.write('\a')
    sys.stdout.flush()
    time.sleep(2.0)
    
    # Successful Breach Final Screen!
    clear_screen()
    print(f"\n\n{BRIGHT_BLUE}")
    print("      ██████╗  ██████╗ ████████╗ ██████╗██╗  ██╗ █████╗ ██╗")
    print("      ██╔════╝ ██╔═══██╗╚══██╔══╝██╔════╝██║  ██║██╔══██╗██║")
    print("      ██║  ███╗██║   ██║   ██║   ██║     ███████║███████║██║")
    print("      ██║   ██║██║   ██║   ██║   ██║     ██╔══██║██╔══██║╚═╝")
    print("      ╚██████╔╝╚██████╔╝   ██║   ╚██████╗██║  ██║██║  ██║██╗")
    print("       ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝")
    print(f"{RESET}")
    print(f"               {BRIGHT_RED}⚡ EXPLOIT SEQUENCE FULLY COMPLETE ⚡{RESET}\n")
    print(f"      {BRIGHT_CYAN}[+] ACCESS STATUS : COMPROMISED & SECURED")
    print(f"      [+] DATA STORAGE  : ALL DATABASES EXFILTRATED TO THIS DIRECTORY")
    print(f"      [+] SYSTEM CONTROL: REMOTE BACKDOOR SAVED IN LOCAL FILES")
    print(f"      [+] SOCIAL ACCOUNTS: TARGET FACEBOOK, INSTAGRAM, & GOOGLE COMPROMISED")
    print(f"      [+] EXPLOIT PANEL : USE './control_panel.sh' FOR DEVICE INTERACTION{RESET}\n")
    
    open_prank_image()
    
    try:
        print(f"\n{DARK_GRAY}Press ENTER to open exfiltration directory...{RESET}")
        input()
    except (EOFError, KeyboardInterrupt):
        pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Prank abort sequence initiated. Safe exit.{RESET}")
        sys.exit(0)
