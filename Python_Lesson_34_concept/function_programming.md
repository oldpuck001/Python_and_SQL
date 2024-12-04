function_programming.md

函數式編程

你可以像使用其他對象（字符串、數、序列等）一樣使用函數：將其賦給變量，將其作為參數進行傳遞，以及從函數返回它們。在有些語言（如scheme和Lisp）中，幾乎所有的任務都是以這種方式使用函數來完成的。在Python中，通常不會如此倚重函數（而是創建自定義對象），但完全可以這樣做。

Python提供了一些函數式編程工具，其中包括lambda表達式以及函數map、filter和reduce。

在較新的Python版本中，函數map和filter的用途並不大，應該使用列表推導來替代它們。

map(func, seq, seq, …)        將序列中的所有元素執行函數

你可以使用map将序列的所有元素传递给函数。

>>>list(map(str, range(10)))  #與[str(i) for i in range(10)]等價
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

filter(func, seq)        返回一個迭代器，其中包含對其執行函數時結果為真的所有元素

可使用filter根據布爾函數的返回值來對元素進行過濾。

>>>def func(x):
...    return x.isalnum()
...
>>>seq = ["foo", "x41", "?!", "***"]
>>>list(filter(func, seq))
['foo', 'x41']

就這個示例而言，如果轉而使用列表推導，就無需創建前述自定義函數。

>>>[x for x in seq if x.isalnum()]
['foo', 'x41']

實際上，Python提供了一種名為lambda表達式的功能（lambda來源於希臘字母，在數學中用於表示匿名函數），讓你能夠創建內嵌的簡單函數（主要供map、filter和reduce使用）。

>>>filter(lambda x: x.isalnum(), seq)
['foo', 'x41']

然而，使用列表推導的可讀性更高。

reduce(func, seq, initial)        等價於func(func(func(seq[0], seq[1]), seq[2]), …)

要使用列表推導來替換函數reduce不那麼容易，而這個函數提供的功能即便能用到，也用得不多。它使用指定的函數將序列的前兩個元素合二為一，再將結果與第三個元素合二為一，依此類推，直到處理完整個序列並得到一個結果。例如，如果你要將序列中的所有數相加，可結合使用reduce和lambda x, y: x + y。

>>>numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
>>>from functools import reduce
>>>reduce(lambda x, y: x + y, numbers)
1161

當然，就這個示例而言，還不如使用內置函數sum。

實際上，可不使用這個lambda函數，而是導入模塊operator中的函數add（這個模塊包含對於每個內置運算符的函數）。與使用自定義函數相比，使用模塊operator中的函數總是效率更高。