abnormal.md

Python使用異常對象來表示異常狀態，並在遇到錯誤時引發異常。異常對象未被處理（或捕獲）時，程序將終止並顯示一條錯誤消息（traceback）。

>>>1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in?
ZeroDivisionError: integer division or modulo by zero

每個異常都是某個類（這裡是ZeroDivisionError）的實例，從而逮住錯誤並採取措施，而不是放任整個程序失敗。