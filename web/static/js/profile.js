let user_id = $('#user_id').val()
let endpoint = 'http://127.0.0.1:5001/api/v1/status/' + user_id

function makeRequest(endpoint) {
    return new Promise((resolve, reject) => {
        $.get(endpoint, (data, status) => {
            if (status === 'success')
                resolve(data)
        })
    })
}

$('.start-test-btn').click(function(event){
    event.preventDefault()
    currentAssessment = $(this).attr('href').split('/').pop()
    assessmentUrl = `http://127.0.0.1:5000/assessment/${currentAssessment}`

    makeRequest(endpoint).then(data => {
        if (!data[currentAssessment]) {
            window.open(assessmentUrl)
            return
        }
        if (!confirm('Starting a new test would clear previous records. Do you want to continue?'))
            return

        let refreshPromise = new Promise((resolve, reject) => {
            $.ajax({
                type: 'PUT',
                url: 'http://127.0.0.1:5001/api/v1/refresh_user',
                contentType: 'application/json',
                data: `{"user_id": "${user_id}", "assessment_name": "${currentAssessment}"}`,
                success: newData => resolve (newData)
            })
        });
        refreshPromise.then( newData => {
            window.open(assessmentUrl)
        })
    })
})
