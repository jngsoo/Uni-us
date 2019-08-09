Highcharts.chart('barChart_0804', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Hot Keyword'
    },
    subtitle: {
        text: '출처 : 한국외대 에브리타임'
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
        name: 'Population',
        data: [
            ['일본', 174] , ['나라', 98] , ['학점', 68] , ['수강신청', 58] , ['이중', 57] , ['경제', 51] , ['경영', 50] , ['재수강', 47] , ['교양', 36] , ['졸업', 31] , ['알바', 29] , ['북한', 29] , ['증원', 28] , ['보수', 27] , ['선동', 27] , ['불매운동', 26] , ['미국', 26] , ['정부', 26] , ['부전공', 21] , ['이중전공', 20] ,
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