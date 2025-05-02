SQLite.md

SQLite是一個小型數據庫引擎，它不需要作為獨立的服務器運行，且可直接使用本地文件，而不需要集中式數據庫存儲機制。

在較新的Python版本（從2.5開始）中，標準庫中包含了一個SQLite的包裝器，即使用模塊sqlite3實現的PySQLite。



fetchall：

在Python中，curs.fetchall() 是sqlite3模組中Cursor物件的一個方法，主要用於從資料庫查詢中檢索所有結果行。以下是詳細的說明：

用法
rows = curs.fetchall()

功能
curs.fetchall() 會返回查詢結果中所有尚未提取的行，並將其以列表形式返回。
如果查詢結果為空或所有行都已被提取，則會返回空列表。

返回值
列表（list）：
每一行是查詢結果中的一筆記錄。
每一行通常是元組（tuple），其中包含來自資料庫表格的欄位值。

特點
1.一次性提取：
fetchall() 一次性提取所有剩餘的行，這可能會導致大量資料佔用記憶體。
如果結果集非常大，建議使用fetchone()或fetchmany(size)來分批提取。
   
2.配合SQL查詢：
必須在執行查詢語句（`SELECT`）後使用，否則結果為空。

注意事項
1.記憶體效率：
如果查詢結果非常大，fetchall()可能會消耗過多記憶體並降低性能。建議使用fetchone()或fetchmany()進行分批提取。

2.查詢上下文：
必須在執行SELECT查詢後調用fetchall()，否則沒有結果可以提取。

3.多次調用：
每次調用fetchall()時，只會返回查詢結果中尚未提取的部分。如果所有行都已提取，將返回空列表。



description：

在Python的sqlite3模組中，curs.description是Cursor物件的一個屬性，用於獲取最近執行的查詢結果中的欄位（列）資訊。以下是詳細的說明：

用法
column_info = curs.description

功能
curs.description提供關於查詢結果欄位的詳細資訊，例如欄位名稱和其他屬性。
它是一個包含元組的列表，每個元組對應查詢結果中的一個欄位。

結構
返回值：列表（list），其中每個元素是元組（tuple）。
每個元組包含7個元素，結構如下：
1.名稱（name）：欄位名稱（最常用）。
2.類型代碼（type_code）：欄位的數據類型（通常為None）。
3.顯示大小（display_size）：顯示欄位所需的大小（通常為None）。
4.內部大小（internal_size）：欄位的內部大小（通常為None）。
5.精度（precision）：數字類型的精度（通常為None）。
6.比例（scale）：數字類型的小數位數（通常為None）。
7.允許為NULL（null_ok）：是否允許NULL值（通常為None）。

注意：sqlite3模組中，除了第一個元素（名稱），其他元素通常都是None，因為SQLite不需要其他詳細的列屬性。

應用場景
1.動態生成列名：
當需要將查詢結果轉換為JSON、字典或其他格式時，description提供欄位名稱。

rows = curs.fetchall()
data = [dict(zip(column_names, row)) for row in rows]
print(data)

2.自動化處理：
在不清楚查詢結果結構的情況下，可動態獲取列名以適應不同的查詢。

注意事項
1.屬性值：
description僅在執行查詢後可用。如果未執行任何查詢，或查詢結果不包含列（例如`INSERT`），則`description`為`None`。

2.SQLite特性：
由於SQLite的數據類型是動態的，大多數欄位屬性（例如type_code和null_ok）在description中為None。