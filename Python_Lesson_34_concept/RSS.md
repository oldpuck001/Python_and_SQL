RSS.md

RSS和相關內容

RSS指的是富網站摘要（Rich Site Summary）、RDF網站摘要（RDF Site Summary）或簡易信息聚合（Really Simple Syndication），具體指哪個取決於版本。在最簡單的情況下，RSS是一種以XML方式列出新聞的格式。 RSS文檔（feed）與其說是靜態文檔，不如說是服務，因為它們需要定期或不定期地更新。它們甚至還需動態地計算，以呈現最新博客更新，等等。另一種作用與RSS相同的較新格式是Atom。有關RSS以及相關資源描述框架（RDF）的詳細信息，請參閱http://www.w3.org/RDF。有關Atom規範請參閱http://tools.ietf.org/html/rfc4287。

市面上的RSS閱讀器很多，它們通常也能處理其他格式，如Atom。鑑於RSS格式易於處理，因此不斷有開發人員探索出它的新用途。例如，有些瀏覽器（如Mozilla Firefox）允許用戶將RSS feed收藏為書籤，進而提供一個動態的書籤子菜單，其中的菜單項為不同的新聞。 RSS還是播客的支柱（播客其實就是列出聲音文件的RSS feed）。

問題是，如果你要編寫客戶端程序來處理來自多個網站的feed，就必須準備解析多種不同的格式，甚至需要對feed條目中的HTML片段進行解析。為此，可使用BeautifulSoup（或其面向XML的版本），但更佳的選擇是使用Mark Pilgrim開發的Universal Feed Parser（https://pypi.python.org/pypi/feedparser），因為它能夠處理多種feed格式（包括RSS和Atom及其擴展），並在一定程度上支持內容清理。 Pilgrim還撰寫了一篇很有用的文章“Parsing RSS At All Costs”（http://xml.com/pub/a/2003/01/22/dive-into-xml.html），如果你想自己處理清理，可參考這篇文章。