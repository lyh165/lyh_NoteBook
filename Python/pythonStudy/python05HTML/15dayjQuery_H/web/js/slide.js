$(function(){
	

	var $li = $('.slide_pics li');
	var len = $li.length;
	// 获取左右按钮
	var $prev = $('.prev');
	var $next = $('.next');

	// 将要运动过来的li
	var nowli = 0;
	// 当前要离开的li
	var prevli = 0;
	// 定时器 用来自定播放的
	var timer = null;



	$li.not(':first').css({left:760}); // 设置其他的图片偏移760
// 动态创建点
// each 执行多次
	$li.each(function(index){
		var $sli = $('<li>');
		if(index==0){
			$sli.addClass('active');
		}
		$sli.appendTo('.points');

	})
	$points = $('.points li');
// 点击 点的事件	
	$points.click(function(){
		nowli = $(this).index();
		if (nowli == prevli) {
			return;
		}
		move();
		$(this).addClass('active').siblings().removeClass('active');
	});

// 左右按钮的事件
	
	$prev.click(function(){
		nowli--;
		move();
		// 控制点
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	})


	$next.click(function(){
		nowli++;
		move();
		// 控制点
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	});

// 停止播放
	$('.slide').mouseenter(function(){
		clearInterval(timer);
	});

	// 离开子元素之后 继续播放
	$('.slide').mouseleave(function(){
		timer = setInterval(autoplay,4000);
	});
// 自动播放
	timer = setInterval(autoplay,4000);

	function autoplay(){
		nowli++;
		move();
		// 控制点
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	}

	function move(){

		// 处理左边为空的情况
		if(nowli<0){
			nowli = len - 1;
			prevli = 0;

			$li.eq(nowli).css({left:-760});
			$li.eq(prevli).stop().animate({left:760});
			$li.eq(nowli).stop().animate({left:0});
			prevli = nowli;
			return;
		}

		if(nowli>len-1)
		{
			nowli = 0;
			prevli = len-1;

			$li.eq(nowli).css({left:760});
			$li.eq(prevli).stop().animate({left:-760});
			$li.eq(nowli).stop().animate({left:0});
			prevli = nowli;
		}




		if (nowli > prevli){
			$li.eq(nowli).css({left:760});
			$li.eq(prevli).stop().animate({left:-760});
			
		}
		else{
			$li.eq(nowli).css({left:-760});
			$li.eq(prevli).stop().animate({left:760});
		}

		$li.eq(nowli).stop().animate({left:0});
			prevli = nowli;
	};



})