$(function () {

    // 注册事件
    $("#regist").submit(function (e) {
        e.preventDefault();
        $.ajax({
            url: "/user/register",
            type: "POST",
            data: $('#regist').serialize(),
            // headers: {
            //     "X-CSRFToken": getCookie("csrf_token")
            // },
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
            // headers: {
            //     "X-CSRFToken": getCookie("csrf_token")
            // },
            success: function (resp) {
                if (resp.errno == "200") {
                    alert(resp)
                }
                location.reload();

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

    // 登出
    $(".logout").click(function () {
        $.ajax({
            url: "/user/logout",
            type: "get",
            // headers: {
            //     "X-CSRFToken": getCookie("csrf_token")
            // },
            success: function (resp) {
                location.reload()
            }
        });
        alert('登出成功')
    })

});
