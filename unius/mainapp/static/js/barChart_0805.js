Highcharts.chart('barChart_0805', {
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
                ['경제', 247],
                ['수강신청', 226],
                ['일본', 223],
                ['나라', 204],
                ['문재인', 145],
                ['경영', 138],
                ['정치', 125],
                ['문재앙', 103],
                ['이중', 102],
                ['학점', 91], 
                ['북한', 71],
                ['정부', 71],
                ['대통령', 64],
                ['미국', 58],
                ['휴학', 56],
                ['재수강', 54],
                ['교양', 54],
                ['졸업', 50],
                ['보수', 48],
                ['강사', 45], 
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