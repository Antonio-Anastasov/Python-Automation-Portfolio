import tkinter as tk
import requests
from datetime import datetime



def fetch_prices():
    
    time_label.config(text="Обновяване на данните...")
    window.update()

    urls = {
        "XRP": "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT",
        "Gold (PAXG)": "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"
    }

    try:
       
        res_xrp = requests.get(urls["XRP"])
        if res_xrp.status_code == 200:
            price_xrp = round(float(res_xrp.json()['price']), 4)
            xrp_label.config(text=f"XRP: ${price_xrp}")

       
        res_gold = requests.get(urls["Gold (PAXG)"])
        if res_gold.status_code == 200:
            price_gold = round(float(res_gold.json()['price']), 2)
            gold_label.config(text=f"Gold: ${price_gold}")

       
        current_time = datetime.now().strftime("%H:%M:%S")
        time_label.config(text=f"Последно обновяване: {current_time}")

    except requests.exceptions.RequestException:
        time_label.config(text="Грешка с интернет връзката!")



window = tk.Tk()
window.title("Крипто Тракер")
window.geometry("300x250")  
window.configure(bg="#2c3e50") 


window.wm_attributes("-topmost", True)



title_label = tk.Label(window, text="Цени на живо", font=("Arial", 16, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=10)  

xrp_label = tk.Label(window, text="XRP: Зареждане...", font=("Arial", 14), bg="#2c3e50", fg="#3498db")
xrp_label.pack(pady=5)

gold_label = tk.Label(window, text="Gold: Зареждане...", font=("Arial", 14), bg="#2c3e50", fg="#f1c40f")
gold_label.pack(pady=5)


refresh_btn = tk.Button(window, text="Обнови цените", font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
                        command=fetch_prices)
refresh_btn.pack(pady=15)

time_label = tk.Label(window, text="", font=("Arial", 10), bg="#2c3e50", fg="#bdc3c7")
time_label.pack(pady=5)


fetch_prices()


window.mainloop()
