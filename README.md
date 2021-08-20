# MangaSpider-
从湾湾网站爬取中文漫画并自动分章节保存本地
<br>
<br>
根目录需要下载<em>phantomjS.exe</em>
<a href="https://mirrors.huaweicloud.com/phantomjs/phantomjs-1.9.6-linux-i686-symbols.tar.bz2">下载</a>
<br>
<br>
<p>基于PhantomJs和Selnium的爬虫（python 3.x）</p>

<p>依赖的python包请查看requirements.txt，pycharm可直接虚拟环境读取</p>

<p>mangabz_spider.config文件用来更改配置</p>

<p>
  <b>如何配置mangabz_spider.config:</b>
</p>
<h4>示例</h4>
<!-- ----------------------mangabz_spider.conf--------------------------------- -->
<hr>
<p>name = 租借女友                             <em style:"color: gray"><- 漫画名称 可以随便起但起了就不能改了 一个名字只能对应一个url</em></p>
<p>url = http://www.mangabz.com/279bz/         <em style:"color: gray"><- 漫画主页(http://www.mangabz.com )的网址 只能爬取这个网站的漫画</em> </p>
<p>root_path = D:\\Comics\\                    <em style:"color: gray"><- 保存的本地地址（双斜杠），请最好使用英文地址，防止bug</em></p>
<hr>
<!-- --------------------------------------------------------------------------- -->

<p>2. 配置完毕后启动update_src.bat，进度条就是解析的src</p>
<p>3. 启动download_image.bat，下载解析过得src，就是直接下载漫画图片</p>
<p>4. 步骤‘2’和‘3’目前不能同时进行，可能会引发一些bug。请单独启动update_src.bat及download_image.bat。</p>
