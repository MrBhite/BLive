# 使用方法
- 在main.py里输入第19行处输入一个cookie的SESSDATA字段的值
- 在main.py里第14行处输入直播间ID
- 直接运行startup.bat

# BLive
- 基于blive弹幕监听等功能的一系列软件

# 弹幕监听
- refernce文件夹中保留有[引用项目](https://github.com/yulinfeng000/blive)的弹幕监听框架与简单示例，由于其23年即停止维护，故进行了框架修复，具体更改如下：
  - 在eeframework.py及core.py中，针对建立ws链接的代码，在请求头中增加了```User-Agent```属性(需注意的是，缺少此属性会造成链接建立失败，ws下行数据遗漏等现象)。
  - 在blive文件夹下新添加const.py文件，以储存代码中的常量
  - 在框架代码中添加```if TEST:```语句，用以调试
- 上述引用项目不好使，改使用[这个项目](https://github.com/xfgryujk/blivedm/tree/dev)

# 生成型AI语音输出
## 更改模型和数据集
- 在```MrBhites/GPT_SoVITS/res```下面放置数据文件(最好以生源为目录，将数据集和两个模型放在同一目录下)
- 在```MrBhites/GPT_SoVITS/const.py```下更新参考音频目录(绝对路径),
- 在```MrBhites/GPT_SoVITS/configs/tts_infer.yaml```下更新模型路径(以项目目录为根的相对路径)
# 语音输入控制

# 直播页面开发