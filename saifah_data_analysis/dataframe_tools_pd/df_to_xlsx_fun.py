# df_to_xlsx.py

# 导出xlsx文件
def df_to_xlsx(df, path, index=True):

    try:
        df.to_excel(path, index=index)
        info = f'Export successfully!\nFile path: {path}\n'
        return [True, info]
    
    except:
        info = 'Export failed!\n'
        return [False, info]