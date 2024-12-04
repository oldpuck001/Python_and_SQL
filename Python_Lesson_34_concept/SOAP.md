SOAP.md

SOAP也是一種將XML和HTTP用作底層技術的消息交換協議。與XML-RPC一樣，SOAP也支持遠程過程調用，但SOAP規範比XML-RPC規範複雜得多。 SOAP是異步的，支持有關路由的元請求，而且類型系統非常複雜（而XML-RPC使用簡單而固定的類型機）。

當前，沒有標準的Python SOAP工具包，可以考慮使用Twisted（[http://twistedmatrix.com](http://twistedmatrix.com/)）、ZSI（[http://pywebsvcs.sf.net](http://pywebsvcs.sf.net/)）或SOAPy（[http://soapy.sf.net](http://soapy.sf.net/)）。有關SOAP的詳細信息，請參閱http://www.w3.org/TR/soap。

以前，SOAP指的是簡單對象訪問協議（Simple Object Access Protocol），但現在不是這樣了。