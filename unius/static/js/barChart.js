Highcharts.chart('barChart', {
    chart: {
    type: 'column'
    },
    title: {
    text: 'Hot Keyword'
    },
    xAxis: {
    categories: ['Africa', 'America', 'Asia', 'Eursope', 'Oceania','hel']
    },
    series: [{
    name: 'Year 1800',
    data: [107, 31, 635, 203, 2]
    }, {
    name: 'Year 1900',
    data: [133, 156, 947, 408, 6]
    }, {
    name: 'Year 2012',
    data: [1052, 954, 4250, 740, 38]
    }]
});