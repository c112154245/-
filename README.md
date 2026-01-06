環境:python3.11.7(virtual)

train.py:
from ultralytics import YOLO

# 載入 YOLOv8 預訓練模型
model = YOLO("yolov8n.pt")

# 訓練模型
model.train(
    data="dataset/data.yaml",
    epochs=10,
    imgsz=640,
    batch=8,
    project="runs/detect/train_person",
    name="train_person",
    exist_ok=True
)

# 預測單張驗證集圖片
results = model.predict("dataset/valid/images/0001.jpg", show=True)

predict.py:
from ultralytics import YOLO

# 載入訓練好的模型
model = YOLO("runs/detect/train/weights/best.pt")

# 預測圖片或資料夾
model.predict(
    source="dataset/images/test",
    save=True,
    conf=0.25
)


本研究使用 Ultralytics 提供之 YOLOv8 物件偵測模型進行訓練與預測。訓練程式碼主要透過 train.py 執行，載入官方提供的預訓練模型 yolov8n.pt 作為初始權重，並指定資料集設定檔 data.yaml，以加速模型收斂並提升整體效能。模型訓練過程中，系統會自動將資料分為訓練集與驗證集，並於每個訓練週期後進行驗證，以評估模型學習成效。

在預測階段，透過 test.py 載入訓練完成後的最佳權重檔（best.pt），對單張圖片進行物件偵測，模型會輸出預測之邊界框與類別標籤，並以視覺化方式顯示結果，用以確認模型辨識能力與標註正確性。
