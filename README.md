安裝與環境配置說明

本專案使用 Python 3.10 開發，主要依賴套件如下：
| 套件            | 版本     | 功能說明                          |
| ------------- | ------ | ----------------------------- |
| ultralytics   | 8.x    | YOLOv8 目標檢測與訓練核心套件            |
| torch         | 2.x    | PyTorch 深度學習框架，提供 GPU 運算與自動微分 |
| torchvision   | 0.15.x | 影像相關工具，包括資料增強、轉換等             |
| opencv-python | 4.x    | 影像讀取、預處理與可視化                  |
| matplotlib    | 3.x    | 訓練曲線、檢測結果可視化                  |
| numpy         | 1.x    | 陣列運算與資料處理                     |

安裝方式:
# 建立虛擬環境
python -m venv yolov8_env
# 啟動虛擬環境
# Windows
yolov8_env\Scripts\activate
# 安裝套件
pip install ultralytics torch torchvision opencv-python matplotlib numpy

作業系統與硬體配置：
作業系統：Windows 10 64-bit
GPU：NVIDIA GeForce 系列，CUDA 11.7
CPU：Intel i7 或以上
記憶體：16GB 以上
訓練與預測皆支援 GPU 加速，可透過 device=0 指定 GPU 使用，若無 GPU 可設定 device='cpu'。


重要模塊輸入/輸出說明

YOLO 模型模塊 (ultralytics.YOLO)
輸入：
data：資料集 YAML 檔路徑，定義訓練、驗證、測試資料及類別
epochs：訓練輪數
imgsz：影像 resize 尺寸
batch：訓練批次大小
輸出：
模型權重 (best.pt, last.pt)
訓練曲線與損失圖 (results.png)
訓練日誌 (events.out.tfevents.*)

資料加載與預處理模塊
輸入：資料集影像與對應 YOLO 標註檔 (.txt)
輸出：模型可讀的批次 tensor，包含：
影像 tensor (B, C, H, W)
邊界框座標及類別索引

驗證模塊 (model.val())
輸入：驗證集資料集 YAML 或資料夾
輸出：
評估指標：Precision, Recall, mAP@0.5, mAP@0.5:0.95
損失值曲線

預測模塊 (model.predict())
輸入：測試影像資料夾或單張影像
輸出：
預測結果列表，每個目標包含：
邊界框座標 [x1, y1, x2, y2]
類別索引
置信度分數
可選擇儲存檢測影像結果
