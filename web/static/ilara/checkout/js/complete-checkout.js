function completeCheckout(orderId) {
    postData = {"orderId": orderId}
    const csrftoken = Cookies.get('csrftoken')
    $.ajax({
        url:"/store/checkout/",
        headers:{'X-CSRFToken': csrftoken},
        data: postData,
        method: "POST",
        success: function(response) {
            if (response.message == "success") {
                UIkit.notification({
                    message: 'Payment processed successfully.',
                    status: 'success',
                    pos: 'top-right',
                    timeout: 5000
                });
            };
            setTimeout(() => {
                window.location.href = '/store/'
            }, 3000);
        },
        error: function() {
            UIkit.notification({
                message: 'Error encountered while processing payment. Please try again.',
                status: 'danger',
                pos: 'top-right',
                timeout: 5000
            });
        }
    });
}
