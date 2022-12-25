let assessment_name = $('#hidden').attr('name')
let endpoint = `http://127.0.0.1:5000/assessment/${assessment_name}`
let answersForm = document.querySelector('#answersForm')


document.onvisibilitychange = () => $('#answersForm').submit()

function createRequest(){
    let obj = {}
    const formData = new URLSearchParams(new FormData(answersForm))
    formData.forEach((value, key) => obj[key] = value)

    return JSON.stringify(obj)
}


answersForm.onsubmit = e => {
    e.preventDefault()
    let request_data = createRequest()

    fetch(endpoint, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: request_data
    })
    .then(res => {
        return res.json()
    })
    .then(data => {
        $(document.body).replaceWith(
            '<h2>Result</h2>\
            <p>Total: ' + data.total + '</p>\
            <p>Got:' + data.score + '</p>\
            <p>Failed: ' + data.failed + '</p>\
            <p>Score: ' + data.percent_score + '%</p>\
            <a href="http://127.0.0.1:5000/profile"><button>back to profile</button></a>'
        )
    })
}


