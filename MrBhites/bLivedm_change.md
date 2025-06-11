# 2025-6-9更改
## 弹幕监听
- 由于近期B站的更新，对于防爬取功能有了新的校验手段，在此之前，对于```https://api.live.bilibili.com/room/v1/Room/get_info```这个接口的请求中，param只有id和type两个参数，而更改后开始采用 WBI 签名鉴权，正常的请求应有如下图所示的param:
- ![新的param示例](新的param.png)
- B站具体对于WBI签名鉴权的更改如[这个文档所示](https://socialsisteryi.github.io/bilibili-API-collect/docs/misc/sign/wbi.html)
- 故增加对应的鉴权处理函数