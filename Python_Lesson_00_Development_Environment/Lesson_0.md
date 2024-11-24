Lesson_0內容：

(1) VScode 安裝

    VScode官方網站：https://code.visualstudio.com

(2)VScode延伸模組的安裝

    Python延伸模組：Python、Pylance、Python Debugger
    Python的官方網站：https://www.python.org
    HTML延伸模組：Live Server

(3)Python第三方庫的使用

    macOS終端機的常用命令：
        查看你目前所在目錄的完整路徑: pwd
        列出目前目錄中的文件: ls、ls -la
            ls 列出目錄內容； -la 以長列表格式顯示，並包含所有文件，隱藏文件也會顯示出來。
        切換目錄(相對路徑): cd path/to/dir
        切換目錄(絕對路徑): cd /path/to/dir
        切換至父目錄: cd ..
            可以輸入 cd ../Desktop 先回到上一層目錄，再進入 Desktop 文件夾
        回到前一個/下一個指令: ↑(上箭頭)/↓(下箭頭)
        列出所有已安裝的包: pip freeze
        安裝指定包的最新版本: pip install package
        安裝指定包版本: pip install package==1.0.0
        更新包: pip install --upgrade package
        拆卸包: pip uninstall package

    部分需要安裝的包：pandas、openpyxl、docx

(4)Node.js和npm的安裝（使用Electron框架的準備工作）

    Node.js官方網站: https://nodejs.org/
    檢查是否已經安裝的指令：
        node -v
        npm -v
    如過執行結果顯示版本號，說明 Node.js 和 npm 已經安裝成功。
    npm (Node Package Manager) 是隨 Node.js 一起安裝的包管理工具，它的主要作用包括以下幾個方面：1.包管理；2.項目初始化；3.包發佈與分享；4.本地與全局安裝；5.依賴管理；6.運行腳本。

    在終端中，創建一個新目錄並進入該目錄，然後初始化一個新的 npm 項目：
        mkdir my-electron-app
        cd my-electron-app
        npm init -y
        這樣會創建一個包含默認配置的 package.json 文件。

    安裝 Electron：
        npm install electron --save-dev
        這會將 Electron 安裝為開發依賴，並更新 package.json 文件中的 devDependencies。

    在項目根目錄下創建一個名為 main.js 的文件，這是 Electron 應用的主進程文件，負責創建和管理應用窗口。參考代碼見 main.js

    在項目根目錄下創建 index.html 文件，這是應用程序的用戶界面部分。

    修改 package.json 文件中的 "main": "index.js", 修改成 "main": "main.js",

    修改 package.json 文件中的 scripts 部分，以便能夠使用 npm start 來運行 Electron 應用。
        "scripts": {
            "test": "echo \"Error: no test specified\" && exit 1",
            "start": "electron ."
        }
        "test": "echo \"Error: no test specified\" && exit 1" 是一個預設的 npm 腳本，用於在你沒有設置測試命令時顯示錯誤消息並退出。如果你運行 npm test，它會輸出 "Error: no test specified" 並返回一個非零的退出代碼（表示錯誤）。如果你目前沒有為項目設置測試腳本，也不打算使用 npm test 命令來運行測試，那麼你可以刪除這行代碼，這樣在無意中運行 npm test 時就不會顯示這個錯誤。如果你打算在將來為項目添加測試，這行代碼可以作為一個提醒，讓你知道目前還沒有設置測試腳本。在你添加測試腳本後，你可以修改這行代碼以運行你的測試命令。

    在 VS Code 中打開終端，然後運行以下命令來啟動 Electron 應用：
        npm start

    運行成功，初始化完成。

(5)Git與GitHub的安裝

    Git官方網站：https://git-scm.com/downloads
    安裝方法：在macOS終端機中執行 xcode-select --install 指令。這條指令的作用是安裝Xcode命令行工具（Command Line Tools），其中包括Git版本控制系統。
    檢查安裝是否成功：在VScode的終端機中執行 git --version 指令，執行結果如果出現Git的版本編號，則表示安裝成功。
    設置用戶名的指令：git config --global user.name 'your_name'
    設置Email的指令：git config --global user.email 'your_name@gmail.com'
    初始化指令：git init
    建立不需要的被追蹤的文件清單：在項目文件夾中新建 .gitignore 文件，將不需要追蹤的文件名寫入其中，可以使用通配符，例如：*
    Git中文件的四種狀態：Untracked、Tracked、Staged、Committed。
    檢查當前目錄中每個文件的狀態：git status
    追蹤單個文件的指令：git add your_file.md
    追蹤所有文件的指令：git add --all
        使用 git add --all 的優點：不仅会将新增和修改的文件添加到暂存区，还会处理已删除的文件。
    建立還原點的指令：git commit -m '說明信息'
        -m 是 --message 的縮寫，後面跟著的是一個簡短的提交信息。
    查看提交日誌的指令：git log 或者 git log --oneline
    比較還原點的指令：git diff 還原點的ID --要對比的文件的文件名
    還原指令：git checkout 還原點的ID --要對比的文件的文件名

    GitHub的網站地址：https://github.com
    建立庫之後，複製粘貼執行三條初始化的指令
    更新指令：git push -u origin main
    複製儲存庫的指令：git clone https://github.com/user/repository.git my-directory
        將指定的 GitHub 儲存庫複製到名為 my-directory 的目錄中。網址從GitHub頁面中複製。