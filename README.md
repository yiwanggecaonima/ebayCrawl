# ebayCrawl

闲的蛋疼写的ebay crawl,用一下CrawlSpider来获取页面上的link,这里写的有一些潦草，可以根据想要获取的link改动下面的parse方法．
一大堆UA请求头和代理ip就不必说了，如果自己想弄一个代理池ip也可以，我这里是直接用崔大的代理池（有一些代理获取不到，可能是因为时间久了，解析路径发生了改变，或者种种原因，如果有雅致，可以试着弄一个，最简单的就是对接flask啦,有接口即可）

分布式采用的事scrapy_redis这个库，这个是现在算是比较主流的一个分布式架构了，scrapy对接redis.
存储用的是mongodb,也可以直接存在redis,但是想到redis是基于内存的．．．．这里数据的关联性不大，所以就不把mysql搬出来了．

贴出邮箱：wutong8773@163.com  欢迎交流讨论


