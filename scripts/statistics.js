window.addEventListener("DOMContentLoaded", (event) => {
    str = window.location.pathname.split("/")
    username = str[2]
    fetch("http://127.0.0.1:5000/manager/"+username+"/get_statistics", {method: "GET"})
    .then(response => response.json())
    .then(data => checkResponse(data))
})

function checkResponse(data){
    for (obj in data){
        statistic = document.createElement("h3")
        statistic_info = document.createTextNode(obj + ": " + data[obj])
        statistic.appendChild(statistic_info)
        body = document.getElementById("this_article")
        body.appendChild(statistic)
    }
}