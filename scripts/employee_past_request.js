window.addEventListener("DOMContentLoaded", (event) => {
    str = window.location.pathname.split("/")
    username = str[2]
    fetch("http://127.0.0.1:5000/employee/"+username+"/reimbursements", {method: "GET"})
    .then(response => response.json())
    .then(data => checkResponse(data))
})

function checkResponse(data){
    for(obj in data){
        username_tag = document.createElement("h3")
        username_text = document.createTextNode("username: "+data[obj]["_username"])
        username_tag.appendChild(username_text)

        r_id_tag = document.createElement("h3")
        r_id_text = document.createTextNode("r_id: "+data[obj]["_r_id"])
        r_id_tag.appendChild(r_id_text)

        amount_tag = document.createElement("h3")
        amount_text = document.createTextNode("amount: "+data[obj]["_amount"])
        amount_tag.appendChild(amount_text)

        reason_tag = document.createElement("p")
        reason_tag.id = data[obj]["_amount"] + " " + data[obj]["_reason"]
        reason_text = document.createTextNode("reason: "+data[obj]["_reason"])
        reason_tag.appendChild(reason_text)

        body = document.getElementById("this_article")

        body.appendChild(username_tag)
        body.appendChild(r_id_tag)
        body.appendChild(amount_tag)
        body.appendChild(reason_tag)

        statusCheck(data[obj]["_status"], data[obj]["_r_id"], data[obj]["_manager_response"], body)
    }

    function statusCheck(status, r_id, manager_response, body){
        if(!status){
            status_tag = document.createElement("h4")
            status_tag = document.createTextNode("Status: Awaiting approval")
            body.appendChild(status_tag)
        }
        else{
            status_tag = document.createElement("h4")
            status_tag = document.createTextNode("status: "+data[obj]["_status"])
            body.appendChild(status_tag)
            
            manager_reason_tag = document.createElement("p")
            manager_reason_text = document.createTextNode(manager_response)
            manager_reason_tag.appendChild(manager_reason_text)
            body.appendChild(manager_reason_tag)
        }
    }
}