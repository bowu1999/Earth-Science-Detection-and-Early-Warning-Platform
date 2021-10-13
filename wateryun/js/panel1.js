(function (){
    // 图表1
    var myChart = echarts.init(document.getElementById('pl1'));
    var option;

    option = {
        tooltip:{

        },
        toolbox:{
            feature:{
                saveAsImage:{}
            }
        },
        xAxis: {
            type: 'category',
            data: ['周一', '周二', '周三', '周四', '周五', '周六', '周天']
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: 'line',
            smooth: true
            }
        ]
    };
    myChart.setOption(option);
})();