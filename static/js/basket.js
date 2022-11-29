function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
let buttonBasket = document.querySelectorAll(".addCart")
buttonBasket.forEach(element => {
    element.addEventListener("click", function() {
        const quantity = 1;
        fetch(`${location.origin}/api/basket/`, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('token')}`,
            },
            body: JSON.stringify({
                'product': element.id,
                'quantity': quantity
            })
        }).then(response => response.json()).then(data => {
            if (data.success == undefined) {
                q = document.querySelector('.count')
                q_mobile = document.querySelector('.count-mobile')
                q.innerHTML = parseInt(q.innerHTML)+1
                q_mobile.innerHTML = parseInt(q_mobile.innerHTML)+1
            }
        })
    });
});
