let button = document.querySelector(".seeMore")
let products = document.querySelector("#product-list")

button.addEventListener("click", function() {
    let url = `${location.origin}/api/product-list/`;
    let all_products = document.querySelectorAll(".showcase")
    let count = all_products.length+4;
    fetch(url).then(response => response.json()).then(data => {
        document.getElementById('product-list').innerHTML = ''
      for (let i in data) {
        if (i == count || i == data.length ) {
            break;
        }
        else {
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

                  <a href="#" class="showcase-category">${data[i].category.name}</a>

                  <a href="${data[i]['detail_url']}">
                    <h3 class="showcase-title">${data[i].title}</h3>
                  </a>

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
        }
    })
})
