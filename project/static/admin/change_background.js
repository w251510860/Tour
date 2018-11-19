/**
 * Created by wo on 2018/10/23.
 */

$(document).ready(function () {
    var pic_list = Back.curBack.split("..");
    $("#img_back").attr("src", pic_list[".." + Back.index]);
    // alert("11");
    $('.btn_change').click(function () {
        Back.index += 1;
        // alert(Back.curBack);
        if(Back.index > 5){
            Back.index = 1;
        }
        $(".index_back").val(Back.index);
        $("#img_back").attr("src", pic_list[Back.index]);
    });
});
