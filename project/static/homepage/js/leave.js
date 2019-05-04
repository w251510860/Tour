$(function () {
    $(".comment_submit").submit(function (e) {
        var name = $("#txtUserName").val();
        var phone = $("#txtUserTel").val();
        var sex = $('input[name="txtUserQQ"]:checked').val();
        var txt = $("#txtContent").val();
        alert(name, phone, sex, txt);
    })
});