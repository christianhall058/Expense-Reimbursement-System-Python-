reimbursement_request.addEventListener('click', (event) => {
    username = window.location.pathname.slice(10)
    window.location.href = "http://127.0.0.1:5000/employee/" + username + "/reimburse_request"
})

reimbursements_view.addEventListener('click', (event) => {
    username = window.location.pathname.slice(10)
    window.location.href = "http://127.0.0.1:5000/employee/" + username + "/past_requests"
})