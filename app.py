import os
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_time():
    """回傳目前日期與時間 (Core functionality)"""
    now = datetime.now()
    return jsonify({
        "status": "success",
        "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
        "timestamp": now.timestamp()
    })

@app.errorhandler(404)
def not_found(error):
    """處理 404 錯誤 (Best practice for APIs)"""
    return jsonify({
        "status": "error",
        "message": "找不到此路徑",
        "code": 404
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """處理 500 錯誤範例"""
    app.logger.error(f"Server Error: {error}")
    return jsonify({
        "status": "error",
        "message": "伺服器內部錯誤",
        "code": 500
    }), 500

if __name__ == "__main__":
    # 讀取 Cloud Run 自動注入的 PORT
    port = int(os.environ.get("PORT", 8080))
    # 注意：在 Docker/Cloud Run 中，host 必須是 0.0.0.0
    app.run(host='0.0.0.0', port=port)
