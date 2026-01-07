# sheet_comparision.py

from gui_tk import gui_tk_root

title = '电子表格对比'
geometry = '720x480+50+50'
control_frame_n = 1
control_frame_config = [
                        {'name':                'sheet_comparision',
                        'button_name':          ['选择文件 1', '选择文件 2', '开始对比'],
                        'function_name':        '',
                        'function_para':        ''},

                        {'text_area_hight':     19}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()