# 仕分けロボット Sorting robot
# USBカメラの映像から「リンゴ」と「バナナ」を認識します。
# 学習済みのモデル"keras_model.h5"と"labels.txt"が必要。
                         
# CS&AIセットのシングルモーターを使用します
# (1)モーターの電源を入れる。
# (2)接続カードを読み込む。
# (3)モーターのボタンを押して接続待機状態にする（ボタンが点滅）。

import legoeducation as le
from teachable_machine import TeachableMachine
import cv2 as cv
import time

# 接続カードの情報を設定
card_color = le.LEGO_COLOR_RED  # 動作環境に合わせて修正
card_serial = '2313'            # 動作環境に合わせて修正

CLASS_APPLE = 0
CLASS_BANANA = 1
THRESHOLD = 0.8

# SingleMotorオブジェクト作成
singlemotor = le.SingleMotor()

# シングルモーターと接続
def connect_motor():
    try:
        print("シングルモーターと接続...")
        singlemotor.connect(
            card_color=card_color,
            card_serial=card_serial
        )

        if singlemotor.connected:
            print("接続しました。")
        else:
            print("接続できませんでした。")

    except Exception as e:
        print('Error', str(e))

# モーター制御(絶対角度)
def move_motor(angle):
    print("Motor angle:" + str(angle) + '[degree]')
    singlemotor.motor_run_to_absolute_position(
        position=angle ,speed = 20 )

# シングルモーターと切断
def disconnect_motor():
    try:
        if singlemotor.connected:
            singlemotor.disconnect()
    except:
        pass

#--- main
connect_motor()  # モーターと接続

cap = cv.VideoCapture(0)
model = TeachableMachine(model_path="keras_model.h5",
                         labels_file_path="labels.txt")

image_path = "screenshot.jpg"
move_motor(0)

while True:
    _, img = cap.read()
    cv.imwrite(image_path, img)
    result, resultImage = model.classify_and_show(image_path)

    print("class_index", result["class_index"])
    print("class_name:::", result["class_name"])
    print("class_confidence:", result["class_confidence"])
    print("predictions:", result["predictions"])
    cv.imshow("Video Stream", resultImage)

    if result["class_confidence"] < THRESHOLD:
        print("No sense")
    else:
        if result["class_index"] == CLASS_APPLE:
            move_motor(45)
            time.sleep(0.5)
            move_motor(0)

        if result["class_index"] == CLASS_BANANA:
            move_motor(-45)
            time.sleep(0.5)
            move_motor(0)

    k = cv.waitKey(1)
    if k == 27:  # Press ESC to close the camera view
        break

cap.release()
cv.destroyAllWindows()
disconnect_motor()  # モーターと切断
