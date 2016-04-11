# 《散散心》（具体名字还没想好）

***

## Todo List:
* issue：
    * 手机端页面，发现点赞数和评论数不显示
    * 图片加载优化,图床（七牛）
* 加强爬虫:
    * 1、监测爬取网站内容更新，不再爬取所有内容；
    * 2、抓取代理，添加代理池，来源[peuland](https://proxy.peuland.com/proxy/search_proxy.php)
    * 3、集成错误信息收集页面
* 功能添加：
    * 添加活动发布及团队集结功能
    * 添加消息推送功能，暂定使用现有的celery＋Redis
    * 爬取更多网站的内容，增加“感兴趣的话题”
    * 配置gevent

## 项目介绍

***

> 后段采用Django，前端采用Materialize；
功能主要分为两部分：blog和spider；
blog即为发布和浏览博文的功能，
spider为定向爬取指定网站指定内容的爬虫（目前为[蚂蜂窝](http://www.mafengwo.cn)）；


### 相关笔记

#### Model
***
##### 模型框图：
![Model](https://raw.githubusercontent.com/PU-101/pics/master/sansanxin-model-2.png)
> 注：空箭头：1、黑圆点：多

关系结构由单独的Like、Comment和Follow表来存储，保持User、UserProfile和Post表的纯净。并且所有的多对多关系均通过多对一来表示，构造表的时候也较为方便。

##### Signals

表之间许多相互影响的字段通过Signals来进行及时自动修改,主要有如下几种情况：
* 创建User对象的时候自动创建相应一对一的UserProfile对象；
* 创建或删除Like、Comment、Follow对象的时候，自动修改相应的Post或UserProfile对象中存储数量的字段的值；
这样做，保证了view的干净，并且配置好后，即可放心使用。

##### Mangers

自定义manger及相应的自定义获取queryset方法，保证自定义的查询集可以链接使用，参考自[建立一个更高级别的查询 API：正确使用Django ORM 的方式](http://www.oschina.net/translate/higher-level-query-api-django-orm)


#### Registration
***
用户登录注册等功能使用的是Django-Registartion-redux

#### 爬虫
***
##### 爬虫架构框图：
![架构框图](https://raw.githubusercontent.com/PU-101/pics/master/%E7%88%AC%E8%99%AB.png)

##### URL管理器：
![URL管理器](https://raw.githubusercontent.com/PU-101/pics/master/URL%E7%AE%A1%E7%90%86%E5%99%A8.PNG)

配置new_urls和old_urls两个set，将爬取的页面中的URL添加到new_urls中，从new_urls中取出URL爬取并解析，并存放到old_urls集中去；

爬虫的解析采用的是lxml库

#### 异步任务
***
> 通过celery+redis的配置构建异步任务框架。

目前异步任务的功能用于实现定时启动爬虫，更新数据。后续可能会添加消息推送功能

#### 国际化
目前部分页面（登录、注册）保留了原英文内容，并做了相应的翻译，具体在settings和locale中修改
