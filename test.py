import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/train_person/weights/best.pt")

results = model.predict(r"C:\Users\ISLAB_309\Desktop\機器學習\dataset\train\images\000000002007_jpg.rf.d9171e3ec5135ebb4e28f28a7615d6ba.jpg")

# 抓第一張結果的圖像
img = results[0].plot()  

# 顯示圖像
cv2.imshow("Result", img)
cv2.waitKey(0)   # 等你按任意鍵才關閉
cv2.destroyAllWindows()
