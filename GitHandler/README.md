# GitHandler
Git 的操作

1.Git是什么?
	Git是一个版本控制工具。
		什么是版本控制工具。
			比如我开发了一款微信APP(1.0版本)。
			我再开发微信APP(1.1版本)，那么我怎么操作呢。在原来的版本基础上继续操作。这样会存在一个隐患的问题。如果我中途不小心删除了文件。导致1.1版本的问题，解决不了，此时我怎么去处理。我恢复不了1.0版本的信息。坐着等开出吧。
		此时横空出现一个版本控制工具。Git
		Git能管理你所有版本的信息。如果想反悔，只需要反悔到那个版本即可。
		这就是版本控制工具。

2.Git是怎么操作流程的	?
	Git其实是分为一个远程仓库、本地仓库
		远程仓库是什么？
			比如你在本地仓库做了一件事情。提交到远程仓库。远程仓库就知道你做了这一件事情。
		本地仓库是什么？
			本地仓库就是 你在做任何事情。都跟你本人相关。跟其他人无关。无人知晓，非常你做的事情提交到远程仓库。	

3.git的分支？
	Git分支是什么？
		Git分为一个主分支，叫master。所有人最终提交的东西都会存储到这里。
		Git的其他分支叫branch。是由本地仓库从远程仓库clone回来之后。默认存储在master分支。
			你想，如果你在master分支进行操作。是不是很危险，如果稍微错误一点点。会导致整个项目崩溃。
			所以还是乖乖，拿到一份备份，也就是创建分支，在里面进行操作。当调试测试完毕之后，才去合并到master分支里面。保证万无一失。



5、git的区域
	Git本地仓库分为几个区域
		工作区、暂存区、本地代码库
	默认是操作的时候在 工作区
	提交操作
		git add filename 把工作区的文件 提交到 暂存区
			git add hello.py
		git commit -m "说明此处操作是干什么的" 把暂存区 提交到 本地代码库
			git commit hello.py
	回退操作
		git	reset HEAD filename 
			git	reset HEAD hello.py 

4.git的命令

	4.1、git clone xxxx (从远程仓库拷贝一份代码到本地仓库)
			git clone https://github.com/lyh165/test.git
	4.2、git status  (查看本地仓库的状态)
分支	
	4.3、git branch xxx  (创建分支)
			git branch kdh
	4.4、git branch -d xxx 	(删除分支)
			git branch -d kdh
	4.5、git checkout 分支名 (切换分支)
	4.6 git checkout -b 分支名 (新建并切换分支)		
提交
	4.7 git add 提交到暂存区
	4.8 git commit 提交到本地代码库(记得加 -m "注释")
	4.9 git push origin 本地分支: 远程分支
	3.10 git merge合并
	3.11 git pull origin 远程分支
打tag 版本
	3.12 git tag -a v0.1 -m "0.1版本"
	3.13 git tag 	(查看版本)
	3.14 git push origin kdh:kdh --tags (推送版本)


	git push origin kdh:kdh(前面的kdh代表本地分支,后面的kdh代表远程分支)
推送提交到远程仓库	


如果提交过一次代码
每次执行 都需要 git pull orign master，拉取一下代码，保证本地代码是最新的




