from ultralytics import YOLO

# 載入訓練好的模型
model = YOLO("runs/detect/train/weights/best.pt")

# 預測圖片或資料夾
model.predict(
    source="dataset/images/test",
    save=True,
    conf=0.25
)
