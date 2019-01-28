// $(function() {
//   $('.bt_register').click(function() {
//     $.ajax({
//         url : '/user/register',
//         type : 'POST',
//         data : $('form').serialize(),         //序列化表单输入，选择内容
//         headers:{
//                 "X-CSRF-Token": getCookie('csrf_token')
//             },
//         success : function (resp) {
//             alert(resp);
//         }
//     });
//   });
// });
//

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
    })
})
