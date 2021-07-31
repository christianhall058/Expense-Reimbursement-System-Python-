submitbtn.addEventListener('click', (event) => {
    formdata = getFormData()
    fetch("http://127.0.0.1:5000/findEmployee", {method: "POST", body: JSON.stringify(formdata)})
    .then(response => response.json())
    .then(data => checkResponse(data))
})

function checkResponse(data){
    if(!data){
        document.getElementById("user_pass_error_message").innerHTML="Invalid Credentials"
        location.reload()
    }
    else{
        parsed_data = parsedata(data)
        if(parsed_data === "e"){
            window.location.href = "http://127.0.0.1:5000/employee/" + formdata['username']
        }
        else if(parsed_data === "m"){
            window.location.href = "http://127.0.0.1:5000/manager/" + formdata['username']
        }
    }
}

function parsedata(data){
    for(obj in data[0]){
        parsed_data = data[0][obj]
    }
    return parsed_data
}

function getFormData(){
    const obj = {}
    obj["username"] = document.getElementById("myform").elements[0].value
    obj["password"] = document.getElementById("myform").elements[1].value

    return obj
}