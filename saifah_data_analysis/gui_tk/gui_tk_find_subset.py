# gui_tk_find_subset.py

import pandas as pd
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from gui_tk import gui_tk_area_text
from dataframe_tools_pd import sheetnames_import_fun
from dataframe_tools_pd import columns_title_fun
from dataframe_tools_pd import read_xlsx_xls_csv_txt_fun
from dataframe_tools_pd import df_cleaning_fun
from xlsx_tools_openxl import export_new_xlsx_fun

class gui_tk_find_subset_class:

    def gui_tk_find_subset_frame(self, root, control_frame_config, text_area):

        frame_result = tk.Frame(root)
        frame_result.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        frame_result.frame_1 = tk.Frame(frame_result)
        frame_result.frame_1.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_1, text='File Path', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_1.entry_widget = tk.Entry(frame_result.frame_1, state='readonly', readonlybackground='white')
        frame_result.frame_1.entry_widget.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        frame_result.frame_2 = tk.Frame(frame_result)
        frame_result.frame_2.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_2, text='目标值', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_2.entry_value = tk.Entry(frame_result.frame_2, width=22)
        frame_result.frame_2.entry_value.pack(side=tk.LEFT, padx=5, pady=5)

        options = []

        frame_result.frame_3 = tk.Frame(frame_result)
        frame_result.frame_3.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_3, text='选择工作表', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_3.combobox_sheet = ttk.Combobox(frame_result.frame_3, values=options, state='readonly')
        frame_result.frame_3.combobox_sheet.pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_4 = tk.Frame(frame_result)
        frame_result.frame_4.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_4, text='选择项目列', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_4.combobox_item = ttk.Combobox(frame_result.frame_4, values=options, state='readonly')
        frame_result.frame_4.combobox_item.pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_5 = tk.Frame(frame_result)
        frame_result.frame_5.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_5, text='选择数值列', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_5.combobox_value = ttk.Combobox(frame_result.frame_5, values=options, state='readonly')
        frame_result.frame_5.combobox_value.pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_6 = tk.Frame(frame_result)
        frame_result.frame_6.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Button(frame_result.frame_6, text=control_frame_config['button_name'][0],
                  command=lambda e=frame_result.frame_1.entry_widget,
                                 f=frame_result.frame_3.combobox_sheet,
                                 g=frame_result.frame_4.combobox_item,
                                 h=frame_result.frame_5.combobox_value: self.input_sheet(e,f,g,h,text_area),
                  width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_result.frame_6, text=control_frame_config['button_name'][1],
                  command=lambda e=frame_result.frame_1.entry_widget,
                                 f=frame_result.frame_2.entry_value,
                                 g=frame_result.frame_3.combobox_sheet,
                                 h=frame_result.frame_4.combobox_item,
                                 i=frame_result.frame_5.combobox_value: self.find_subset(e,f,g,h,i,text_area),
                  width=10).pack(side=tk.LEFT, padx=5)

        frame_result.frame_3.combobox_sheet.bind('<<ComboboxSelected>>',
                                                  lambda event: self.on_sheet_change(event,
                                                                                     frame_result.frame_1.entry_widget,
                                                                                     frame_result.frame_3.combobox_sheet,
                                                                                     frame_result.frame_4.combobox_item,
                                                                                     frame_result.frame_5.combobox_value))

        return frame_result


    # 导入按钮函数
    def input_sheet(self, entry_file, combobox_sheet, combobox_item, combobox_value, text_area):

        fill_text = ''
        path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx'),
                                                     ('Excel Files', '*.xls')])

        if path:
            entry_file.config(state='normal')
            entry_file.delete(0, tk.END)
            entry_file.insert(0, path)
            entry_file.config(state='readonly')
            fill_text += f'Selected: {path}\n'
            fill_text += 'File selection successful!\n'

            sheets_name_result = sheetnames_import_fun.sheetnames_import(path)
            if sheets_name_result[0]:

                sheets_name_list = sheets_name_result[2]
                combobox_sheet['values'] = sheets_name_list
                combobox_sheet.set(sheets_name_list[0])               # 设置默认选择第一个
                combobox_sheet.config(state='readonly')

            else:

                combobox_sheet.set('')
                combobox_sheet.config(state='disabled')

            fill_text += sheets_name_result[1]

        else:
            fill_text += f'File selection failed!\n'

        self.on_sheet_change(None, entry_file, combobox_sheet, combobox_item, combobox_value)

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 自动更新列名列表
    def on_sheet_change(self, event, file_entry, combobox_sheet, combobox_item, combobox_value):

        file_path = file_entry.get()
        sheet_name = combobox_sheet.get()

        result = columns_title_fun.columns_title(file_path, sheet_name)

        if result[0]:
            new_options = result[1]

            combobox_item['values'] = new_options
            if new_options[0]:
                combobox_item.set(new_options[0])
            combobox_item.config(state='readonly')

            combobox_value['values'] = new_options
            if new_options[0]:
                combobox_value.set(new_options[0])
            combobox_value.config(state='readonly')


    # 凑数按钮函数
    def find_subset(self, file_entry, value_entry, combobox_sheet, combobox_item, combobox_value, text_area):

        fill_text = ''
        file_path = file_entry.get()
        target_value = value_entry.get()
        sheet_name = combobox_sheet.get()
        col_name = combobox_item.get()
        col_num = combobox_value.get()

        # 转换目标值为 float
        target_value = float(str(target_value).replace(',', '').strip() or 0)

        # 读入数据
        result_info = read_xlsx_xls_csv_txt_fun.read_xlsx_xls_csv_txt(file_path=file_path, sheet_name=sheet_name)

        if result_info[0]:

            df = result_info[2]
            value_name = df[col_name].tolist()
            result_cleaned = df_cleaning_fun.df_cleaning(df, col_num, 'to_float')
            if result_cleaned[0]:
                df = result_cleaned[2]
            value_num = df[col_num].tolist()

        # 仅剔除数值为 0 的项，保留名称为空的项
        valid_pairs = [
            (name, num)
            for name, num in zip(value_name, value_num)
            if num != 0.0
        ]

        # 若没有有效数据，直接导出提示
        if not valid_pairs:
            fill_text += '无有效数据，所有数值均为 0\n'
            gui_tk_area_text.text_area_fill(text_area, fill_text)
            return

        tolerance = 0.00000001

        dp = {0.0: [[]]}
        results = []

        for name, num in valid_pairs:
            new_dp = {}
            for current_sum in dp:
                new_sum = current_sum + num
                subset_list = dp[current_sum]
                for subset in subset_list:
                    new_subset = subset + [(name, num)]
                    if abs(new_sum - target_value) <= tolerance:
                        results.append(new_subset)
                    if new_sum not in new_dp:
                        new_dp[new_sum] = []
                    new_dp[new_sum].append(new_subset)
            for k, v in new_dp.items():
                if k not in dp:
                    dp[k] = []
                dp[k].extend(v)

        if not results:
            fill_text += '未找到满足条件的组合。\n'
            gui_tk_area_text.text_area_fill(text_area, fill_text)
            return

        # 输出结果，每组加小计和空行
        output_data = []
        for idx, subset in enumerate(results, 1):
            total = 0.0
            for name, num in subset:
                output_data.append({
                    '组合编号': f'组合 {idx}',
                    '名称': name,
                    '数值': num,
                })
                total += num
            output_data.append({
                '组合编号': f'组合 {idx}',
                '名称': '小计',
                '数值': total,
            })
            output_data.append({})              # 空行分隔

        df_result = pd.DataFrame(output_data)

        result_info = export_new_xlsx_fun.export_new_xlsx(df_result)
        if result_info[0]:
            fill_text += result_info[1]
            subprocess.run(['open', result_info[2]])
        else:
            fill_text += '导出失败！'

        gui_tk_area_text.text_area_fill(text_area, fill_text)