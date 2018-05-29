通过规律 找出div的上一级 上一级 然后找到所要的元素下的表情内容进行匹配
//div[@class="threadlist_lz clearfix"]//a[@class="j_th_tit"]/@href

//取出帖子里的每个图片的链接
//img[@class="BDE_Image"]/@src

安装 lxml


最终目的是获取a标签下的 跳转/p/5006374769

<div class="threadlist_lz clearfix">
<div class="threadlist_title pull_left j_th_tit 
">
    <i class="icon-member-top" alt="会员置顶" title="会员置顶"></i><i class="icon-good" alt="精品" title="精品"></i>
    <a rel="noreferrer" href="/p/5006374769" title="【答疑解惑】误删误封绿色通道" target="_blank" class="j_th_tit ">【答疑解惑】误删误封绿色通道</a>
</div>

--------------
<div class="threadlist_lz clearfix">
<div class="threadlist_title pull_left j_th_tit ">
    <a rel="noreferrer" href="/p/5703716074" title="找个能疼我得大叔" target="_blank" class="j_th_tit ">找个能疼我得大叔</a>
</div>