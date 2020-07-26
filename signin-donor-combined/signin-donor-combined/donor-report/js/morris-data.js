$(function() {

    fetch('http://127.0.0.1:4001/donor')
    .then(response => {
        response.json().then(serverData=>{
            // console.log(serverData);

            let result1 = serverData.result1;
            let result2 = serverData.result2;
            data_donut = [{
                label: "currently working centers",
                value: 0
            }, {
                label: "centers in maintainance",
                value: 0
            }, {
                label: "Currently in development centers",
                value: 0
            }]
            
            for(let i = 0 ; i< result1.length; i++)
            {
                data_donut[i].value = result1[i][0];
            }

            // console.log(data_donut);

            Morris.Donut({
                element: 'morris-donut-chart',
                data: data_donut,
                resize: true
            });

            data_bar =[{
                y: 'Jan',
                a: 0,
                b: 0
            }, {
                y: 'Feb',
                a: 0,
                b: 0
            }, {
                y: 'Mar',
                a: 0,
                b: 0
            }, {
                y: 'Apr',
                a: 0,
                b: 0
            }, {
                y: 'May',
                a: 0,
                b: 0
            }, {
                y: 'Jun',
                a: 0,
                b: 0
            }, {
                y: 'Jul',
                a: 0,
                b: 0
            }]

            for(let i = 0 ; i< result2.length; i++)
            {
                data_bar[i].a = result2[i][0];
                data_bar[i].b = result2[i][1];
            }

            Morris.Bar({
                element: 'morris-bar-chart',
                data: data_bar,
                xkey: 'y',
                ykeys: ['a', 'b'],
                labels: ['With your help', 'Us without you'],
                hideHover: 'auto',
                resize: true
            });
        })
    })
});
