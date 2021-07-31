window.addEventListener("DOMContentLoaded", (event) => {
    str = window.location.pathname.split("/")
    username = str[2]
    fetch("http://127.0.0.1:5000/manager/"+username+"/get_reimbursements", {method: "GET"})
    .then(response => response.json())
    .then(data => checkResponse(data))
})

function checkResponse(data){
    for(obj in data){
        username_tag = document.createElement("h3")
        username_text = document.createTextNode("username: "+data[obj]["_username"])
        username_tag.appendChild(username_text)

        r_id_tag = document.createElement("h3")
        r_id_text = document.createTextNode("r_id:" +data[obj]["_r_id"])
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
            approve_button = document.createElement("button")
            approve_button.innerHTML = "Approve"
            approve_button.id = "approve_" + r_id
            disapprove_button = document.createElement("button")
            disapprove_button.innerHTML = "Disapprove"
            disapprove_button.id = "disapprove_" + r_id
            body.appendChild(approve_button)
            body.appendChild(disapprove_button)

            manager_response_textbox = document.createElement("input")
            manager_response_textbox.type = "text"
            manager_response_textbox.id = "textbox_" + r_id
            body.appendChild(manager_response_textbox)
        }
        else{
            status_tag = document.createElement("h4")
            status_tag.id = "status_"+status + "_" +r_id
            status_tag = document.createTextNode("status: "+status)
            body.appendChild(status_tag)
            //Create textbox

            manager_reason_tag = document.createElement("p")
            manager_reason_text = document.createTextNode(manager_response)
            manager_reason_tag.appendChild(manager_reason_text)
            body.appendChild(manager_reason_tag)
        }
    }

    this_article.addEventListener("click", (event) =>{
        if(event.target.innerHTML != "Disapprove" && event.target.innerHTML != "Approve"){
            return
        }
        else{
            fetchbody = getFetchBody(event)
        
            str = window.location.pathname.split("/")
            username = str[2]
            fetch("http://127.0.0.1:5000/manager/"+username+"/approve_reimbursements", {method: "PUT", body: JSON.stringify(fetchbody)})
            .then(response => console.log(response))
        }
    })

    function getFetchBody(event){
        const obj = {}
        const target = event.target
        target_str = target.id.split("_")

        obj['r_status'] = target_str[0]
        obj['r_id'] = target_str[1]

        if(document.getElementById("textbox_" + target_str[1]).value === ""){
            obj['manager_response'] = "No response"
        }
        else{
            obj['manager_response'] = document.getElementById("textbox_" + target_str[1]).value
        }
        return obj
    }
    
}