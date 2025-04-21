property.md

通過存取方法定義的屬性通常稱為特性（property）。

特性（property）是一種功能強大的存取器替代品。

存取方法（詳見抽象：自定義對像中類的內容），是名稱類似於getHeight和setHeight的方法，用於獲取或設置屬性（這些屬性可能是私有的）。如果訪問給定屬性時必須採取特定的措施，那麼像這樣封裝狀態變量（屬性）很重要。例如，請看下面的Rectangle類：

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height

下面的示例演示瞭如何使用這個類：

>>>r = Rectangle()
>>>r.width = 10
>>>r.height = 5
>>>r.get_size()
(10, 5)
>>>r.set_size((150, 100))
>>>r.width
150
>>>r.size
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    r.size
AttributeError: 'Rectangle' object has no attribute 'size'

get_size和set_size是假想屬性size的存取方法，這個屬性是一個由width和height組成的元組。 （可隨便將這個屬性替換為更有趣的屬性，如矩形的面積或其對角線長度。）這些代碼並非完全錯誤，但存在缺陷。使用這個類時，程序員應無須關心它是如何實現的（封裝）。

如果有一天你想修改實現，讓size成為真正的屬性，而width和height是動態計算出來的，就需要提供用於訪問width和height的存取方法，使用這個類的程序也必須重寫。應讓客戶端代碼（使用你所編寫代碼的代碼）能夠以同樣的方式對待所有的屬性。

那麼如何解決這個問題呢？給所有的屬性都提供存取方法嗎？這當然並非不可能，但如果有大量簡單的屬性，這樣做就不現實（而且有點傻），因為將需要編寫大量這樣的存取方式，除了獲取或設置屬性外什麼都不做。這將引入複製並粘貼（重複代碼）的壞味，顯然很糟糕（雖然在有些語言中，這樣的問題很常見）。所幸Python能夠替你隱藏存取方法，讓所有的屬性看起來都一樣。