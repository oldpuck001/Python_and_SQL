# GUI_Tkinter.py

import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import subprocess
import azure.cognitiveservices.speech as speechsdk

def update_option_menu_state(checkbutton_var, option_menu):
    # 根据 Checkbutton 的状态更新 OptionMenu 的状态
    if checkbutton_var.get():
        option_menu.config(state=tk.NORMAL)         # 启用 OptionMenu
    else:
        option_menu.config(state=tk.DISABLED)       # 禁用 OptionMenu

def import_file():

    file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx'), ('Excel Files', '*.xls')])

    if file_path:
        import_file_entry.config(state='normal')
        import_file_entry.delete(0, tk.END)
        import_file_entry.insert(0, file_path)
        import_file_entry.config(state='readonly')

        sheet_file = pd.ExcelFile(file_path)
        sheetnames = sheet_file.sheet_names

        sheet_selected_option.set('')
        sheet_option_menu['menu'].delete(0, 'end')
        for sheet in sheetnames:
            sheet_option_menu['menu'].add_command(label=sheet, command=tk._setit(sheet_selected_option, sheet))

def select_folder():

    folder_path = filedialog.askdirectory()
    folder_entry.config(state='normal')
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)
    folder_entry.config(state='readonly')

def export_file():

    # 快速入门：将文本转换为语音
    # https://learn.microsoft.com/zh-cn/azure/ai-services/speech-service/get-started-text-to-speech?tabs=windows%2Cterminal&pivots=programming-language-python

    file_path = import_file_entry.get()
    speechKey = speechKey_entry.get()
    speechRegion = speechRegion_entry.get()
    maleVoice = male_var.get()
    maleRepeats = male_selected_option.get()
    maleTranslate = male_translate_var.get()
    maleExample = male_example_var.get()
    femaleVoice = female_var.get()
    femaleRepeats = female_selected_option.get()
    femaleTranslate = female_translate_var.get()
    femaleExample = female_example_var.get()
    language = language_selected_option.get()
    sheet = sheet_selected_option.get()
    singleAudio = single_audio_var.get()
    folder_path = folder_entry.get()

    save_path = filedialog.asksaveasfilename(defaultextension=".mp3",filetypes=[("MP3 Files","*.mp3")])

    if folder_path == '':
        folder_path, file_name = os.path.split(save_path)
        folder_name = os.path.splitext(file_name)[0]                # 去除文件擴展名，生成同名文件夾路徑
        if singleAudio == True:
            save_folder = os.path.join(folder_path, folder_name)
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)
    else:
        save_folder = folder_path

    temporary_folder = os.path.join(folder_path, 'temporary_folder')
    if not os.path.exists(temporary_folder):
        os.makedirs(temporary_folder)

    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.xlsx':
        vocabulary_df = pd.read_excel(file_path, sheet_name=sheet, engine='openpyxl')
    elif file_extension == '.xls':
        vocabulary_df = pd.read_excel(file_path, sheet_name=sheet, engine='xlrd')

    column_word = vocabulary_df.iloc[:, 0]

    # 初始化 Speech SDK 設定
    speech_config = speechsdk.SpeechConfig(subscription=speechKey, region=speechRegion)
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio48Khz96KBitRateMonoMp3)

    # 准備空的音頻流列表
    audio_segments = []
    num = 0

    for word in column_word:
        if singleAudio == True:
            audio_segment = []

        if maleVoice == True:
            if language == '英语':
                voice_name = "en-US-GuyNeural"
            elif language == '日语':
                voice_name = "ja-JP-KeitaNeural"
            elif language == '泰语':
                voice_name = "th-TH-NiwatNeural"

            if maleRepeats == '1遍':
                word_text = word
            elif maleRepeats == '2遍':
                word_text = word + '\n' + word
            elif maleRepeats == '3遍':
                word_text = word + '\n' + word + '\n' + word

            save_file_male = os.path.join(temporary_folder, f'{word}_male.mp3')
            audio_male = synthesize_speech_to_file(word_text, voice_name, save_file_male, speech_config)
            audio_segments.append(save_file_male)
            if singleAudio == True:
                audio_segment.append(save_file_male)

        if femaleVoice == True:
            if language == '英语':
                voice_name = "en-US-JennyNeural"
            elif language == '日语':
                voice_name = "ja-JP-NanamiNeural"
            elif language == '泰语':
                voice_name = "th-TH-PremwadeeNeural"

            if femaleRepeats == '1遍':
                word_text = word
            elif femaleRepeats == '2遍':
                word_text = word + '\n' + word
            elif femaleRepeats == '3遍':
                word_text = word + '\n' + word + '\n' + word

            save_file_female = os.path.join(temporary_folder, f'{word}_female.mp3')
            audio_female = synthesize_speech_to_file(word_text, voice_name, save_file_female, speech_config)
            audio_segments.append(save_file_female)
            if singleAudio == True:
                audio_segment.append(save_file_female)

        if maleTranslate == True:
            word_text = vocabulary_df.iloc[num, 1]
            save_file_male = os.path.join(temporary_folder, f'{word}_male_translate.mp3')
            audio_male_translate = synthesize_speech_to_file(word_text, 'zh-TW-YunJheNeural', save_file_male, speech_config)
            audio_segments.append(save_file_male)
            if singleAudio == True:
                audio_segment.append(save_file_male)

        if femaleTranslate == True:
            word_text = vocabulary_df.iloc[num, 1]
            save_file_female = os.path.join(temporary_folder, f'{word}_female_translate.mp3')
            audio_female_translate = synthesize_speech_to_file(word_text, 'zh-TW-HsiaoYuNeural', save_file_female, speech_config)
            audio_segments.append(save_file_female)
            if singleAudio == True:
                audio_segment.append(save_file_female)

        if maleExample == True:
            word_text = vocabulary_df.iloc[num, 2]
            save_file_male = os.path.join(temporary_folder, f'{word}_male_example.mp3')
            if language == '英语':
                voice_name = "en-US-GuyNeural"
            elif language == '日语':
                voice_name = "ja-JP-KeitaNeural"
            elif language == '泰语':
                voice_name = "th-TH-NiwatNeural"
            audio_male_example = synthesize_speech_to_file(word_text, voice_name, save_file_male, speech_config)
            audio_segments.append(save_file_male)
            if singleAudio == True:
                audio_segment.append(save_file_male)

        if femaleExample == True:
            word_text = vocabulary_df.iloc[num, 2]
            save_file_female = os.path.join(temporary_folder, f'{word}_female_example.mp3')
            if language == '英语':
                voice_name = "en-US-JennyNeural"
            elif language == '日语':
                voice_name = "ja-JP-NanamiNeural"
            elif language == '泰语':
                voice_name = "th-TH-PremwadeeNeural"
            audio_female_example = synthesize_speech_to_file(word_text, voice_name, save_file_female, speech_config)
            audio_segments.append(save_file_female)
            if singleAudio == True:
                audio_segment.append(save_file_female)

        if singleAudio == True:
            save_file = os.path.join(save_folder, f'{word}.mp3')
            # 使用 FFmpeg 合并音频文件
            command = ['ffmpeg']
            for file in audio_segment:
                command.extend(['-i', file])
            command.extend(['-filter_complex', 'concat=n={}:v=0:a=1'.format(len(audio_segment)), save_file])
            subprocess.run(command, check=True)

        num += 1

    # 使用 FFmpeg 合并音频文件
    command = ['ffmpeg']
    for file in audio_segments:
        command.extend(['-i', file])
    command.extend(['-filter_complex', 'concat=n={}:v=0:a=1'.format(len(audio_segments)), save_path])
    subprocess.run(command, check=True)

    # 删除临时文件夹
    shutil.rmtree(temporary_folder)

    # 通知生成结果
    messagebox.showinfo('信息', '生成音频成功！')

