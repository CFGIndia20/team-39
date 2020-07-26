var Charts = function(){
    var monthlyBarChart = function(){
        var baseURL = window.location.origin;
        var filePath = "/helper/routing.php";
        var purchase_sales=[];
        $.ajax({
            url: baseURL + filePath,
            method: "POST",
            data: {
                "monthly": true,
                "fetch": "purchase"
            },
            dataType : "json",
            success: function(data){
                //console.log(data);
                var l=[];
                var s=[];
                data.forEach(elem => {
                    console.log(elem);
                    l.push(parseInt(elem.month));
                    s.push(elem.sum);
                });
                //console.log(l);
                var arr=[];
                arr[0]=0;
                for(let index = 1; index <= 12; index++) {
                    //console.log(index);
                    if(l.includes(index)){
                        arr[index] = parseInt(s[l.indexOf(index)]);
                    }
                    else{
                        arr[index]=0;
                    }
                    
                }
                var purchase=arr.slice(1,13);
                purchase_sales.push(purchase);
                //console.log(purchase);
                
                //var h = purchase_sales(purchase);
            }
        });

        $.ajax({
            url: baseURL + filePath,
            method: "POST",
            data: {
                "monthly": true,
                "fetch": "sales"
            },
            dataType : "json",
            success: function(data){
                console.log(data);
                var l=[];
                var s=[];
                data.forEach(elem => {
                    console.log(elem);
                    l.push(parseInt(elem.month));
                    s.push(elem.sum);
                });
                //console.log(l);
                var arr=[];
                arr[0]=0;
                for(let index = 1; index <= 12; index++) {
                    //console.log(index);
                    if(l.includes(index)){
                        arr[index] = parseInt(s[l.indexOf(index)]);
                    }
                    else{
                        arr[index]=0;
                    }
                    
                }
                var sales=arr.slice(1,13);
            
                //console.log(purchase);
                purchase_sales.push(sales);
                purchaseSales(purchase_sales);
            }
        });
    }

    var ValuationChart = function(){
        var baseURL = window.location.origin;
        var filePath = "/helper/routing.php";
        var purchase_sales=[];
        $.ajax({
            url: baseURL + filePath,
            method: "POST",
            data: {
                "valuation": true,
            },
            dataType : "json",
            success: function(data){
                //console.log(data);
                makePie(data);
            }
        });
    }
    return{
        init: function(){
            monthlyBarChart();
            ValuationChart();
        }
    }
}();
jQuery(document).ready(function(){
    Charts.init();

    
})

function makePie(data){
    console.log(data);
    var arr=[];
    var labels=[];
    var backgroundcolor = [];
    data.forEach(elem => {
        console.log(elem);
        arr.push(parseInt(elem.sum_rate));
        labels.push(elem.name);
        var r = Math.floor(Math.random() * 200);
        var g = Math.floor(Math.random() * 200);
        var b = Math.floor(Math.random() * 200);
        var color = 'rgb(' + r + ', ' + g + ', ' + b + ')';
        backgroundcolor.push(color);
    });
    console.log(arr);
    var ctx = document.getElementById('valuation-pie').getContext('2d');
    var pie = new Chart(ctx, {
        type: 'pie',
        data: {
            datasets: 
            [
            {
            data: arr,
            backgroundColor: backgroundcolor,
            hoverBorderColor: "rgba(255, 255, 255, 255)",
            }
            
        ],
        labels: labels
    }
        
    });
}

function purchaseSales(purchase_sales){
    //console.log(purchase_sales);
    purchase=purchase_sales[0];
    sales=purchase_sales[1];
    var ctx = document.getElementById('monthly-chart').getContext('2d');
                var myBarChart = new Chart(ctx, {
                    type: 'bar',
                    
                    data: {
                        labels: [
                            'January',
                            'February',
                            'March',
                            'April',
                            'May',
                            'June',
                            'July',
                            'August',
                            'September',
                            'October',
                            'November',
                            'December'
                        ],
                        datasets: [{
                            
                            label: "Monthly Purchase",
                            backgroundColor: 'rgba(240, 127, 154, 0.73)',
                            data: purchase
                        },
                        {
                            label: "Monthly Sales",
                            backgroundColor: 'rgba(129, 127, 240, 0.56)',
                            data: sales
                        }
                        ]
                    },
                    options: {
                        scales: {
                            xAxes: [{
                              
                              ticks: {
                                min: 0
                              }
                            }],
                            yAxes: [{
                              
                            }],
                          }
                    }
                    
                    
                });
    return 1;
}

 