$(function () {
    $("#regist").submit(function (e) {
        e.preventDefault();
        $.ajax({
            url:"/user/register",
            type:"POST",
            data: $('#regist').serialize(),
            success:function (resp) {
                alert(resp)
            }
        })
    });

    // 注册按钮点击事件
    $(".register_btn").click(function () {
        if($(".box-2").css("display") == "none"){
				$(".box-2").show();
			}else{
				$(".box-2").hide();
			}
    });

    // 登录按钮点击事件
    $(".login_btn").click(function () {
        if($(".box-1").css("display") == "none"){
				$(".box-1").show();
			}else{
				$(".box-1").hide();
			}
    });

});
