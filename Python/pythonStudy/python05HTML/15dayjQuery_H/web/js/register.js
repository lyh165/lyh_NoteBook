// $(function(){

// 	var error_name = false;
// 	var error_password = false;
// 	var error_check_password = false;
// 	var error_email = false;
// 	var error_check = false;


// 	$('#user_name').blur(function() {
// 		check_user_name();
// 	});

// 	$('#user_name').focus(function() {
// 		$(this).next().hide();
// 	});


// 	$('#pwd').blur(function() {
// 		check_pwd();
// 	});

// 	$('#pwd').focus(function() {
// 		$(this).next().hide();
// 	});

// 	$('#cpwd').blur(function() {
// 		check_cpwd();
// 	});

// 	$('#cpwd').focus(function() {
// 		$(this).next().hide();
// 	});

// 	$('#email').blur(function() {
// 		check_email();
// 	});

// 	$('#email').focus(function() {
// 		$(this).next().hide();
// 	});

// 	$('#allow').click(function() {
// 		if($(this).is(':checked'))
// 		{
// 			error_check = false;
// 			$(this).siblings('span').hide();
// 		}
// 		else
// 		{
// 			error_check = true;
// 			$(this).siblings('span').html('请勾选同意');
// 			$(this).siblings('span').show();
// 		}
// 	});


// 	function check_user_name(){
// 		//数字字母或下划线
// 		var reg = /^[a-zA-Z0-9_]{5,15}$/;
// 		var val = $('#user_name').val();

// 		if(val==''){
// 			$('#user_name').next().html('用户名不能为空！')
// 			$('#user_name').next().show();
// 			error_name = true;
// 			return;
// 		}

// 		if(reg.test(val))
// 		{
// 			$('#user_name').next().hide();
// 			error_name = false;
// 		}
// 		else
// 		{
// 			$('#user_name').next().html('用户名是5到15个英文或数字，还可包含“_”')
// 			$('#user_name').next().show();
// 			error_name = true;
// 		}

// 	}


// 	function check_pwd(){
// 		var reg = /^[\@A-Za-z0-9\!\#\$\%\^\&\*\.\~]{6,22}$/;
// 		var val = $('#pwd').val();

// 		if(val==''){
// 			$('#pwd').next().html('密码不能为空！')
// 			$('#pwd').next().show();
// 			error_password = true;
// 			return;
// 		}

// 		if(reg.test(val))
// 		{
// 			$('#pwd').next().hide();
// 			error_password = false;
// 		}
// 		else
// 		{
// 			$('#pwd').next().html('密码是6到15位字母、数字，还可包含@!#$%^&*.~字符')
// 			$('#pwd').next().show();
// 			error_password = true;
// 		}		
// 	}


// 	function check_cpwd(){
// 		var pass = $('#pwd').val();
// 		var cpass = $('#cpwd').val();

// 		if(pass!=cpass)
// 		{
// 			$('#cpwd').next().html('两次输入的密码不一致')
// 			$('#cpwd').next().show();
// 			error_check_password = true;
// 		}
// 		else
// 		{
// 			$('#cpwd').next().hide();
// 			error_check_password = false;
// 		}		
		
// 	}

// 	function check_email(){
// 		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
// 		var val = $('#email').val();

// 		if(val==''){
// 			$('#email').next().html('邮箱不能为空！')
// 			$('#email').next().show();
// 			error_email = true;
// 			return;
// 		}

// 		if(re.test(val))
// 		{
// 			$('#email').next().hide();
// 			error_email = false;
// 		}
// 		else
// 		{
// 			$('#email').next().html('你输入的邮箱格式不正确')
// 			$('#email').next().show();
// 			error_email = true;
// 		}

// 	}


// 	$('.reg_form').submit(function() {

// 		check_user_name();
// 		check_pwd();
// 		check_cpwd();
// 		check_email();

// 		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
// 		{
// 			return true;
// 		}
// 		else
// 		{
// 			return false;
// 		}

// 	});

// })

// -------- 

$(function(){

// 定义几个变量用来代表最后用来提交表单的
	var error_name = false;
	var error_pwd = false;
	var error_cpwd = false;
	var error_email = false;
	var error_allow = false;

// 绑定事件
// blur 失去焦点的时候
	$('#user_name').blur(function(){
		check_username();
	});
// focus
// 获取当前焦点的时候 把提示信息隐藏起来	
	$('#user_name').focus(function(){
		$(this).next().hide();
	});

// 密码
	$('#pwd').blur(function(){
		check_pwd();
	});
	$('#pwd').focus(function(){
		$(this).next().hide();
	});
// 确认密码
	$('#cpwd').blur(function(){
		check_cpwd();
	});
	$('#cpwd').focus(function(){
		$(this).next().hide();
	});
// 邮箱
	$('#email').blur(function(){
		check_email();
	});
	$('#email').focus(function(){
		$(this).next().hide();
	});

// 协议	
	$('#allow').click(function(){
		if ($(this).prop('checked')==true) {
			 error_allow = false;
			 $('.error_tip2').hide();
		}
		else
		{
			error_allow = true;
		 	$('.error_tip2').html('请勾选同意！').show();

		}
	});


	function check_username(){

		var val = $('#user_name').val();
		// i 是忽略大小写
		var re = /^\w{5,15}$/i;
		if(val ==''){
			$('#user_name').next().html('用户名不能为空！');
			$('#user_name').next().show();
			error_name = true; // 有错误
			return;
		}
		
		if(re.test(val)){
			error_name = false;
		}
		else{
			error_name = true; // 有错误
			$('#user_name').next().html('用户名是包含数字、字母、下划线的5到15位字符');
			$('#user_name').next().show();
		}


	}



	function check_pwd(){

		var val = $('#pwd').val();
		var re = /^[a-zA-Z0-9@\$\*\.\!\?]{6,16}$/; // \$ 是将它转移成字符$
		if(val ==''){
			$('#pwd').next().html('密码不能为空！');
			$('#pwd').next().show();
			error_pwd = true; // 有错误
			return;
		}
		
		if(re.test(val)){
			 error_pwd = false;
		}
		else{
			error_pwd = true; // 有错误
			$('#pwd').next().html('密码是包含数字、字母、还包含@$*.!?的6-16位字符');
			$('#pwd').next().show();
		}
	}

	function check_cpwd(){
		var val = $('#pwd').val();
		var cval = $('#cpwd').val();

		if (val==cval) {
			 error_cpwd = false;

		}
		else
		{
			 error_cpwd = true;
			$('#cpwd').next().html('两次输入的密码不一致');
			$('#cpwd').next().show();

		}


	}
	function check_email(){

		var val = $('#email').val();
		// var re = /^[a-zA-Z0-9][\w\.]*@[\w]+(\.[\w]{2,3}){2,3}$/; // *是多个 (...)是一个范围
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(val ==''){
			$('#email').next().html('邮箱不能为空！');
			$('#email').next().show();
			error_email = true; // 有错误
			return;
		}
		
		if(re.test(val)){
			 error_email = false;
		}
		else{
			error_email = true; // 有错误
			$('#email').next().html('邮箱是包含数字、字母、包含. 例如wy@.163.com,tx@@qq.com,name@165.cn');
			$('#email').next().show();
		}
	}


	$('.reg_form').submit(function(){
		check_username();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name == false && 
			error_pwd == false &&
			 error_cpwd == false &&
			 error_email == false &&
			 error_allow == false){
			// 全部正确才能提交
			return true;
		}
		else
		{
			// 不正确 不能提交
			return false;
		}

	})


})