/**
 * Created by wo on 2018/10/24.
 */

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(function(){

    $("#form_action").submit(function (e) {
        e.preventDefault();

        $.ajax({
            url:"/admin/login",
            type:'POST',
            data: $("#form_action").serialize(),
            headers:{
                "X-CSRF-Token": getCookie('csrf_token')
            },
            success:function (resp) {

                if(resp.error==200){
                    window.location.href = "/admin/page";
                }else{
                    $(".span_msg").css("background", "white");
                    $(".span_msg").css("color", "black");
                    $('.span_msg').text(resp.errmsg);
                }
            }
        })
    });
});