text="" # 需要生成语音的内容
text_language="多语种混合" # 需要生成语音的语言
inp_ref="D:\\My\\Work\\BLive\\LiveHouse\\MrBhites\\GPT_SoVITS\\res\\雪莲\\Azuma Max\\Azuma_4.wav" #主参考音频
inp_refs=[ #辅参考音频
        "D:\\My\\Work\\BLive\\LiveHouse\\MrBhites\\GPT_SoVITS\\res\\雪莲\\Azuma Max\\Azuma_1.wav",
        "D:\\My\\Work\\BLive\\LiveHouse\\MrBhites\\GPT_SoVITS\\res\\雪莲\\Azuma Max\\Azuma_2.wav",
        "D:\\My\\Work\\BLive\\LiveHouse\\MrBhites\\GPT_SoVITS\\res\\雪莲\\Azuma Max\\Azuma_3.wav",
        "D:\\My\\Work\\BLive\\LiveHouse\\MrBhites\\GPT_SoVITS\\res\\雪莲\\Azuma Max\\Azuma_4.wav",
        "D:\\My\\Work\\BLive\\LiveHouse\\MrBhites\\GPT_SoVITS\\res\\雪莲\\Azuma Max\\Azuma_5.wav",
        "D:\\My\\Work\\BLive\\LiveHouse\\MrBhites\\GPT_SoVITS\\res\\雪莲\\Azuma Max\\Azuma_6.wav",
        "D:\\My\\Work\\BLive\\LiveHouse\\MrBhites\\GPT_SoVITS\\res\\雪莲\\Azuma Max\\Azuma_7.wav",
        "D:\\My\\Work\\BLive\\LiveHouse\\MrBhites\\GPT_SoVITS\\res\\雪莲\\Azuma Max\\Azuma_8.wav",
        "D:\\My\\Work\\BLive\\LiveHouse\\MrBhites\\GPT_SoVITS\\res\\雪莲\\Azuma Max\\Azuma_9.wav",
        "D:\\My\\Work\\BLive\\LiveHouse\\MrBhites\\GPT_SoVITS\\res\\雪莲\\Azuma Max\\Azuma_10.wav"
] 
prompt_text="你是真的愿挨阿，你油盐不进阿" # 主参考音频内容
prompt_language="中文" # 主参考音频语言
top_k=5 # 5
top_p=1
temperature=1
how_to_cut="凑四句一切"
batch_size=20
speed_factor=1.0
ref_text_free=True
split_bucket=True
fragment_interval=0.3
seed=-1
keep_random=True
parallel_infer=True
repetition_penalty=1.35

inputs = [ # 不包含上述的text，其由调用模块自行加入
            text_language, inp_ref, inp_refs,
            prompt_text, prompt_language, 
            top_k, top_p, temperature, 
            how_to_cut, batch_size, 
            speed_factor, ref_text_free,
            split_bucket,fragment_interval,
            seed, keep_random, parallel_infer,
            repetition_penalty
        ]