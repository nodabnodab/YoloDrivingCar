# 파일명: car_control.py

from pop import Pilot
import time

# 이 모듈이 임포트될 때 자동차 객체를 한 번만 생성
try:
    autocar = Pilot.AutoCar()
    print("✅ AutoCar 객체가 성공적으로 초기화되었습니다.")
except Exception as e:
    autocar = None
    print(f"⚠️ AutoCar 객체 초기화 실패: {e}")

def set_steering(angle):
    """ -1.0 ~ 1.0 사이의 값을 받아 조향각을 설정합니다. """
    if autocar:
        angle = max(-1.0, min(angle, 1.0))
        autocar.steering = angle

def set_speed(speed_percent):
    """ 0 ~ 100 사이의 값을 받아 속도를 설정합니다. """
    if autocar:
        speed = max(0, min(speed_percent, 100))
        if speed == 0:
            autocar.stop()
        else:
            autocar.forward(speed)

def stop():
    """ 자동차를 정지시킵니다. """
    if autocar:
        autocar.steering = 0
        autocar.stop()