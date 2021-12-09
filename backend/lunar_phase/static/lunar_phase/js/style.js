
$(function () {
    const token = localStorage.getItem("token")
    $.ajax({
        type: 'GET',
        dataType: 'json',
        beforeSend: function (xhr){
            xhr.setRequestHeader('Authorization', "Basic " + token);
        },
        url: '/api/current_lp',
        success: function (data) {
            const response = data;
            $('h1').text(response.current_phase);
        }
    });
})