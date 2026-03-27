# =========================
# IT Problem Simulator
# Full GUI + CLI Hybrid Version
# By Agus Satria Adhitama
# =========================

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import random
import time
import threading
import os
import sys

# ====================================
# Utilities
# ====================================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def simulate_loading(text="Processing", duration=3):
    for _ in range(duration):
        for dot in ['.', '..', '...']:
            print(f"{text}{dot}", end='\r')
            time.sleep(0.4)
    print(' ' * 30, end='\r')  # clear line

def log_event(event):
    with open("simulator_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {event}\n")

def random_tip():
    tips = [
        "Cek kabel LAN atau WiFi",
        "Restart router untuk koneksi stabil",
        "Pastikan printer menyala",
        "Close aplikasi yang tidak perlu",
        "Bersihkan cache untuk performa maksimal",
        "Restart komputer untuk performa optimal",
        "Periksa konfigurasi software",
        "Periksa update terbaru aplikasi",
        "Cek kapasitas storage yang tersedia",
        "Monitor penggunaan CPU & memory"
    ]
    return random.choice(tips)

# ====================================
# GUI Enhancement Utilities
# ====================================
def gradient_frame(frame, color1, color2):
    """Create a vertical gradient background"""
    canvas = tk.Canvas(frame, width=400, height=550)
    canvas.pack(fill="both", expand=True)
    limit = 400
    for i in range(limit):
        r1, g1, b1 = frame.winfo_rgb(color1)
        r2, g2, b2 = frame.winfo_rgb(color2)
        r = int(r1 + (r2-r1) * i/limit) >> 8
        g = int(g1 + (g2-g1) * i/limit) >> 8
        b = int(b1 + (b2-b1) * i/limit) >> 8
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0,i,400,i,fill=color)
    return canvas

def popup_message(title, message, kind="info"):
    if kind=="info":
        messagebox.showinfo(title, message)
    elif kind=="warning":
        messagebox.showwarning(title, message)
    elif kind=="error":
        messagebox.showerror(title, message)

# ====================================
# Error Simulation Functions
# ====================================
def internet_error():
    slow_print("\nConnecting to network...", 0.02)
    simulate_loading("Checking network", 3)
    slow_print("❌ ERROR: No Internet Connection")
    slow_print(f"💡 Tip: {random_tip()}\n")
    log_event("Simulated Internet Error")
    popup_message("Internet Error", f"❌ No Internet Connection\n💡 Tip: {random_tip()}", "error")

def printer_error():
    slow_print("\nSending data to printer...", 0.02)
    simulate_loading("Printer communication", 3)
    slow_print("🖨️ ERROR: Printer Not Responding")
    slow_print(f"💡 Tip: {random_tip()}\n")
    log_event("Simulated Printer Error")
    popup_message("Printer Error", f"🖨️ Printer Not Responding\n💡 Tip: {random_tip()}", "error")

def app_crash():
    slow_print("\nLaunching application...", 0.02)
    simulate_loading("Loading app", 3)
    slow_print("⚠️ ERROR: Application Not Responding")
    slow_print(f"💡 Tip: {random_tip()}\n")
    log_event("Simulated Application Crash")
    popup_message("Application Crash", f"⚠️ Application Not Responding\n💡 Tip: {random_tip()}", "error")

def disk_full_error():
    slow_print("\nWriting data to disk...", 0.02)
    simulate_loading("Checking disk space", 3)
    slow_print("💾 ERROR: Disk Full")
    slow_print(f"💡 Tip: {random_tip()}\n")
    log_event("Simulated Disk Full Error")
    popup_message("Disk Full", f"💾 Disk Full\n💡 Tip: {random_tip()}", "error")

