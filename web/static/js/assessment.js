let assessment_name = $('#hidden').attr('name')
let endpoint = `http://127.0.0.1:5000/assessment/${assessment_name}`
let answersForm = document.querySelector('#answersForm')
let displayed_result = false

document.onvisibilitychange = () => {
    if (!displayed_result)
        $('#answersForm').submit()
}

function createRequest(){
    let user_choices = {}
    const formData = new URLSearchParams(new FormData(answersForm))
    formData.forEach((value, key) => user_choices[key] = value)

    return user_choices
}


answersForm.onsubmit = e => {
    e.preventDefault()
    let user_choices = createRequest()

    fetch(endpoint, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(user_choices)
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

        delete user_choices[assessment_name]
        $('#reset').hide(), $('#submit').hide()

        const keys = Object.keys(correct_answers)
        keys.forEach(key => {
            if (correct_answers[key] === user_choices[key])
                $(`#${key}`).text('Correct')
            else $(`#${key}`).text(`Incorrect: ${correct_answers[key]}`)
        });
        displayed_result = true
    })
}