# 創建 Speech Synthesizer，將音頻保存到文件中
def synthesize_speech_to_file(word_text, voice_name, output_filename, speech_config):

    word_text = word_text
    speech_config.speech_synthesis_voice_name = voice_name
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_filename)
    
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    result = speech_synthesizer.speak_text_async(word_text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        return output_filename
    else:
        return None


# 創建 Tk 的實例
root = tk.Tk()

# 設置窗口的標題
root.title("单词表转音频")

# 設置窗口的大小與位置（+10+20' 設定了窗口左上角位於屏幕的(10, 20)位置）
root.geometry('960x500+140+130')

# 設置窗口的最小大小
root.minsize(640, 360)

# 設置窗口的最大大小
root.maxsize(1280, 720)

# 設置窗口是否可以被用戶調整大小，兩個參數分別表示寬度和高度是否可以調整
root.resizable(False, False)

# 纵向框架
vertical_frame = tk.Frame(root)
vertical_frame.pack()

# 导入文件文件路径
import_file_frame = tk.Frame(vertical_frame)
import_file_frame.pack(side=tk.TOP, fill=tk.X, expand=True, padx=10, pady=10)
import_file_label = tk.Label(import_file_frame, text='导入文件路径', width=20, anchor=tk.W)
import_file_label.pack(side=tk.LEFT)
import_file_entry = tk.Entry(import_file_frame, width=105, state='readonly')
import_file_entry.pack(side=tk.LEFT)

# speechKey框架
speechKey_frame = tk.Frame(vertical_frame)
speechKey_frame.pack(side=tk.TOP, fill=tk.X, expand=True, padx=10, pady=10)
speechKey_label = tk.Label(speechKey_frame, text='SPEECH KEY', width=20, anchor=tk.W)
speechKey_label.pack(side=tk.LEFT)
speechKey_entry = tk.Entry(speechKey_frame, width=105)
speechKey_entry.pack(side=tk.LEFT)

# speechRegion框架
speechRegion_frame = tk.Frame(vertical_frame)
speechRegion_frame.pack(side=tk.TOP, fill=tk.X, expand=True, padx=10, pady=10)
speechRegion_label = tk.Label(speechRegion_frame, text='SPEECH REGION', width=20, anchor=tk.W)
speechRegion_label.pack(side=tk.LEFT)
speechRegion_entry = tk.Entry(speechRegion_frame, width=105)
speechRegion_entry.pack(side=tk.LEFT)

# male框架
male_frame = tk.Frame(vertical_frame)
male_frame.pack(side=tk.TOP, fill=tk.X, expand=True, padx=10, pady=10)
male_label = tk.Label(male_frame, text='男声朗读选择', width=20, anchor=tk.W)
male_label.pack(side=tk.LEFT)
male_var = tk.BooleanVar(value=True)
male_Checkbutton = tk.Checkbutton(male_frame, text='男声朗读', variable=male_var, command=lambda: update_option_menu_state(male_var, male_option_menu))
male_Checkbutton.pack(side=tk.LEFT)
male_selected_option = tk.StringVar(male_frame)
male_options = ['1遍', '2遍', '3遍']
male_option_menu = tk.OptionMenu(male_frame, male_selected_option, *male_options)
male_selected_option.set(male_options[1])
male_option_menu.pack(side=tk.LEFT)
male_translate_var = tk.BooleanVar(value=False)
male_translate_Checkbutton = tk.Checkbutton(male_frame, text='男声朗读译文', variable=male_translate_var)
male_translate_Checkbutton.pack(side=tk.LEFT, padx=35)
male_example_var = tk.BooleanVar(value=False)
male_example_Checkbutton = tk.Checkbutton(male_frame, text='男声朗读例句', variable=male_example_var)
male_example_Checkbutton.pack(side=tk.LEFT)

# female框架
female_frame = tk.Frame(vertical_frame)
female_frame.pack(side=tk.TOP, fill=tk.X, expand=True, padx=10, pady=10)
female_label = tk.Label(female_frame, text='女声朗读选择', width=20, anchor=tk.W)
female_label.pack(side=tk.LEFT)
female_var = tk.BooleanVar(value=False)
female_Checkbutton = tk.Checkbutton(female_frame, text='女声朗读', variable=female_var, command=lambda: update_option_menu_state(female_var, female_option_menu))
female_Checkbutton.pack(side=tk.LEFT)
female_selected_option = tk.StringVar(female_frame)
female_options = ['1遍', '2遍', '3遍']
female_option_menu = tk.OptionMenu(female_frame, female_selected_option, *female_options)
female_selected_option.set(female_options[1])
female_option_menu.pack(side=tk.LEFT)
update_option_menu_state(female_var, female_option_menu)
female_translate_var = tk.BooleanVar(value=False)
female_translate_Checkbutton = tk.Checkbutton(female_frame, text='女声朗读译文', variable=female_translate_var)
female_translate_Checkbutton.pack(side=tk.LEFT, padx=35)
female_example_var = tk.BooleanVar(value=False)
female_example_Checkbutton = tk.Checkbutton(female_frame, text='女声朗读例句', variable=female_example_var)
female_example_Checkbutton.pack(side=tk.LEFT)

# language框架
language_frame = tk.Frame(vertical_frame)
language_frame.pack(side=tk.TOP, fill=tk.X, expand=True, padx=10, pady=10)
language_label = tk.Label(language_frame, text='语种选择', width=20, anchor=tk.W)
language_label.pack(side=tk.LEFT)
language_selected_option = tk.StringVar(language_frame)
language_options = ['英语', '日语', '泰语']
language_option_menu = tk.OptionMenu(language_frame, language_selected_option, *language_options)
language_selected_option.set(language_options[1])
language_option_menu.pack(side=tk.LEFT)

# 选择工作表框架
sheet_frame = tk.Frame(vertical_frame)
sheet_frame.pack(side=tk.TOP, fill=tk.X, expand=True, padx=10, pady=10)
sheet_label = tk.Label(sheet_frame, text='选择工作表', width=20, anchor=tk.W)
sheet_label.pack(side=tk.LEFT)
sheet_selected_option = tk.StringVar(sheet_frame)
sheet_options = ['']
sheet_option_menu = tk.OptionMenu(sheet_frame, sheet_selected_option, *sheet_options)
sheet_selected_option.set(sheet_options[0])
sheet_option_menu.pack(side=tk.LEFT)

# 是否生成单字音频框架
single_audio_frame = tk.Frame(vertical_frame)
single_audio_frame.pack(side=tk.TOP, fill=tk.X, expand=True, padx=10, pady=10)
single_audio_label = tk.Label(single_audio_frame, text='是否生成单字音频', width=20, anchor=tk.W)
single_audio_label.pack(side=tk.LEFT)
single_audio_var = tk.BooleanVar(value=False)
yes_radio = tk.Radiobutton(single_audio_frame, text='是', variable=single_audio_var, value=True, padx=30)
yes_radio.pack(side=tk.LEFT)
no_radio = tk.Radiobutton(single_audio_frame, text='否', variable=single_audio_var, value=False, padx=30)
no_radio.pack(side=tk.LEFT)

# 单字音频输出文件夹框架
folder_frame = tk.Frame(vertical_frame)
folder_frame.pack(side=tk.TOP, fill=tk.X, expand=True, padx=10, pady=10)
folder_label = tk.Label(folder_frame, text='单字音频输出文件夹', width=20, anchor=tk.W)
folder_label.pack(side=tk.LEFT)
folder_entry = tk.Entry(folder_frame, width=105, state='readonly')
folder_entry.pack(side=tk.LEFT)

# Button
button_frame = tk.Frame(vertical_frame)
button_frame.pack(side=tk.TOP, fill=tk.X, expand=True, padx=10, pady=10)
import_button = tk.Button(button_frame, text='导入xlsx文件', command=import_file, width=20)
import_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True)
select_button = tk.Button(button_frame, text='输出单子音频文件夹', command=select_folder, width=20)
select_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True)
export_button = tk.Button(button_frame, text='生成语音文件', command=export_file, width=20)
export_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True)


root.mainloop()