def memory_error():
    slow_print("\nAllocating memory for app...", 0.02)
    simulate_loading("Memory check", 3)
    slow_print("⚠️ ERROR: Not Enough Memory")
    slow_print(f"💡 Tip: {random_tip()}\n")
    log_event("Simulated Memory Error")
    popup_message("Memory Error", f"⚠️ Not Enough Memory\n💡 Tip: {random_tip()}", "error")

def cpu_overload():
    slow_print("\nRunning heavy computation...", 0.02)
    simulate_loading("CPU load simulation", 3)
    slow_print("🔥 WARNING: CPU Overload Detected")
    slow_print(f"💡 Tip: {random_tip()}\n")
    log_event("Simulated CPU Overload")
    popup_message("CPU Overload", f"🔥 CPU Overload Detected\n💡 Tip: {random_tip()}", "warning")

def network_fluctuation():
    slow_print("\nMonitoring network...", 0.02)
    simulate_loading("Analyzing connection", 3)
    slow_print("🌐 WARNING: Network Fluctuation Detected")
    slow_print(f"💡 Tip: {random_tip()}\n")
    log_event("Simulated Network Fluctuation")
    popup_message("Network Fluctuation", f"🌐 Network Fluctuation Detected\n💡 Tip: {random_tip()}", "warning")

# ====================================
# Training Mode GUI
# ====================================
def training_mode():
    training_window = tk.Toplevel()
    training_window.title("Training Mode")
    training_window.geometry("500x400")
    
    questions = [
        {"q": "Internet tidak jalan, apa yang pertama kali dilakukan?", "a": ["Cek kabel", "Restart router", "Ping", "Hubungi admin"]},
        {"q": "Printer tidak merespon, solusi paling cepat?", "a": ["Cek kabel printer", "Hidupkan printer", "Restart service printer", "Hubungi teknisi"]},
        {"q": "Aplikasi crash terus, langkah pertama?", "a": ["Close app", "Restart PC", "Check logs", "Update app"]},
        {"q": "CPU tiba-tiba overload, langkah cepat?", "a": ["Close app", "Monitor task manager", "Restart PC", "Upgrade CPU"]},
        {"q": "Disk penuh, tindakan cepat?", "a": ["Hapus file sementara", "Move file ke external", "Restart PC", "Format disk"]}
    ]
    
    def check_answer(q_idx, ans_idx):
        if ans_idx in [0,1]:
            result_label.config(text="✅ Good choice!", fg="green")
        else:
            result_label.config(text="⚠️ Maybe better next time.", fg="red")
        log_event(f"Training Q{q_idx+1} attempted: Option {ans_idx+1}")
    
    row_idx = 0
    for i, q in enumerate(questions):
        tk.Label(training_window, text=f"Q{i+1}: {q['q']}", wraplength=450, justify="left").grid(row=row_idx, column=0, sticky="w", pady=5)
        row_idx += 1
        for j, option in enumerate(q["a"]):
            btn = tk.Button(training_window, text=option, command=lambda q_idx=i, ans_idx=j: check_answer(q_idx, ans_idx))
            btn.grid(row=row_idx, column=j, padx=5, pady=5)
        row_idx += 1
    result_label = tk.Label(training_window, text="", font=("Arial", 12))
    result_label.grid(row=row_idx, column=0, columnspan=4, pady=10)

# ====================================
# Startup Credit Popup
# ====================================
def show_credit_popup(root):
    popup = tk.Toplevel()
    popup.title("Credit")
    popup.geometry("350x120")
    tk.Label(popup, text="IT Problem Simulator\nby Agus Satria Adhitama", font=("Arial", 12, "bold")).pack(pady=20)
    tk.Button(popup, text="Close", command=popup.destroy).pack(pady=5)
    popup.after(4000, popup.destroy)

# ====================================
# Random Event Generator
# ====================================
def random_event(root):
    events = [internet_error, printer_error, app_crash, disk_full_error, memory_error, cpu_overload, network_fluctuation]
    def trigger_random():
        while True:
            time.sleep(random.randint(10,25))
            random.choice(events)()
    t = threading.Thread(target=trigger_random, daemon=True)
    t.start()

