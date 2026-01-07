# sheet_subtotals.py

from gui_tk import gui_tk_root

title = '分类汇总表格'
geometry = '720x480+50+50'
control_frame_n = 1
control_frame_config = [
                        {'name':                'sheet_subtotals',
                        'button_name':          ['导入', '生成'],
                        'function_name':        '',
                        'function_para':        ''},

                        {'text_area_hight':     16}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()