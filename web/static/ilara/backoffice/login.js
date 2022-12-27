function login() {
    formData = $("#loginForm").serializeArray();
    const csrftoken = Cookies.get('csrftoken');
    $.ajax({
        url:"/login/",
        headers:{'X-CSRFToken': csrftoken},
        data: formData,
        method: "POST",
        success: function(response) {
            if (response.message == "success") {
                window.location.href = '/store';
            }
        },
        error: function() {
            UIkit.notification({
                message: 'Error encountered while logging you in. Please try again.',
                status: 'danger',
                pos: 'top-right',
                timeout: 5000
            });
        }
    });
}
