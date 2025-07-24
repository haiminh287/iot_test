import RPi.GPIO as GPIO
import time

LED_PIN = 12     # GPIO 17 nối với LED (chân số 11)
SOUND_PIN = 27     # GPIO 27 nhận tín hiệu từ cảm biến âm thanh (DO)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SOUND_PIN, GPIO.IN)

led_state = False

try:
    while True:
        if GPIO.input(SOUND_PIN) == 0:  # 0 = phát hiện âm thanh (vỗ tay, gõ bàn)
            print("Phát hiện âm thanh!")
            led_state = not led_state
            GPIO.output(LED_PIN, led_state)
            time.sleep(0.3)  # Chống nhiễu
        time.sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
