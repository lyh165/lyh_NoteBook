1.安装requests 库(基本使用 https://www.cnblogs.com/lei0213/p/6957508.html)
	pip install requests

2.安装BeautifulSoup 库(https://cuiqingcai.com/1319.html)	类似于正则、lxml
	pip install 安装BeautifulSoup

3. 知乎抓包工具出现了一点问题
	知乎的网站已经改了一部分，没有那么好抓

4.编码模块 （chardet）	

5、糗事百科
	页面变化
	https://www.qiushibaike.com/8hr/page/1/
	https://www.qiushibaike.com/8hr/page/2/
	https://www.qiushibaike.com/8hr/page/3/
	模糊查询
	//div[contains(@id,"qiushi_tag")]
	用户名
	//div[contains(@id,"qiushi_tag")]//div/a/h2
	段子
	//div[contains(@id,"qiushi_tag")].//div[@class="content"]/span
	赞、评价、
	...

	6、CPU、进程、线程、锁、队列
		CPU 是计算机一个 计算一个基本单位，用来执行任务的
		CPU包含多个进程
		一个进程包含多个线程
		线程执行任务 包含一个锁，用来控制执行任务的 ，称之为阻塞
		父线程、子线程（父线程结束，不管子线程在干什么，都要结束）
		队列，相当于 内存里面的"堆"一样 先进先出
		栈 相当于 喝酒一样 先喝再吐 吐之前是把最后的先吐 后进先出

		队列加入参数、
		爬数据、存数据是属于IO(线程处理)

	7、计算机的核心是CPU，CPU承担了所有的计算任务
		一个cpu核心一次只能执行一个任务
		将

		一个CPU一次只能执行一个进程，其他进程处于非运行状态。
		进程里包含的执行单元叫线程。
		一个进程 可以包含 多个线程。

		一个进程的内存空间是共享的，每个进程里面的线程都是可以使用这个共享空间。
		一个线程在使用这个共享的时候，其他线程必须等他结束。

		通过“锁”实现，作用就是防止多个现场使用这块内存空间。
		先试用的线程空间上锁，其他现场就在门口等待，打开锁再进来。

进程：表示程序的一次执行
线程：cpu运算的基本调度单位
GIL：python里的执行通行证：而且只有一个，拿到通行证的线程就可以进入cpu执行任务。
	没有就干瞪眼。
python的多线程 适用于：大量密集的I/O处理
Python的多进程：大量的密集并行计算。

scrapy

9.selenium、phantomJS(无界面的浏览器)

10.Tesseract 的安装
	

