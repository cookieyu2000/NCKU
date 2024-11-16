from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

# 設定檔案資料夾路徑
FILE_FOLDER = "D:/Gene/NCKU/data/zip"  # 替換為存放 ZIP 檔的資料夾路徑
app.config["FILE_FOLDER"] = FILE_FOLDER


@app.route("/")
def index():
    # 取得資料夾中的檔案列表
    files = [f for f in os.listdir(FILE_FOLDER) if f.endswith(".zip")]
    return render_template("index.html", files=files)


@app.route("/download/<filename>")
def download_file(filename):
    # 確保下載的檔案在目標資料夾中
    return send_from_directory(app.config["FILE_FOLDER"], filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host="10.22.24.176", port=5000)
