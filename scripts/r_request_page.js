submit_request.addEventListener('click', (event) => {
    formdata = getFormData()
    str = window.location.pathname.split("/")
    username = str[2]
    fetch("http://127.0.0.1:5000/employee/"+username+"/reimburse_request/form", {method: "POST", body: JSON.stringify(formdata)})
    .then(response => response.json())
    .then(data => checkResponse(data))
})

function checkResponse(parsed_data){
    //For later implementation of ducks
    // if(parsed_data === "duck"){
    //     window.location.href = "http://127.0.0.1:5000/employee/" + formdata['username']
    // }
    // else if(parsed_data === "kill duck"){
    //     window.location.href = "http://127.0.0.1:5000/manager/" + formdata['username']
    // }
    // else{}
    if(parsed_data === true){
        return true
    }
    else{
        return false
    }

}

function getFormData(){
    const obj = {}
    obj["amount"] = document.getElementById("myform").elements[0].value
    obj["reason"] = document.getElementById("myform").elements[1].value

    return obj
}