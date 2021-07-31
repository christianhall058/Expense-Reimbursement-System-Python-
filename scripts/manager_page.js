reimbursements_view.addEventListener('click', (event) => {
    username = window.location.pathname.slice(9)
    window.location.href = "http://127.0.0.1:5000/manager/" + username + "/reimbursement_view"
})

statistics_view.addEventListener('click', (event) => {
    username = window.location.pathname.slice(9)
    window.location.href = "http://127.0.0.1:5000/manager/" + username + "/statistics"
})