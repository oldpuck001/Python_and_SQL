初始化Electron框架

在終端中，創建一個新目錄並進入該目錄，然後初始化一個新的 npm 項目：
    mkdir my-electron-app
    cd my-electron-app
    npm init -y
    這樣會創建一個包含默認配置的 package.json 文件。

安裝 Electron：
    npm install electron --save-dev
    這會將 Electron 安裝為開發依賴，並更新 package.json 文件中的 devDependencies。

在項目根目錄下創建一個名為 main.js 的文件，這是 Electron 應用的主進程文件，負責創建和管理應用窗口。參考代碼見 main.js

在項目根目錄下創建 backend.py 文件，用于连接前端与后端的通讯。

修改 package.json 文件中的 "main": "index.js", 修改成 "main": "main.js",

修改 package.json 文件中的 scripts 部分，以便能夠使用 npm start 來運行 Electron 應用。
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1",
        "start": "electron ."
    }
"test": "echo \"Error: no test specified\" && exit 1" 是一個預設的 npm 腳本。
用於在你沒有設置測試命令時顯示錯誤消息並退出。
如果你運行 npm test，它會輸出 "Error: no test specified" 並返回一個非零的退出代碼（表示錯誤）。
如果你目前沒有為項目設置測試腳本，也不打算使用 npm test 命令來運行測試，那麼你可以刪除這行代碼，
這樣在無意中運行 npm test 時就不會顯示這個錯誤。如果你打算在將來為項目添加測試，這行代碼可以作為一個提醒，
讓你知道目前還沒有設置測試腳本。在你添加測試腳本後，你可以修改這行代碼以運行你的測試命令。

在項目根目錄下創建 index.html、index.css、index.js 文件，這是應用程序的用戶界面部分。

在 VS Code 中打開終端，然後運行以下命令來啟動 Electron 應用：
    npm start

運行成功，初始化完成。