function addToCart(productId) {
    postData = {"productId": productId}
    const csrftoken = Cookies.get('csrftoken');
    $.ajax({
        url:"/store/cart/",
        headers:{'X-CSRFToken': csrftoken},
        data: postData,
        method: "POST",
        success: function(response) {
            if (response.message == "success") {
                UIkit.notification({
                    message: 'Added to cart!',
                    status: 'success',
                    pos: 'top-right',
                    timeout: 5000
                });
            }
            else if (response.message == "Out of stock") {
                UIkit.notification({
                    message: response.message,
                    status: 'warning',
                    pos: 'top-right',
                    timeout: 5000
                });
            }
        },
        error: function(response) {
            if (response.message == "error") {
                UIkit.notification({
                    message: 'Error encountered while adding your item to cart. Please try again.',
                    status: 'danger',
                    pos: 'top-right',
                    timeout: 5000
                });
            }
        }
    })
}
