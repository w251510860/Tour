$(document).ready(function () {
    var username = $("#username").val();
    var password = $("#password").val();
    var re_password = $("#re-password").val();
    var telephone_number = $("#telephone-number").val();
    var email = $("#e-mail").val();


    $("#regist").submit(function (e) {

        // $("#regist").preventDefault(function (e) {
        //     check_password(password, re_password)
        // });
        alert("密码为",username, password, re_password, telephone_number, email);

        // $.ajax({
        //     url: "/greet",
        //     data: {
        //         "username": username,
        //         "password": password,
        //         "telephone_number": telephone_number,
        //         "email": email,
        //     },
        //     type: "POST",
        //     dataType: "json",
        //     success: function (data) {
        //         alert('发送成功')
        //     }
        // });

    });

    function check_password(password, re_password) {
        if (password != re_password) {
            alert('两次密码不一致')
        }

    }
});