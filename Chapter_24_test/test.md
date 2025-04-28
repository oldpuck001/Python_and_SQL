test.md

應該遵循“使其管用，使其更好，使其更快”這條古老的規則。

單元測試可讓程序管用，源代碼檢查可讓程序更好，而性能分析可讓程序更快。

單元測試工具：unittest
unittest是基於流行的Jave測試框架JUnit，它能夠以結構化方式編寫龐大而詳盡的測試集。
unittest包含的一些功能在大多數測試中都不需要。

函數unittest.main負責替你運行測試：實例化所有的TestCase子類，並運行所有名稱以test打頭的方法。

如果你定義了方法setUp和tearDown，它們將分別在每個測試方法之前和之後執行。你可使用這些方法來執行適用於所有測試的初始化代碼和清理代碼，這些代碼稱為測試夾具（test fixture）。

諸如assertEqual等方法檢查指定的條件，以判斷指定的測試是成功還是失敗了。

TestCase類還包含很多與之類似的方法，如assertTrue、assertIsNotNone和assertAlmostEqual。

模塊unittest區分錯誤和失敗。錯誤指的是引發了異常，而失敗是調用failUnless等方法的結果。

碼農高天關於unittest框架、和在測試單元中增加代碼覆蓋率測試的視頻
b站：
https://www.bilibili.com/video/BV1sZ4y1i7nQ/?share_source=copy_web
https://www.bilibili.com/video/BV17L411D7wy/?share_source=copy_web
YouTube：
https://youtu.be/n6DljHXv1do?si=jNx_CHnoQi47Caic
https://youtu.be/5Md_3ZeuYPc?si=G1XlW1fdu3HOYpVw