function removeFromCart(itemId) {
    const csrftoken = Cookies.get('csrftoken');
    $.ajax({
        url:"/store/cart/"+itemId+"/",
        headers:{'X-CSRFToken': csrftoken},
        method: "DELETE",
        success: function(response) {
            if (response.message == "success") {
                UIkit.notification({
                    message: 'Removed from cart!',
                    status: 'success',
                    pos: 'top-right',
                    timeout: 5000
                });
                window.location.href = '/store/cart/';
            } else {
                console.log(response)
                UIkit.notification({
                    message: 'Error encountered while removing your item from cart. Please try again.',
                    status: 'danger',
                    pos: 'top-right',
                    timeout: 5000
                });
            }
        }
    })
}
