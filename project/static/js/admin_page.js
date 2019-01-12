$(function(){
  var wh = $(window).height();

  var index = 1;
  active_tab(index);
  var back_url = $(".wrapper").attr("data-back");

  $("body").css("background-image", "url("+back_url+")");
  var con = $(".tab_li").text();


  $(".form_alter_pic").submit(function(e){
    e.preventDefault();

    $(this).ajaxSubmit({
      url: "/admin/alter_pic/",
      type: "POST",
      headers: {"X-CSRF-Token": getCookie('csrf_token')},
      success: function(resp){
        $(".alter_window").hide();
        $("#user_pic").attr("src", resp.data.pic_url);
      }
    });
  });

  $(".info_form").submit(function(e){
    e.preventDefault();

    $(this).ajaxSubmit({
      url: "/admin/alter_user_info/",
      type: "POST",
      headers: {"X-CSRF-Token": getCookie('csrf_token')},
      success: function(resp){
        alert(resp.errmsg);
        $(".alter_info_window").hide();

        $(".user_sign").text(resp.data.user.private_sign);
        $(".user_nick").text(resp.data.user.nick_name);
        if(resp.data.user.sex == "man"){
          $("input[name='sex']").get(0).checked = true;
        }else{
          $("input[name='sex']").get(1).checked = true;
        }
        // $(".user_sex").text(resp.data.user.sex);
        if(resp.data.user.pic_url == null || resp.data.user.pic_url == ""){
          resp.data.user.pic_url = "../static/picture/admin_index.jpg"
        }
        $("#user_pic").attr("src", resp.data.user.pic_url);
        $(".user_phone").text(resp.data.user.phone_num);
        $(".user_live").text(resp.data.user.user_live);
        $(".user_last").text(resp.data.user.last_login);
        $(".btn_op").attr("alter_info", resp.data.user.id);
        $("input[name='i']").val(resp.data.user.id);
      }
    });
  });

  // $("#table_info").DataTable();
});

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function remove_back(index) {
    $('#'+index).addClass('show_background');
    $('#'+index).siblings().removeClass('show_background');
}
// 切换tab
function active_tab(index){
  if(index == 1){
    var user_id = $(".wrapper").attr("data-id");
    get_admin_info(user_id);
    remove_back(index);
    $('.box').show();
    $('.box').siblings().hide();
  }
  if(index == 2){
    remove_back(index);
    $('.travel_box').show();
    $('.travel_box').siblings().hide();
  }
  if(index == 3){
    remove_back(index);
    $('.travel_blog').show();
    $('.travel_blog').siblings().hide();
  }
  if(index == 4){
    remove_back(index);
  }
  if(index == 5){
    remove_back(index);
  }
  if(index == 9){
    logout();
  }
}

function get_admin_info(admin_id){
  $.get("/admin/get_admin_info", {admin_id: admin_id}, function(resp){
    if(resp.error == 200){
      $(".td_name").text(resp.data.admin.nick_name);
      if(resp.data.admin.pic_url==null){
        resp.data.admin.pic_url = "../static/picture/admin_index.jpg";
      }
      $(".img_pic").attr("src", resp.data.admin.pic_url);
      $(".td_phone").text(resp.data.admin.phone_num);
      $(".td_last").text(resp.data.admin.last_login);
    }else{
      alert(resp.errmsg);
    }
  });
}

function logout(){
  $.get("/admin/logout", function(resp){
      if(resp.error){
        alert(resp.errmsg);
      }else{
        window.location.reload();
      }
  })
}

function show_person(){
  $(".tb_name").fadeIn();
  $(".users_list").fadeOut();
  $("#tb_user").hide();
}

function show_users(){
  $(".users_list").fadeIn();
  $(".tb_name").fadeOut();
}

function get_user_info(id){
  $.get("/admin/get_user_info", {
    "user_id": id
  }, function(resp){
    if(resp.error==200){
      $("#tb_name").hide();
      $(".user_sign").text(resp.data.user.private_sign);
      $(".user_nick").text(resp.data.user.nick_name);
      if(resp.data.user.sex == "man"){
        $("input[name='sex']").get(0).checked = true;
      }else{
        $("input[name='sex']").get(1).checked = true;
      }
      // $(".user_sex").text(resp.data.user.sex);
      if(resp.data.user.pic_url == null || resp.data.user.pic_url == ""){
        resp.data.user.pic_url = "../static/picture/admin_index.jpg"
      }
      $("#user_pic").attr("src", resp.data.user.pic_url);
      $(".user_phone").text(resp.data.user.phone_num);
      $(".user_live").text(resp.data.user.user_live);
      $(".user_last").text(resp.data.user.last_login);
      $(".btn_op").attr("alter_info", resp.data.user.id);
      $("input[name='i']").val(resp.data.user.id);
      $("#tb_user").show();
    }else{
      alert(resp.errmsg);
    }
  })
}

// 更改用户头像
function alter_pic(){
  // 展示修改的界面
  $(".alter_window").fadeIn();

}

function hide_alter(){
  $('.alter_window').fadeOut();
  $(".alter_info_window").fadeOut();
}

function change_pic(){
  var reads= new FileReader();
       f=document.getElementById('pic_url').files[0];
       reads.readAsDataURL(f);
       reads.onload=function (e) {
           document.getElementById('img_user_pic').src=this.result;
       };
}

// 修改用户信息
function alter_info(){

  $("input[name='nick']").val($('.user_nick').text());

  $("#person_sign").text($('.user_sign').text());

  var sex = $('input[name="sex"]:checked').val();
  if(sex == "man"){
    $("input[name='sex_info']").get(0).checked = true;
  }else{
    $("input[name='sex_info']").get(1).checked = true;
  }

  $("input[name='phone']").val($('.user_phone').text());

  $("input[name='live']").val($('.user_live').text());

  $(".alter_info_window").show();
}
