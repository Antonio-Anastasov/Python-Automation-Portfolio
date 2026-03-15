import requests
from datetime import datetime

print("--- Стартиране на Тракера за XRP и Злато ---")


urls = {
    "XRP": "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT",
    "Gold (PAXG)": "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"
}

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


with open("assets_log.txt", "a", encoding="utf-8") as file:
    file.write(f"\n--- Проверка в: {current_time} ---\n")

    for name, url in urls.items():
        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                
                raw_price = float(data['price'])
                if name == "XRP":
                    price = round(raw_price, 4)  
                else:
                    price = round(raw_price, 2)  

                log_message = f"Цената на {name} е: ${price}"
                print(log_message)
                file.write(log_message + "\n")
            else:
                error_msg = f"Грешка при {name}! Статус код: {response.status_code}"
                print(error_msg)
                file.write(error_msg + "\n")

        except requests.exceptions.RequestException as e:
            print(f"Критична грешка при свързване за {name}: {e}")

print("\nДанните са успешно записани в 'assets_log.txt'.")


print("\nДанните са успешно записани в 'assets_log.txt'.")


input("\nНатисни Enter, за да затвориш програмата...")
