README.md

主流的Python PDF庫及其功能介紹：

1. PyPDF2

讀取與提取內容：
·提取PDF的文本內容。
·獲取PDF的元數據（如標題、作者等）。
操作PDF頁面：
·分割PDF，提取特定頁面。
·合併多個PDF。
·旋轉、裁剪頁面。
加密與解密：
·支援PDF的加密與密碼保護。
·解密已加密的PDF（如果知道密碼）。
優點：
·輕量且易用。
·支援大多數基本的PDF操作。
局限性：
·不支援複雜的PDF操作，如修改文本或表單填寫。

2. PDFMiner

文本提取：
·精確提取PDF文本內容，支援多種語言。
·支援解析PDF的字體、樣式與排版。
結構分析：
·可以提取文檔結構（如段落、表格、圖形等）。
優點：
·適合高精度的文本提取需求。
·支援處理嵌入式字體與標籤。
局限性：
·主要用於文本提取，缺乏對 PDF 修改的支持。

3. ReportLab

生成PDF：
·創建自定義PDF文檔。
·支援繪製圖形、表格、文字樣式。
報表生成：
·適合生成業務報表、發票或自定義設計的PDF。
優點：
·功能強大且靈活。
·完全專注於PDF生成。
局限性：
·不支援讀取或修改現有的PDF。

4. pdfplumber

文本與數據提取：
·提取PDF中的文本、表格數據和圖像。
·提供更精確的表格提取功能。
頁面解析：
·獲取每頁的詳細信息（如文本位置、字體等）。
優點：
·表格數據提取能力強。
·簡單易用，適合需要提取結構化數據的場景。
局限性：
·專注於數據提取，缺乏 PDF 編輯功能。

5. Fpdf (fpdf2)

PDF生成：
·支援快速生成PDF文檔。
·簡單地添加文字、圖像和表格。
輕量級：
·對於基本的 PDF 生成需求非常高效。
優點：
·易於上手，文檔清晰。
·適合小型項目或基本需求。
局限性：
·功能相對有限，不適合複雜的 PDF 生成或操作。

6. PyMuPDF (又名 Fitz)

文本提取與處理：
·支援高效的文本提取，包括字體和文本位置。
圖像處理：
·提取 PDF 中的圖像。
·修改圖像或頁面結構。
文檔操作：
·裁剪頁面、合併文檔、提取頁面。
優點：
·高性能，適合處理大文件。
·提供豐富的文檔操作功能。
局限性：
·API 相對較為複雜。

7. PDFKit

HTML 轉 PDF：
·將HTML或URL直接轉換為PDF。
格式保持：
·保留原始 HTML 的排版和樣式。
優點：
·非常適合將 Web 應用內容生成 PDF。
·簡單快捷。
局限性：
·依賴於wkhtmltopdf工具，需額外安裝。

庫名	         主要用途              優勢                  局限性
PyPDF2	        讀取、分割、合併PDF     簡單易用              無法修改文本或結構
PDFMiner	    高精度文本提取          支援多語言、結構分析    僅用於文本提取
ReportLab	    生成PDF報表            功能強大、靈活         無法處理現有 PDF
pdfplumber	    提取文本和結構化數據     表格提取能力強         無法修改或生成 PDF
Fpdf (fpdf2)	簡單的PDF生成          輕量、快速             功能有限
PyMuPDF	        提取和修改PDF          高性能、多功能         API較為複雜
PDFKit	        HTML轉PDF             保留HTML排版          需安裝外部工具wkhtmltopdf


將 Word 和 Excel 文件轉換為 PDF 通常需要借助專門的庫或工具。以下是一些常用方法和工具：

1. 使用 python-docx 和 win32com（適用於 Word 文件）
這種方法適用於Windows平台，依賴於Microsoft Word的COM介面。

安裝依賴：
pip install python-docx pywin32

範例程式碼：
import win32com.client

def word_to_pdf(input_path, output_path):
    # 打開 Word 應用
    word = win32com.client.Dispatch("Word.Application")
    doc = word.Documents.Open(input_path)
    # 將 Word 文件保存為 PDF
    doc.SaveAs(output_path, FileFormat=17)  # 17 表示 PDF 格式
    doc.Close()
    word.Quit()

範例使用
word_to_pdf("example.docx", "example.pdf")

優點：
完美保留Word文件的格式和內容。
局限性：
僅限於Windows平台，且需要安裝Microsoft Word。

2. 使用openpyxl和win32com（適用於Excel文件）
與Word的轉換類似，通過COM介面調用Excel。

安裝依賴：
pip install openpyxl pywin32

範例程式碼：
import win32com.client

def excel_to_pdf(input_path, output_path):
    # 打開 Excel 應用
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False
    workbook = excel.Workbooks.Open(input_path)
    # 將 Excel 保存為 PDF
    workbook.ExportAsFixedFormat(0, output_path)  # 0 表示 PDF 格式
    workbook.Close()
    excel.Quit()

範例使用
excel_to_pdf("example.xlsx", "example.pdf")

優點：
支援多頁Excel文件的高精度轉換。
局限性：
僅限於Windows平台，且需要安裝Microsoft Excel。

3. 使用pandoc（跨平台方法）
pandoc是一個強大的文件轉換工具，可以將多種格式轉為PDF。

安裝 Pandoc
安裝LaTeX（如TeX Live或MikTeX）以支持PDF生成。

使用範例（CLI命令）：
pandoc example.docx -o example.pdf

優點：
支援多種格式，跨平台。
不依賴Microsoft Office。
局限性：
對於格式複雜的文檔，可能需要額外調整。

4. 使用unoconv或LibreOffice（跨平台方法）
unoconv利用LibreOffice或OpenOffice將文件轉換為PDF。

安裝LibreOffice和unoconv：
安裝LibreOffice
安裝 unoconv：
sudo apt-get install unoconv

使用範例（CLI 命令）：
unoconv -f pdf example.docx
unoconv -f pdf example.xlsx

Python 中調用：
import subprocess

def convert_to_pdf(input_path, output_path):
    subprocess.run(["unoconv", "-f", "pdf", "-o", output_path, input_path])

範例使用
convert_to_pdf("example.docx", "example.pdf")
convert_to_pdf("example.xlsx", "example.pdf")

優點：
跨平台，支援多種格式。
不需要安裝 Microsoft Office。
局限性：
需要安裝額外的工具。
性能受限於LibreOffice的版本與配置。

5. 使用aspose（雲服務與本地庫）
Aspose 是一個專業的商業級工具，支援多種文件格式轉換。

安裝依賴：
pip install aspose-words
pip install aspose-cells

Word 範例：
from aspose.words import Document

def word_to_pdf(input_path, output_path):
    doc = Document(input_path)
    doc.save(output_path)

範例使用
word_to_pdf("example.docx", "example.pdf")

Excel 範例：
from aspose.cells import Workbook

def excel_to_pdf(input_path, output_path):
    workbook = Workbook(input_path)
    workbook.save(output_path, options={"save_format": "pdf"})

範例使用
excel_to_pdf("example.xlsx", "example.pdf")

優點：
專業級支持，精確保留格式。
跨平台，無需安裝 Microsoft Office。
局限性：
商業庫，需購買許可。

方法        支援格式          平台         是否需 Office   難度    適用場合
win32com    Word, Excel     Windows     是              中等    高精度格式轉換
pandoc      Word            跨平台       否              簡單    簡單文檔轉換
unoconv     Word, Excel     跨平台       否              中等    不依賴 Office
aspose      Word, Excel     跨平台       否              簡單    商業專業需求