
import os
from tkinter import filedialog

def path_join(path, path_m):

    if isinstance(path_m, list):
        
        if len(path_m) == 1:

            path = os.path.join(path, path_m[0])

            os.makedirs(path, exist_ok=True)

        else:

            for n in path_m[1]:

                path_join(os.path.join(path, path_m[0]), n)

    else:

        os.makedirs(path, exist_ok=True)


path_list = [
                ['项目数据'],
        
                ['审计底稿', 
                                [
                                    ['1.初步业务活动'],
                                    ['2.风险评估'],
                                    ['3.控制测试'],
                                    ['4.实质性程序'],
                                    ['5.其他项目'],
                                    ['6.完成审计工作'],
                                    ['7.永久性档案'],
                                    ['8.底稿附件'],
                                    ['9.记账凭证检查拍照'],
                                ]
                ],
                
                ['审计报告'],

                ['原始资料']
            ]

path = filedialog.askdirectory()

if path:

    for path_m in path_list:

        path_join(path, path_m)