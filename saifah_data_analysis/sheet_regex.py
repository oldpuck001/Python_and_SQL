# sheet_regex.py

from gui_tk import gui_tk_root

title = '使用正则表达式筛选'
geometry = '1280x720+50+50'
control_frame_n = 1
control_frame_config = [
                        {'name':                'sheet_regex',
                         'widget_text':         ['选择文件', '导入数据', '预览数据', '添加regex', '[]', 'AND', 'OR', '执行筛选', '导出文件'],
                         'function_name':       '',
                         'function_para':       ''},

                        {'text_area_hight':     18}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()