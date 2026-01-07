Git_&_GitHub.md

Git與GitHub

初始化指令：git init

建立不需要的被追蹤的文件清單：在項目文件夾中新建 .gitignore 文件，將不需要追蹤的文件名寫入其中，可以使用通配符，例如：*

常用文件清单见示例。

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

更新指令：

git add --all

git commit -m 'updata202512114'

git push -u origin main

複製儲存庫的指令：git clone https://github.com/user/repository.git my-directory
將指定的 GitHub 儲存庫複製到名為 my-directory 的目錄中。網址從GitHub頁面中複製。