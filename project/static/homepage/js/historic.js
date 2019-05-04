$(function () {
    // 首次进入，去加载新闻列表数据
    updateNewsData()
});

function updateNewsData() {
    var params = {
        "page_num": 1,
        'per_page': 50
    };
    $.get("/scenic/scenic_list", params, function (resp) {
        if (resp) {
            // 先清空原有数据
            // 显示数据
            for (var i = 0; i < resp.newsList.length; i++) {
                var news = resp.newsList[i];
                var content = '<li id="plant">[旅游资讯]';
                content += "<a href='/scenic/" + news.id +"'>" + news.title + '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + '推荐时间 :' + news.advice_time + '</a>';
                content += '</li>';
                $(".con_news").append(content)
            }
        }
    })
}