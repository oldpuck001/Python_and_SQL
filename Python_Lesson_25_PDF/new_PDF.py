# new_PDF.py

from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

# 定義輸出的 PDF 文件路徑
text = '第一行內容\n第二行內容\n第三行內容'
path = '/Users/lei/Downloads/output.pdf'

# 字型文件路徑（macOS系統字型目錄或自定義安裝字型路徑）
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'  # 替換為系統中已安裝的中文字型路徑
font_name = 'STHeiti'                                   # 自定義字型名稱，和字型文件匹配

# 檢查字型文件是否存在
if not os.path.exists(font_path):
    raise FileNotFoundError(f"字型文件未找到：{font_path}")

# 註冊字型
pdfmetrics.registerFont(TTFont(font_name, font_path))

# 初始化樣式表
styles = getSampleStyleSheet()

# 自定義段落樣式
chinese_style = ParagraphStyle(
    'Chinese',                                          # 樣式名稱
    parent=styles['BodyText'],                          # 以預設的BodyText樣式為基礎
    fontName=font_name,                                 # 使用註冊的字型名稱
    fontSize=14,                                        # 字體大小設為14點
    leading=16                                          # 行距設為16點
)

# 將字符串以換行符拆分成多行文字，存成列表
lines = text.split('\n')

# 創建段落列表
story = [Paragraph(line, chinese_style) for line in lines]

# 建立 PDF 文件
file = SimpleDocTemplate(path)
file.build(story)

print(f"PDF 已生成：{path}")


# 注意事項
# 字型支援：
# Arial Unicode必須在系統中安裝，否則無法正確顯示中文。
# 若使用其他字型（如SimSun），需確保其名稱與系統中的字型一致。
# 換行符處理：
# 文本中的 \n 會被拆分成多段，生成PDF時每段會獨立顯示。
# 文字編碼：
# 輸入的文本（text）需要是UTF-8編碼，否則可能導致字元錯誤。