$(function () {

    // 注册事件
    $("#regist").submit(function (e) {
        e.preventDefault();
        $.ajax({
            url: "/user/register",
            type: "POST",
            data: $('#regist').serialize(),
            success: function (resp) {
                alert(resp)
            }
        })
    });

    // 登录事件
    $("#login").submit(function (e) {
        e.preventDefault();
        $.ajax({
            url: "/user/login",
            type: "POST",
            data: $('#login').serialize(),
            success: function (resp) {
                alert(resp)
            }
        })

    });


    // 注册按钮点击事件
    $(".register_btn").click(function () {
        if ($(".box-2").css("display") == "none") {
            if ($(".box-1").css("display") !== "none") {
                $(".box-1").hide();
            }
            $(".box-2").show();
        } else {
            $(".box-2").hide();
        }
    });

    // 登录按钮点击事件
    $(".login_btn").click(function () {
        if ($(".box-1").css("display") == "none") {
            if ($(".box-2").css("display") !== "none") {
                $(".box-2").hide();
            }
            $(".box-1").show();
        } else {
            $(".box-1").hide();
        }
    });

});
