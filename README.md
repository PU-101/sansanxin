# 《散散心》（具体名字还没想好）

***

## Todo List:
* issue：
    * 手机端页面，发现点赞数和评论数不显示
    * 图片加载优化,图床（七牛）
* 加强爬虫:
    * 1、监测爬取网站内容更新，不再爬取所有内容；
    * 2、抓取代理，添加代理池，来源[peuland](https://proxy.peuland.com/proxy/search_proxy.php)
* 功能添加：
    * 添加消息推送功能，暂定使用现有的celery＋Redis
    * 爬取更多网站的内容，增加“感兴趣的话题”
    * 配置gevent

## 项目介绍

***

> 后段采用Django，前端采用Materialize；
功能主要分为两部分：blog和spider；
blog即为发布和浏览博文的功能，
spider为定向爬取指定网站指定内容的爬虫（目前为[蚂蜂窝](http://www.mafengwo.cn)）；


### Blog

#### Model

##### 模型框图：
![Model](https://raw.githubusercontent.com/PU-101/pics/master/sansanxin-model-2.png)
> 注：空箭头：1、黑圆点：多

关系结构由单独的Like、Comment和Follow表来存储，保持User、UserProfile和Post表的纯净。并且所有的多对多关系均通过多对一来表示，构造表的时候也较为方便。

##### Signals
***
表之间许多相互影响的字段通过Signals来进行及时自动修改,主要有如下几种情况：
* 创建User对象的时候自动创建相应一对一的UserProfile对象；
* 创建或删除Like、Comment、Follow对象的时候，自动修改相应的Post或UserProfile对象中存储数量的字段的值；
这样做，保证了view的干净，并且配置好后，即可放心使用。


