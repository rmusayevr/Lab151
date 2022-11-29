const FilterLogic = {
    url: `${location.origin}/api/product-list/`,

    filterProduct(categoryId) {
        let url = this.url
        if (categoryId) {
            url = url + '?category=' + categoryId
        }
        fetch(url).then(response => response.json()).then(data => {
            document.getElementById('product-list').innerHTML = ''
            console.log(data)
            for (let i in data) {
                document.getElementById('product-list').innerHTML += `
                <div class="showcase">

                <div class="showcase-banner">

                 <a href="">
                  <img src="${data[i].visual_cover_image}" alt="" width="300" class="product-img default">`
                  
                  if (data[i].visual_cover_image_2) { +
                  `<img src="${data[i].visual_cover_image_2}" alt="" width="300" class="product-img hover">`
                  }
                  
                  else { +
                  `<img src="${data[i].visual_cover_image}" alt="" width="300" class="product-img hover">` +
                 `</a>

                  </a>
                  <!-- <p class="showcase-badge">15%</p> -->

                  <div class="showcase-actions">

                    <button class="btn-action">
                      <ion-icon name="eye-outline"></ion-icon>
                    </button>


                    <button class="btn-action">
                      <ion-icon name="bag-add-outline"></ion-icon>
                    </button>

                  </div>

                </div>

                <div class="showcase-content">

                  <a href="#" class="showcase-category">${data[i].category[0].name}</a>

                  <a href="#">
                    <h3 class="showcase-title">${data[i].title}</h3>
                  </a>

                  
                  <div class="price-box">
                    
                    <p class="price">${data[i].visual_price}</p>
                    <del></del>
                    
                    
                    
                  </div>
                </div>

              </div>    
                `
            }
        })
    }
}

let filterCategory = document.getElementsByClassName('menu-title')
for (let i = 0; i < filterCategory.length; i++) {
    filterCategory[i].addEventListener('click', function () {
        let categoryId = this.getAttribute('data')
        FilterLogic.filterProduct(categoryId)
        console.log(categoryId)
    })
}