# BLive
- 基于blive弹幕监听等功能的一系列软件

# 弹幕监听
- 在res/blive-main中下载有作者yulinfeng000([点击跳转github主页](https://github.com/yulinfeng000))的弹幕监听框架与简单示例，由于其23年即停止维护，故进行了框架修复，具体更改如下：
  - 在eeframework.py及core.py中，针对建立ws链接的代码，在请求头中增加了```User-Agent```属性(需注意的是，缺少此属性会造成链接建立失败，ws下行数据遗漏等现象)。
  - 在blive文件夹下新添加const.py文件，以储存代码中的常量
  - 在框架代码中添加```if TEST:```语句，用以调试

# test2