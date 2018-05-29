(function(){
	var calc = function(){
		var docElement = document.documentElement; //获取一个html文档
		// 三目运算符 简写
		// 如果屏幕大于 > 750 就按照750 否则就等于下面的
		// docElement.style.fontSize = 20*(clientWidthValue/375) + 'px';
		// 然后用当前屏幕的宽度做一个基准 / 375 再乘以一个20 然后赋值给html的fontsize
		// 这就是动态改变fontsize的值
		var clientWidthValue = docElement.clientWidth > 750 ? 750 : docElement.clientWidth;
		docElement.style.fontSize = 20*(clientWidthValue/375) + 'px';
	}
	calc();
	window.addEventListener('resize',calc);
})();