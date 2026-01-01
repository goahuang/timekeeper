# 選用 slim 版本以最小化體積
FROM python:3.11-slim

WORKDIR /app

# 防止 Python 緩衝日誌，這對於 Cloud Run 即時查看日誌非常重要
ENV PYTHONUNBUFFERED=1

# 安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製程式碼
COPY . .

# Cloud Run 通訊埠
EXPOSE 8080

# 設定預設連接埠為 8080，這在本地 docker run 時會被使用
ENV PORT=8080

# 啟動指令：使用 Gunicorn 作為高效能 Web Server
# 使用 sh -c 確保變數 $PORT 被正確展開
CMD sh -c "gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app"
