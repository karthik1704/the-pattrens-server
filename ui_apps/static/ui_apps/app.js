
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const portfolio = document.getElementById('portfolio');
const searchEl = document.getElementsByClassName('search');

let platform = [];
let patterns = [];
let category = [];
let elements = [];
let next = null;
let previous = null;

function main(id=null){
    $.ajax({
        url: '/api/v1/apps/list',
        data: {
            ...(id && { platform: id }),

        },
        success: (res)=>{
            console.log("success -> ", res)
            // portfolio.innerHTML = '';
            let height  = Math.ceil(res.count/4) * 408.656;
            next = res.next;
            previous = res.previous;
            console.log(height);
            console.log(portfolio.style.cssText);
            portfolio.style.cssText = `height: ${height}px; margin: 0px -20px -20px 0px; position: relative;`;
            console.log(portfolio.style.cssText);
            res.count>0 ? res.results.map((item)=>{
                portfolio.innerHTML = `
                <div
                class="portfolio-item img-zoom ct-photography ct-media ct-branding ct-Media ct-webdesign"
                >
                    <a href="/detail/${item.slug}">
                        <div class="portfolio-item-wrap">
                            <div class="portfolio-image">
                                <img src="${item.image}" alt="" />
                            </div>
                
                            <div class="portfolio-contents">
                                <div class="fst-content">
                                    <h2>${item.name}</h2>
                                    <div class="portfolio-heart">
                                    <i class="fas fa-heart"></i>466
                                    </div>
                                </div>
                
                                <div class="portfolio-detail sec-content">
                                    <p>Travel and share the Best moments</p>
                                    <div class="portfolio-clock">
                                        <i class="far fa-clock"></i>APR 26
                                    </div>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>`
            }) :  portfolio.innerHTML =`<div> NO APPS </div>`;
        
        },
        error: (err) => console.error(err),

    });
}

portfolio.addEventListener('load' , main());


const handlePlatformChange = (cb) => {
    if (cb.checked){
        platform.push(cb.value);
    } else {
       let idx = platform.indexOf(cb.value)
       if (idx !== -1){
           platform.splice(idx, 1);
       }
    }
    console.log(platform);
};

const onHandleMenuClick = (id)=>{

   id === 0 ? main() : main(id=id);
}

const handleCategoryChange = (cb) => {
    if (cb.checked){
        category.push(cb.value);
    } else {
       let idx = category.indexOf(cb.value)
       if (idx !== -1){
           category.splice(idx, 1);
       }
    }
    console.log(category);
};

const handlePatternsChange = (cb) => {
    if (cb.checked){
        patterns.push(cb.value);
    } else {
       let idx = patterns.indexOf(cb.value)
       if (idx !== -1){
           patterns.splice(idx, 1);
       }
    }
    
    console.log(patterns);
};

const handleElementsChange = (cb) => {
    if (cb.checked){
        elements.push(cb.value);
    } else {
       let idx = elements.indexOf(cb.value)
       if (idx !== -1){
           elements.splice(idx, 1);
       }
    }
    console.log(elements);
};

// Search 

$(".search").on("change", function(){
    console.log($(this).val());
});