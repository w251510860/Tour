$(function () {
    // 打开登录框
    $('.login_btn').click(function () {
        $('.regist').hide();
        $('.login').show();
    });

    // 打开注册框
    $('.register_btn').click(function () {
        $('.login').hide();
        $('.regist').show();
    });

    // 切换注册框
    $('.to_regist').click(function () {
        $('.login').hide();
        $('.regist').show();
    });

    // 注册表单提交
    $(".regist").submit(function (e) {
        e.preventDefault();
        var username = $("#username").val();
        var password = $("#password").val();
        var re_password = $("#re-password").val();
        var phone_num = $("#telephone-number").val();
        if (!username){
            alert('请输入用户名');
            return;
        }
        if (!password){
            alert('请输入密码');
            return;
        }
        if (password !== re_password){
            alert('两次密码不一致');
            return;
        }
        if (!phone_num){
            alert('请输入手机号');
            return;
        }
        var params = {
            "username": username,
            "password": password,
            "phone_num": phone_num,
        };

        $.ajax({
            url: "/passport/register",
            type: "POST",
            data: JSON.stringify(params),
            contentType: "application/json",
            // headers:{'X-CSRFToken':getCookie('csrf_token')},
            dataType: "json",
            success: function (resp) {
                if (resp.errno == "0"){
                    location.reload();
                } else{
                    alert(resp.errmsg)
                }
            }
        })
    });

    // 登陆表单提交
    $(".login").submit(function (e) {
        var phone_num = $("#login-telephone-number").val();
        var password = $("#login-password").val();
        if (!phone_num){
            alert('请输入手机号')
        }
        if (!password){
            alert('请输入密码')
        }
        var params = {
            "password": password,
            "phone_num": phone_num,
        }
        $.ajax({
            url: '/passport/login',
            type: 'POST',
            data: JSON.stringify(params),
            contentType: "application/json",
            dataType: "json",
            // headers:{'X-CSRFToken':getCookie('csrf_token')},
            success: function (resp) {
                if (resp.errno == "0"){
                    location.reload();
                } else{
                    alert(resp.errmsg)
                }
            }
        })
    })
});

function logout() {
    $.ajax({
        url: "/passport/logout",
        type: "post",
        contentType: "application/json",
        // headers: {'X-CSRFToken': getCookie('csrf_token')},
        success: function (resp) {
            location.reload()
        }
    })
}