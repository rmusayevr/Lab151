let showMoreButton = document.querySelector(".seeMore")
const FilterLogic = {
  url: `${location.origin}/api/product-list/`,

  filterProduct(categoryId) {
    let url = this.url
    if (categoryId < 4) {
      url = url + '?category__parent=' + categoryId
    }
    else {
      url = url + '?category=' + categoryId
    }
    fetch(url).then(response => response.json()).then(data => {
      document.getElementById('product-list').innerHTML = ''
      for (let i in data) {
        function star() {
          html = ''
          for (let j = 0; j < data[i].star_ratings; j++) {
            html += `<ion-icon name="star"></ion-icon>`
          }
          return html
        }
        function nonstar() {
          html = ''
          for (let j = 0; j < 5 - data[i].star_ratings; j++) {
            html += `<ion-icon name="star-outline"></ion-icon>`
          }
          return html
        }
        document.getElementById('product-list').innerHTML += `
                <div class="showcase">
                <div class="showcase-banner">
                 <a href="${data[i]['detail_url']}">
                  <img src="${data[i].visual_cover_image}" alt="" width="300" class="product-img default">
                  ${data[i].visual_cover_image_2 ? 
                    `<img src="${data[i].visual_cover_image_2}" alt="" width="300" class="product-img hover">` : 
                    `<img src="${data[i].visual_cover_image}" alt="" width="300" class="product-img hover">`}
                 </a>

                  </a>
                  <!-- <p class="showcase-badge">15%</p> -->

                </div>

                <div class="showcase-content">

                  <a href="#" class="showcase-category">${data[i].category[0].name}</a>

                  <a href="${data[i]['detail_url']}">
                    <h3 class="showcase-title">${data[i].title}</h3>
                  </a>

                  <div class="showcase-rating">
                    ${star()}
                    ${nonstar()}
                  </div>
                  
                  <div class="price-box">
                    ${data[i].is_sale ?
                    `<p class="price">₼${data[i].visual_price.toFixed(2)}</p>
                    <del>₼${data[i].real_price.toFixed(2)}</del>`
                    :
                    `<p class="price">₼${data[i].real_price.toFixed(2)}</p>`
                    }
                  </div>
                  
                </div>

              </div>    
                `
      }
      showMoreButton.classList.add('d-none')
    })
  }
}



let filterCategory = document.getElementsByClassName('categories')
for (let i = 0; i < filterCategory.length; i++) {
  filterCategory[i].addEventListener('click', function () {
    let categoryId = this.getAttribute('data')
    FilterLogic.filterProduct(categoryId)
  })
}