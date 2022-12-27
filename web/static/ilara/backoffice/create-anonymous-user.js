function createAnonymousUser() {
    const csrftoken = Cookies.get('csrftoken');
    $.ajax({
        url:"/signup/anon/",
        headers:{'X-CSRFToken': csrftoken},
        method: "POST",
        success: function(response) {
            if (response.message == "success") {
                window.location.replace('/store')
            } else {
                UIkit.notification({
                    message: 'Error encountered while signing you in. Please try again.',
                    status: 'danger',
                    pos: 'top-right',
                    timeout: 5000
                });
            }
        }
    });
}
