Highcharts.chart('barChart_0801', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Hot Keyword'
    },
    subtitle: {
        text: '출처 : 한국외대 애브리타임'
    },
    xAxis: {
        type: 'category',
        labels: {
            rotation: -45,
            style: {
                fontSize: '13px',
                fontFamily: 'Verdana, sans-serif'
            }
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: '단어 빈출 횟수'
        }
    },
    legend: {
        enabled: false
    },
    tooltip: {
        pointFormat: 'Population in 2017: <b>{point.y:.1f} millions</b>'
    },
    series: [{
        name: 'word',
        data: [
            ['학점', 81] , ['경제', 56] , ['나라', 38] , ['이중', 37] , ['경영', 36] , ['글캠', 36] , ['수강신청', 28] , ['미국', 27] , ['에타', 26] , ['최저임금', 26] , ['교양', 25] , ['졸업', 24] , ['일본', 24] , ['규제', 24] , ['정시', 23] , ['재수강', 22] , ['수시', 22] , ['자선', 21] , ['시간표', 20] , ['남친', 19]
        ],
        dataLabels: {
            enabled: true,
            rotation: -90,
            color: '#FFFFFF',
            align: 'right',
            format: '{point.y:.0f}', // one decimal
            y: 10, // 10 pixels down from the top
            style: {
                fontSize: '13px',
                fontFamily: 'Verdana, sans-serif'
            }
        }
    }]
});