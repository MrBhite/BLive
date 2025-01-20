text=""
text_language=""
inp_ref="./res/雪莲/Azuma Max/Azuma_4.wav" #主参考音频
inp_refs="" #辅参考音频
prompt_text=""
prompt_language=""
top_k=""
top_p=""
temperature=""
how_to_cut=""
batch_size=""
speed_factor=""
ref_text_free=""
split_bucket=""
fragment_interval=""
seed=""
keep_random=""
parallel_infer=""
repetition_penalty=""

inputs = [
            text,text_language, inp_ref, inp_refs,
            prompt_text, prompt_language, 
            top_k, top_p, temperature, 
            how_to_cut, batch_size, 
            speed_factor, ref_text_free,
            split_bucket,fragment_interval,
            seed, keep_random, parallel_infer,
            repetition_penalty
        ]