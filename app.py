from flask import Flask
app = Flask(__name__) #__name__:目前執行的模組

from flask import render_template#Flask提供函數render_template()，可以將有關HTML 5的程式碼放在另一個檔案裡，藉由render_template()去讀取它。
@app.route("/")#函式的裝飾(Decorator):以函式為基礎，提供附加的功能
def home():
    return render_template("index.html")

if __name__ == "__main__": #如果以主程式執行
    app.run() #立即啟動伺服器