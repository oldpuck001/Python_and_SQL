# text_to_audio.py

# 这段Python代码是使用Azure的Cognitive Services的语音服务（Speech Service）进行文字转语音（Text-to-Speech，简称TTS）的示例

#导入os模块和azure.cognitiveservices.speech模块。
# os模块用于获取环境变量。
# azure.cognitiveservices.speech模块则是Azure的Cognitive Services的语音服务SDK。
import os
import azure.cognitiveservices.speech as speechsdk

# 语音服务的订阅密钥和区域通常在Azure的门户网站上设置。
SPEECH_KEY = 'SPEECH_KEY'
SPEECH_REGION = 'SPEECH_REGION'

#然后创建一个SpeechConfig对象
speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)

# 创建一个AudioOutputConfig对象，配置使用默认的扬声器输出语音。
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

#设置语音服务的语音配置的属性speech_synthesis_voice_name为'en-US-JennyNeural'，这是美式英语的一种语音模型。
# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name='en-US-JennyNeural'

#创建一个SpeechSynthesizer对象，用于执行文字转语音的任务。这个对象需要传入SpeechConfig和AudioOutputConfig对象作为参数。
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

#通过控制台输入文字
# Get text from the console and synthesize to the default speaker.
print("Enter some text that you want to speak >")
text = input()

#调用SpeechSynthesizer对象的speak_text_async方法进行异步的文字转语音任务，得到一个speech_synthesis_result结果对象。
speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

#判断语音合成的结果。
#如果speech_synthesis_result.reason为SynthesizingAudioCompleted，则表示语音合成成功。
#如果为Canceled，则表示语音合成被取消。
#如果取消的原因是CancellationReason.Error，则表示有错误发生，进一步打印错误的详细信息。
if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

# 这段代码的主要功能是将输入的文字转换为语音并通过默认的扬声器播放出来，如果在语音合成过程中出现错误，还会打印错误信息。
# 使用speech_synthesizer.speak_text_async(text)將文字轉換為 MP3 音頻文件造成程序崩潰的原因和解決方法
# 程式碼使用了Azure的語音服務將文字轉換為MP3音頻文件。Python在崩潰時，正是在使用 speak_text_async(text) 該函數。
# 這個函數是異步的，會立即返回，而不會等待語音合成完成。這個特性可能是問題所在。
# 在異步語音合成的情況下，一旦Python主程式結束，語音合成可能還在進行。
# 由於Python程序結束會導致資源回收，如網路連接等，這將導致進行中的語音合成任務無法完成，甚至可能導致當前進程崩潰。
# 因此，我們需要等待語音合成任務完成再結束主程式。

# 修改最後一行代碼如下：

# result_future = speech_synthesizer.speak_text_async(text)
# result_future.get()

# 在上述修改中，speak_text_async(text) 返回一個Future對象，可以通過調用 result_future.get() 來等待異步任務完成。
# 這樣，就能確保語音合成任務在主程式結束前完成，避免了可能導致崩潰的資源回收問題。