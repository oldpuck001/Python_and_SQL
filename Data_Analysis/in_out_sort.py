# in_out_sort.py

from gui_tk import gui_tk_root

title = 'In/Out Value Sort'
geometry = '720x480+50+50'
control_frame_n = 1
control_frame_config = [
                        {'name':                'in_out_sort',
                         'widget_text':         ['Import', 'Export'],
                         'function_name':       '',
                         'function_para':       ''},

                        {'text_area_hight':     10}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()