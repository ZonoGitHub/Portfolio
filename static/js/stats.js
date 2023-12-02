var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
   type: 'bar', //doughnut
    data:{
        labels:['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets:[{
            label:'# of Votes',
            data:[12,19,3,5,2,3],
            backgroundColor:[
                'rgba(225, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(225, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(225, 159, 64, 0.2)',
            ],
            borderColor:[
                'rgba(225, 99, 132, 0.2)',
                'rgba(225, 99, 132, 0.2)',
                'rgba(225, 99, 132, 0.2)',
                'rgba(225, 99, 132, 0.2)',
                'rgba(225, 99, 132, 0.2)',
                'rgba(225, 99, 132, 0.2)',
            ],

            borderWidth:1
        }]
    },
option:{
    //title:{
      //  display:true,
      //  text: "livre par categorie", },
    scales:{
        yAxes:[{
            ticks:{
                beginAtZero:true
}
}],
}
}
})