# ====================================
# CLI Hybrid Mode
# ====================================
def cli_mode():
    while True:
        print("""
=== IT Problem Simulator CLI ===
1. Internet Error
2. Printer Error
3. Application Crash
4. Disk Full
5. Memory Error
6. CPU Overload
7. Network Fluctuation
8. Training Mode
9. Exit
""")
        choice = input("Pilih menu: ")
        clear_screen()
        if choice=="1": internet_error()
        elif choice=="2": printer_error()
        elif choice=="3": app_crash()
        elif choice=="4": disk_full_error()
        elif choice=="5": memory_error()
        elif choice=="6": cpu_overload()
        elif choice=="7": network_fluctuation()
        elif choice=="8": slow_print("Launching Training Mode...")
        elif choice=="9": slow_print("Keluar dari CLI..."); break
        else: slow_print("Pilihan tidak valid!\n")

# ====================================
# Main GUI App
# ====================================
def run_app():
    root = tk.Tk()
    root.title("IT Problem Simulator")
    root.geometry("500x650")
    root.minsize(480, 600)

    # Fix scaling biar ga pecah di exe
    root.tk.call('tk', 'scaling', 1.2)

    # ===== STYLE =====
    root.configure(bg="#1e1e2e")

    main_frame = tk.Frame(root, bg="#1e1e2e")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # ===== TITLE =====
    title = tk.Label(
        main_frame,
        text="IT Problem Simulator",
        font=("Segoe UI", 18, "bold"),
        fg="white",
        bg="#1e1e2e"
    )
    title.pack(pady=(0,10))

    subtitle = tk.Label(
        main_frame,
        text="Simulate IT Issues & Train Your Skills",
        font=("Segoe UI", 10),
        fg="#cfcfcf",
        bg="#1e1e2e"
    )
    subtitle.pack(pady=(0,20))

    # ===== BUTTON FRAME =====
    btn_frame = tk.Frame(main_frame, bg="#1e1e2e")
    btn_frame.pack(fill="both", expand=True)

    buttons = [
        ("🌐 Internet Error", internet_error),
        ("🖨️ Printer Error", printer_error),
        ("💥 App Crash", app_crash),
        ("💾 Disk Full", disk_full_error),
        ("⚠️ Memory Error", memory_error),
        ("🔥 CPU Overload", cpu_overload),
        ("📡 Network Issue", network_fluctuation),
        ("🧠 Training Mode", training_mode),
        ("💻 CLI Mode", lambda: threading.Thread(target=cli_mode).start()),
        ("❌ Exit", root.destroy)
    ]

    for i, (text, cmd) in enumerate(buttons):
        btn = tk.Button(
            btn_frame,
            text=text,
            command=cmd,
            height=2,
            bg="#2a2a3d",
            fg="white",
            activebackground="#3a3a55",
            relief="flat",
            font=("Segoe UI", 10, "bold")
        )
        btn.grid(row=i, column=0, sticky="ew", pady=5)

    btn_frame.columnconfigure(0, weight=1)

    # ===== STATUS BAR =====
    status = tk.Label(
        root,
        text="Ready",
        bd=1,
        relief="sunken",
        anchor="w",
        bg="#2a2a3d",
        fg="white"
    )
    status.pack(side="bottom", fill="x")

    # ===== CREDIT =====
    credit = tk.Label(
        root,
        text="© 2026 by Agus Satria Adhitama",
        font=("Segoe UI", 8, "italic"),
        bg="#1e1e2e",
        fg="#aaaaaa"
    )
    credit.pack(side="bottom", pady=5)

    # Popup credit (delay dikit biar ga nge-freeze)
    root.after(800, lambda: show_credit_popup(root))

    root.mainloop()

# ====================================
# Run Application
# ====================================
if __name__=="__main__":
    run_app()