let assessment_name = $('#hidden').attr('name')
let endpoint = `http://127.0.0.1:5000/assessment/${assessment_name}`
let answersForm = document.querySelector('#answersForm')
let displayed_result = false

document.onvisibilitychange = () => {
    if (!displayed_result)
        $('#answersForm').submit()
}

function createRequest(){
    let obj = {}
    const formData = new URLSearchParams(new FormData(answersForm))
    formData.forEach((value, key) => obj[key] = value)

    return obj
}


answersForm.onsubmit = e => {
    e.preventDefault()
    let request_data = createRequest()

    fetch(endpoint, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(request_data)
    })
    .then(res => {
        return res.json()
    })
    .then(report_card => {
        statistics = report_card[0]
        correct_answers = report_card[1]

        $('.statistics').append(
            '<h2> Result </h2\
            <p>Total: ' + statistics.total + '</p>\
            <p>Got: ' + statistics.score + '</p>\
            <p>Failed: ' + statistics.failed + '</p>\
            <p>Score: ' + statistics.percent_score + '%</p>'
        )

        const radioButtons = document.querySelectorAll('input')
        radioButtons.forEach(radioButton => radioButton.disabled = true)

        delete request_data[assessment_name]
        $('#reset').hide(), $('#submit').hide()

        const keys = Object.keys(correct_answers)
        keys.forEach(key => {
            if (correct_answers[key] === request_data[key])
                $(`#${key}`).text('Correct')
            else $(`#${key}`).text(`Incorrect: ${correct_answers[key]}`)
        });
        displayed_result = true
    })
}


