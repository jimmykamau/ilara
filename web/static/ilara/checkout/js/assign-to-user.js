function reassignCustomer(orderId) {
    profileId = $("#assignCustomer").val()
    postData = {"profileId": profileId, "orderId": orderId}
    const csrftoken = Cookies.get('csrftoken');
    $.ajax({
        url:"/store/checkout/reassign/",
        headers:{'X-CSRFToken': csrftoken},
        data: postData,
        method: "POST",
        success: function(response) {
            if (response.message == "success") {
                UIkit.notification({
                    message: 'Order reassigned successfully.',
                    status: 'success',
                    pos: 'top-right',
                    timeout: 5000
                });
            }
        },
        error: function() {
            UIkit.notification({
                message: 'Error encountered while reassigning the order. Please try again.',
                status: 'danger',
                pos: 'top-right',
                timeout: 5000
            });
        }
    });
}
