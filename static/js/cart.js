count = document.querySelector('.count')
count_mobile = document.querySelector('.count-mobile')
total = document.querySelector("#total_price")
let price;
quantity = document.querySelector('.quantity')

let downButton = document.querySelectorAll("#stepDown")
downButton.forEach(element => {
    element.addEventListener("click", function() {
        price = element.parentElement.parentElement.querySelector('.price').innerHTML;
        let ProductID = this.getAttribute('data');
        if (parseInt(count.innerHTML) > 1) {
        fetch(`${location.origin}/api/basket/`, {
            method: 'PATCH',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('token')}`,
            },
            body: JSON.stringify({
                'productDown': ProductID,
            })
        }).then(response => response.json()).then(data => {
            
                count_mobile.innerHTML = parseInt(count_mobile.innerHTML) - 1
                count.innerHTML = parseInt(count.innerHTML) - 1
                total.innerHTML = (parseFloat(total.innerHTML) - parseFloat(price)).toFixed(2)
        })}
    });
});

let upButton = document.querySelectorAll("#stepUp")
upButton.forEach(element => {
    element.addEventListener("click", function() {
        price = element.parentElement.parentElement.querySelector('.price').innerHTML;
        let ProductID = this.getAttribute('data');
        fetch(`${location.origin}/api/basket/`, {
            method: 'PATCH',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('token')}`,
            },
            body: JSON.stringify({
                'productUp': ProductID,
            })
        }).then(response => response.json()).then(data => {
            count_mobile.innerHTML = parseInt(count_mobile.innerHTML) + 1
            count.innerHTML = parseInt(count.innerHTML) + 1
            total.innerHTML = (parseFloat(total.innerHTML) + parseFloat(price)).toFixed(2)
        })
    });
});

let removeButton = document.querySelectorAll("#remove")
removeButton.forEach(element => {
    element.addEventListener("click", function() {
        let ProductID = this.getAttribute('data');
        let qty = element.parentElement.querySelector('.quantity').value
        price = parseFloat(element.parentElement.parentElement.querySelector('.price').innerHTML).toFixed(2)
        element.parentElement.parentElement.parentElement.classList.add('d-none')
        fetch(`${location.origin}/api/basket/`, {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        }).then(response => response.json()).then(data => {
                count_mobile.innerHTML = parseInt(count_mobile.innerHTML) - parseInt(qty)
                count.innerHTML = parseInt(count.innerHTML) - parseInt(qty)
                total.innerHTML = (parseFloat(total.innerHTML) - parseInt(qty)*parseFloat(price)).toFixed(2)
            })
    });
});
