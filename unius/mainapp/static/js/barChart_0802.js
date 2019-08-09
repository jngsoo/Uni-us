Highcharts.chart('barChart_0802', {
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
            ['일본', 236] , ['나라', 174] , ['경제', 138] , ['문재인', 114] , ['학점', 92] , ['정부', 79] , ['정치', 64] , ['교양', 63] , ['재수강', 60] , ['북한', 55] , ['자한당', 54] , ['대통령', 48] , ['경영', 48] , ['외교', 46] , ['수강신청', 42] , ['미국', 42] , ['이중', 41] , ['문재앙', 40] , ['글캠', 37] , ['보수', 36]
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