Development_Environment.md

开发环境搭建：

(1) 安装Python

    Python的官方網站：https://www.python.org

(2) 安裝集成开发环境（IDE）：VScode

    VScode官方網站：https://code.visualstudio.com

(3) 安装VScode延伸模組

    中文支持：Language pack extension for Chinese
    Python延伸模組：Python、Pylance、Python Debugger
    HTML延伸模組：Live Server

(4) 安装Python第三方庫（在终端中安装）

    需要安裝的包：pandas、openpyxl、xlrd、python-docx

    安装指令：
    which python3
    /usr/local/bin//python3(返回結果)
    /usr/local/bin/python3 -m pip install pandas
    /usr/local/bin/python3 -m pip install openpyxl
    /usr/local/bin/python3 -m pip install xlrd
    /usr/local/bin/python3 -m pip install python-docx

    pandas包含的包：numpy、pandas、python-dateutil、pytz、six、tzdata
    openpyxl包含的包：et_xmlfile、openpyxl
    xlrd包含的包：xlrd
    python-docx包含的包：lxml、python-docx、typing_extensions

    常用的pip指令：
    列出所有已安裝的包:       pip freeze
    安裝指定包的最新版本:     pip install package
    安裝指定包版本:          pip install package==1.0.0
    更新包:                 pip install --upgrade package
    拆卸包:                 pip uninstall package

    終端機的常用命令：
    查看你目前所在目錄的完整路徑:       pwd
    列出目前目錄中的文件:              ls、ls -la（MacOS系统）、dir（Windows系统）
    ls 列出目錄內容；                 -la 以長列表格式顯示，並包含所有文件，隱藏文件也會顯示出來。
    切換目錄(相對路徑):               cd path/to/dir
    切換目錄(絕對路徑):               cd /path/to/dir
    切換至父目錄:                     cd ..
    先返回上一级目录，再进入子文件夹：   可以輸入 cd ../Desktop 先回到上一層目錄，再進入 Desktop 文件夾
    回到前一個/下一個指令:             ↑(上箭頭)/↓(下箭頭)

(5) 安裝Node.js和npm（使用Electron框架的準備工作）

    Node.js官方網站: https://nodejs.org/
    使用Windows系统安装程序时，在第一个界面将添加到环境变量的选择框选中。

    檢查是否已經安裝的指令：
    node -v
    npm -v
    
    如過執行結果顯示版本號，說明 Node.js 和 npm 已經安裝成功。

    npm (Node Package Manager) 是隨 Node.js 一起安裝的包管理工具，它的主要作用包括以下幾個方面：1.包管理；2.項目初始化；3.包發佈與分享；4.本地與全局安裝；5.依賴管理；6.運行腳本。

(6) 安裝Git

    Git官方網站：https://git-scm.com/downloads

    安裝方法：
    在macOS系统中：終端機中執行 xcode-select --install 指令。這條指令的作用是安裝Xcode命令行工具（Command Line Tools），其中包括Git版本控制系統。
    在Windows系统中：在官网下载安装。
    
    檢查安裝是否成功：在VScode的終端機中執行 git --version 指令，執行結果如果出現Git的版本編號，則表示安裝成功。
    
    設置用戶名的指令：git config --global user.name 'your_name'
    設置Email的指令：git config --global user.email 'your_name@gmail.com'