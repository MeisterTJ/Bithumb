import pybithumb
import time

while True:
    # 현재 가격 받아온다.
    price = pybithumb.get_current_price("BTC")
    try:
        print(price/10)
    except:
        print("에러 발생", price)
    time.sleep(0.2)