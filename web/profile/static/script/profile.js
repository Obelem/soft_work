let user_id = $('#user_id').val()
let endpoint = 'http://rabahk.tk/api/v1/status/' + user_id

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
    assessmentUrl = `http://rabahk.tk/assessment/${currentAssessment}`

    makeRequest(endpoint).then(data => {
        if (!data[currentAssessment]) {
            window.open(assessmentUrl, '_self')
            return
        }
        if (!confirm('Starting a new test would clear previous records. Do you want to continue?'))
            return

        let refreshScoresPromise = new Promise((resolve, reject) => {
            $.ajax({
                type: 'PUT',
                url: 'http://rabahk.tk/api/v1/refresh_user',
                contentType: 'application/json',
                data: `{"user_id": "${user_id}", "assessment_name": "${currentAssessment}"}`,
                success: newData => resolve (newData)
            })
        });
        refreshScoresPromise.then( newData => {
            window.open(assessmentUrl, '_self')
        })
    })
})

$('body').mouseover(event => {
    let target = $(event.target)
    if (target.is($('.certificate_link'))) {
        if (target.data('score') >= 50) return;

        target.click(e => e.preventDefault())

        if (target.data('score') < 50) {
            target.attr('title', 'Certificate unavailable: score is less than 50%');
            return;
        }
        target.attr('title', 'Score 50% or above to generate certificate');
    }
})

$('#delete-account-link').click(e => {
    e.preventDefault();

    if (!confirm('Do you really want to leave?\nThis would wipe all your details from SoftWork'))
        return;

    fetch('http://rabahk.tk/api/v1/delete_user', {
        method: 'DELETE'
    })
    .then(res => { return res.json() } )
    .then(userIs => {
        if (userIs.deleted) {
            window.location.replace('http://rabahk.tk');
        }
    })
})
