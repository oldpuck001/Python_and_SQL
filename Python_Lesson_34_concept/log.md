log.md

日誌與測試有一定的關係，而且在需要大規模改造程序的內部構造時很有用，它無疑能夠幫助你發現問題和bug。日誌大致上就是收集與程序運行相關的數據，供你事後進行研究和積累。

不會導致程序終止、而只是讓它行為異常的bug是最難查找的，但通過查看詳盡的日誌文件也許能夠幫助你找出問題出在什麼地方。

實現日誌的方式：

自己動手使用print語句實現簡單的日誌；
使用標準庫中的模塊logging。

自己動手使用print語句實現簡單的日誌：

print語句是一種簡單的日誌形式。要使用這種日誌形式，只需在程序開頭包含一條類似於下面的語句：

log = open('logfile.txt', 'w')

然後就可將任何感興趣的程序狀態寫入這個文件，如下所示：

print('Downloading file from URL', url, file = log)
text = urllib.urlopen(url).read()
print('File successfully downloaded', file = log)

如果程序在下載期間崩潰，這種方法的效果就不會很好。更安全的做法是，在每條日誌語句前後都打開和關閉文件（至少應該在寫入後刷新文件）。這樣，即便程序崩潰，也將看到日誌文件的最後一行為“Downloading file from URL”，從而知道下載失敗了。

使用標準庫中的模塊logging：

模塊logging的基本用法非常簡單。通過合理地配置模塊logging，可讓日誌以你希望的方式運行。下面是幾個這樣的示例。

- 記錄不同類型的條目（信息、調試信息、警告、自定義類型等）。默認情況下，只記錄警告。
- 只記錄與程序特定部分相關的條目。
- 只記錄有關時間、日期等方面的信息。
- 記錄到其他位置，如套接字。
- 配置日誌器，將一些或大部分日誌過濾掉，這樣無須重寫程序就能獲得所需的日誌信息。

模塊logging非常複雜，文檔中還提供了其他很多相關的信息。

日誌示例（logging模塊）

一個使用模塊logging的程序：

import logging

logging.basicConfig(level = logging.INFO, filename = 'mylog.log')

logging.info('Starting program')

logging.info('Trying to divide 1 by 0')

print(1/0)

logging.info('The division succeeded')

logging.info('Ending program')

運行這個程序時，將生成下面的日誌文件（mylog.log）：

INFO:root:Starting program
INFO:root:Trying to divide 1 by 0

如你所見，試圖將1除以0後什麼都沒有記錄下來，因為這種錯誤將導致程序終止。這是一種簡單的錯誤，你可根據程序崩潰時打印的異常來跟蹤確定問題出在什麼地方。

level = logging.INFO：設置日誌記錄的層級為INFO，即只記錄INFO、WARNING、ERROR 和 CRITICAL四個層級及以上的日誌信息，DEBUG 級別以下的日誌不會被記錄。

在 Python logging 模組中，共有 5 個日誌層級，分別是：

1.DEBUG：用於詳細或冗長的訊息，通常只用於調試或開發過程中。
2.INFO：用於較為重要的事件或訊息，比如程式運行中的關鍵操作，或者是顯示程式運行的進度等。
3.WARNING：用於警告訊息，表示程式運行中出現了一些非致命的問題或不合理的操作，但是不會導致程式崩潰或錯誤。
4.ERROR：用於錯誤訊息，表示程式出現了一些錯誤或異常情況，但程式還能繼續執行。
5.CRITICAL：用於致命錯誤訊息，表示程式遇到了無法繼續執行的嚴重錯誤，此時程式可能會崩潰或停止執行。