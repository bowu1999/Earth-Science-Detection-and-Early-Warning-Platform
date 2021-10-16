function trends(){
    var myChart = echarts.init(document.getElementById('pl1'));
    var option;
    let base = +new Date(1988, 9, 3);
    let oneDay = 24 * 3600 * 1000;
    let data = [[base, Math.random() * 300]];
    for (let i = 1; i < 20000; i++) {
      let now = new Date((base += oneDay));
      data.push([+now, Math.round((Math.random() - 0.5) * 20 + data[i - 1][1])]);
    }
    option = {
        tooltip: {
            trigger: 'axis',
            position: function (pt) {
            return [pt[0], '10%'];
            }
        },
        title: {
            left: 'center',
            show:true, 
            text: '水位变化图',
            textStyle:{
                //文字颜色
                color: 'cadetblue',
                //字体风格,'normal','italic','oblique'
                fontStyle:'normal',
                //字体粗细 'normal','bold','bolder','lighter',100 | 200 | 300 | 400...
                fontWeight:'bold',
                //字体系列
                fontFamily:'sans-serif',
                //字体大小
                fontSize:20
            }
        },
        textStyle:{
            //文字颜色
            color: 'cadetblue',
            //字体风格,'normal','italic','oblique'
            fontStyle:'normal',
            //字体粗细 'normal','bold','bolder','lighter',100 | 200 | 300 | 400...
            fontWeight:'bold',
            //字体系列
            fontFamily:'sans-serif',
            //字体大小
            fontSize:18
        },
        toolbox: {
            feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                dataView: { //数据视图
                    show: true,
                    readOnly: false//是否只读
                },
                magicType: {//切换图表
                    show: true,
                    type: ['line', 'bar', 'stack', 'tiled']//图表
                },
                restore: {},
                saveAsImage: {}
            },
            iconStyle:{
                normal:{
                    borderColor:'cadetblue'
                }
            }
        },
        xAxis: {
            type: 'time',
            boundaryGap: false
        },
        yAxis: {
            type: 'value',
            boundaryGap: [0, '100%']
        },
        dataZoom: [
        {
            type: 'inside',
            start: 0,
            end: 20
        },
        {
            start: 0,
            end: 20
        }
        ],
        series: [
        {
            name: 'Fake Data',
            type: 'line',
            smooth: true,
            symbol: 'none',
            areaStyle: {},
            data: data
        }
        ]
    };

    myChart.setOption(option);
}
trends();