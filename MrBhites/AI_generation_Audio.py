import GPT_SoVITS.inference_webui_fast as GS
import GPT_SoVITS.const as GS_const
import sounddevice


def speak(text_content):
    result = GS.inference(text_content, *(GS_const.inputs))
    for r in result:
        sr = r[0]
        content = r[1]
    sounddevice.play(content, sr)