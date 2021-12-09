
$(function () {
    const token = localStorage.getItem("token");
    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    const url = '/api/lunar_phase' + '?timezone=' + timezone
    $.ajax({
        type: 'GET',
        dataType: 'json',
        beforeSend: function (xhr){
            xhr.setRequestHeader('Authorization', "Basic " + token);
        },
        url: url,
        success: function (data) {
            const response = data;
            $('h1').text(response.current_phase);
        }
    });
})