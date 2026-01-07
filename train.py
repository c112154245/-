from ultralytics import YOLO

# 載入模型
model = YOLO("yolov8n.pt")

# 訓練
model.train(
    data=r"C:\Users\ISLAB_309\Desktop\機器學習\dataset\data.yaml",  # 用 r"..." 避免路徑錯誤
    model="yolov8n.pt",
    epochs=10,
    imgsz=640,
    batch=8,
    name="train_person"
)
