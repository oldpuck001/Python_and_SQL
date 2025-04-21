README.md

Python 中有多個用於進行文字識別（OCR，Optical Character Recognition）的模塊，其中最常用的包括以下幾個：

1. Tesseract-OCR (pytesseract)
    pytesseract是Google開源的Tesseract OCR引擎的Python介面。它是目前最流行的OCR解決方案之一，支持多種語言。
    安裝方法：

    pip install pytesseract

    還需要先安裝 Tesseract 引擎，具體的安裝方式取決於你的操作系統。
    macOS：

    brew install tesseract

    Windows：
    可以從 [Tesseract 官網](https://github.com/tesseract-ocr/tesseract)下載並安裝。

    使用範例：

    from PIL import Image
    import pytesseract

    # 指定圖片路徑
    image = Image.open('path_to_image.png')
    text = pytesseract.image_to_string(image, lang='chi_sim')  # 如果是中文，需使用 chi_sim

    print(text)

2. EasyOCR
    EasyOCR是另一個OCR工具，支持超過80種語言，並且不需要額外的安裝Tesseract引擎。
    安裝方法：

    pip install easyocr

    使用範例：

    import easyocr

    reader = easyocr.Reader(['ch_sim', 'en'])  # 支持中文和英文
    results = reader.readtext('path_to_image.png')

    for result in results:
        print(result[1])  # 取得文字部分

3. OCR.space API (ocrspace)
   ocrspace是一個基於API的服務，它不需要你本地安裝OCR引擎，通過網絡進行識別。
    安裝方法：

    pip install ocrspace

    需要註冊一個 API 密鑰後才能使用。

這些工具大多支持多語言的文字識別，包括中文和日文，可以根據具體的需求選擇合適的模塊。