import RPi.GPIO as GPIO
import time

# Sử dụng số chân theo kiểu BCM
GPIO.setmode(GPIO.BCM)

# Cài đặt chân GPIO 17 làm output
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    # Bật đèn
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("Đèn đã bật.")
    
    time.sleep(5)  
    
    # Tắt đèn
    GPIO.output(LED_PIN, GPIO.LOW)
    print("Đèn đã tắt.")
    
finally:
    # Reset các thiết lập GPIO
    GPIO.cleanup()
