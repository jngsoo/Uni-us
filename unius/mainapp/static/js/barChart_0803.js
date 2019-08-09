Highcharts.chart('barChart_0803', {
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
            ['일본', 202] , ['학점', 102] , ['나라', 57] , ['미국', 56] , ['교양', 55] , ['경제', 55] , ['이중', 49] , ['경영', 46] , ['영특', 39] , ['수강신청', 37] , ['정부', 37] , ['군대', 35] , ['북한', 33] , ['외교', 25] , ['재수강', 24] , ['시간표', 22] , ['에타', 22] , ['수능', 22] , ['졸업', 21] , ['달라', 20] 
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