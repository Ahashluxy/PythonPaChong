前戏：
    1.你是否在夜深人静的时候，想看一些会让你更睡不着的图片却苦于没有资源...
    2.你是否在节假日出行高峰的时候，想快速抢购火车票成功...
    3.你是否在网上购物的时候，想快速且精准的定位到口碑质量最好的商品...

什么是爬虫：
    - 通过编写程序，模拟浏览器上网，然后让其去互联网上抓取数据的过程。


爬虫的价值：
    - 实际应用
    - 就业

爬虫究竟是合法还是违法的？
- 在法律中是不被禁止
- 具有违法风险
- 善意爬虫  恶意爬虫

爬虫带来的风险可以体现在如下2方面：
    - 爬虫干扰了被访问网站的正常运营
    - 爬虫抓取了收到法律保护的特定类型的数据或信息

如何在使用编写爬虫的过程中避免进入局子的厄运呢？
    - 时常的优化自己的程序，避免干扰被访问网站的正常运行
    - 在使用，传播爬取到的数据时，审查抓取到的内容，如果发现了涉及到用户隐私
    商业机密等敏感内容需要及时停止爬取或传播


爬虫在使用场景中的分类
    - 通用爬虫：
        抓取系统重要组成部分。抓取的是一整张页面数据。
    - 聚焦爬虫：
        是建立在通用爬虫的基础之上。抓取的是页面中特定的局部内容。
    - 增量式爬虫：
        检测网站中数据更新的情况。只会抓取网站中最新更新出来的数据。

爬虫的矛与盾


反爬机制
    门户网站，可以通过制定相应的策略或者技术手段，防止爬虫程序进行网站数据的爬取。

反反爬策略
    爬虫程序可以通过制定相关的策略或者技术手段，破解门户网站中具备的反爬机制，从而可以获取门户网站中相关的数据。


robots.txt协议：
    君子协议。规定了网站中哪些数据可以被爬虫爬取哪些数据不可以被爬取。



http协议
    - 概念：就是服务器和客户端进行数据交互的一种形式。
常用请求头信息
    - User-Agent：请求载体的身份标识
    - Connection：请求完毕后，是断开连接还是保持连接

常用响应头信息
    - Content-Type：服务器响应回客户端的数据类型

https协议：
    - 安全的超文本传输协议

加密方式
    - 对称秘钥加密
    - 非对称秘钥加密
    - 证书秘钥加密

requests模块
    - urllib模块
    - requests模块

requests模块：python中原生的一款基于网络请求的模块，功能非常强大，简单便捷，效率极高。
作用：模拟浏览器发请求。

如何使用：（requests模块的编码流程）
    - 指定url
        - UA伪装
        - 请求参数的处理
    - 发起请求
    - 获取响应数据
    - 持久化存储

环境安装：
    pip install requests

实战编码：
    - 需求：爬取搜狗首页的页面数据



实战巩固
    - 需求：爬取搜狗指定词条对应的搜索结果页面（简易网页采集器）
        - UA检测
        - UA伪装
    - 需求：破解百度翻译
        - post请求（携带了参数）
        - 响应数据是一组json数据
    - 需求：爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详情数据

    - 作业：爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数据

    - 需求：爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据
                http://125.35.6.84:81/xk/
        - 动态加载数据
        - 首页中对应的企业信息数据是通过ajax动态请求到的。

        http://125.35.6.84:81/xk/itownet/portal/dzpz.jsp?id=e6c1aa332b274282b04659a6ea30430a
        http://125.35.6.84:81/xk/itownet/portal/dzpz.jsp?id=f63f61fe04684c46a016a45eac8754fe
        - 通过对详情页url的观察发现：
            - url的域名都是一样的，只有携带的参数（id）不一样
            - id值可以从首页对应的ajax请求到的json串中获取
            - 域名和id值拼接处一个完整的企业对应的详情页的url
        - 详情页的企业详情数据也是动态加载出来的
            - http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById
            - http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById
            - 观察后发现：
                - 所有的post请求的url都是一样的，只有参数id值是不同。
                - 如果我们可以批量获取多家企业的id后，就可以将id和url形成一个完整的详情页对应详情数据的ajax请求的url

数据解析：
    聚焦爬虫
    正则
    bs4
    xpath
 聚焦爬虫:爬取页面中指定的页面内容。
    - 编码流程：
        - 指定url
        - 发起请求
        - 获取响应数据
        - 数据解析
        - 持久化存储

数据解析分类：
    - 正则
    - bs4
    - xpath（***）

数据解析原理概述：
    - 解析的局部的文本内容都会在标签之间或者标签对应的属性中进行存储
    - 1.进行指定标签的定位
    - 2.标签或者标签对应的属性中存储的数据值进行提取（解析）

正则解析：

<div class="thumb">

<a href="/article/121721100" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12172/121721100/medium/DNXDX9TZ8SDU6OK2.jpg" alt="指引我有前进的方向">
</a>

</div>

ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'


bs4进行数据解析
    - 数据解析的原理：
        - 1.标签定位
        - 2.提取标签、标签属性中存储的数据值
    - bs4数据解析的原理：
        - 1.实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
        - 2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
    - 环境安装：
        - pip install bs4
        - pip install lxml
    - 如何实例化BeautifulSoup对象：
        - from bs4 import BeautifulSoup
        - 对象的实例化：
            - 1.将本地的html文档中的数据加载到该对象中
                    fp = open('./test.html','r',encoding='utf-8')
                    soup = BeautifulSoup(fp,'lxml')
            - 2.将互联网上获取的页面源码加载到该对象中
                    page_text = response.text
                    soup = BeatifulSoup(page_text,'lxml')
        - 提供的用于数据解析的方法和属性：
            - soup.tagName:返回的是文档中第一次出现的tagName对应的标签
            - soup.find():
                - find('tagName'):等同于soup.div
                - 属性定位：
                    -soup.find('div',class_/id/attr='song')
            - soup.find_all('tagName'):返回符合要求的所有标签（列表）
        - select：
            - select('某种选择器（id，class，标签...选择器）'),返回的是一个列表。
            - 层级选择器：
                - soup.select('.tang > ul > li > a')：>表示的是一个层级
                - oup.select('.tang > ul a')：空格表示的多个层级
        - 获取标签之间的文本数据：
            - soup.a.text/string/get_text()
            - text/get_text():可以获取某一个标签中所有的文本内容
            - string：只可以获取该标签下面直系的文本内容
        - 获取标签中属性值：
            - soup.a['href']

xpath解析：最常用且最便捷高效的一种解析方式。通用性。

    - xpath解析原理：
        - 1.实例化一个etree的对象，且需要将被解析的页面源码数据加载到该对象中。
        - 2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获。
    - 环境的安装：
        - pip install lxml
    - 如何实例化一个etree对象:from lxml import etree
        - 1.将本地的html文档中的源码数据加载到etree对象中：
            etree.parse(filePath)
        - 2.可以将从互联网上获取的源码数据加载到该对象中
            etree.HTML('page_text')
        - xpath('xpath表达式')
    - xpath表达式:
        - /:表示的是从根节点开始定位。表示的是一个层级。
        - //:表示的是多个层级。可以表示从任意位置开始定位。
        - 属性定位：//div[@class='song'] tag[@attrName="attrValue"]
        - 索引定位：//div[@class="song"]/p[3] 索引是从1开始的。
        - 取文本：
            - /text() 获取的是标签中直系的文本内容
            - //text() 标签中非直系的文本内容（所有的文本内容）
        - 取属性：
            /@attrName     ==>img/src


作业：
    爬取站长素材中免费简历模板


        ，






