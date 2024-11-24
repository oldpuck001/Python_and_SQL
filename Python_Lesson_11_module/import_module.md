import_module.md

基本語法：
導入：import math
使用：math.sqrt
使用這種方式導入模塊後，調用模塊中的函數或類時，必須加上模塊名作為前綴，這是因為將整個模塊引入了程式後，需要使用模塊名來區分引用的定義和其他可能在程式中出現的同名定義

使用from關鍵字導入部分函數或模塊中的一切
導入：from math import sqrt
           from math import sqrt, floor, ceil
           from math import *
使用：sqrt
不同模塊的同名函數會衝突，需要math.sqrt的方式調用
確定需要使用哪些函數以後，可以回過頭去修改from math import *語句，以便只導入需要的函數

用變量引導函數
導入：foo = math.sqrt
使用：foo(4)

為整個模塊指定別名，as
導入：import math as foobar
使用：foobar.sqrt
許多第三方包會建議在使用別名時遵循某種慣例，比如pandas用的是 import pandas as pd

為個別函數指定別名，as
導入：from math import sqrt as foobar
使用：foobar

當你導入模塊時，可能發現其所在目錄中除源代碼文件外，還新建了一個名為__pycache__的子目錄（在較舊的Python版本中，是擴展名為.pyc的文件）。這個目錄包含處理後的文件，Python能夠更高效地處理它們。以後再導入這個模塊時，如果.py文件未發生變化，Python將導入處理後的文件，否則將重新生成處理後的文件。刪除目錄__pycache__不會有任何害處，因為必要時會重新創建它。