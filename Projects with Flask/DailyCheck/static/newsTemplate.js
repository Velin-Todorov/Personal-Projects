import { html, render } from 'https://unpkg.com/lit-html?module';
import { repeat } from './node_modules/lit-html/directives/repeat.js'
import { pagination } from './news.js';

export function renderArticles(data){
    
    console.log(data)
    let el = html`
        <h1> ${data['articles'].length} result/s found</h1>

            <br>

            <div class="row m-5">
                ${repeat(data['articles'], (item) => html`
                    <div class="col">
                        <div class="card border-dark mb-5 card text-dark">
                            <img src="${item.urlToImage}" style="max-width:310px; max-height:300px">
                                <div class="card-body" style="height:auto; width:auto;">
                                                                        
                                    <h5 class="card-title" style="font-size: 30px; display: inline;"> 
                                        <a href="${item.url}" target="_blank" rel="noopener noreferrer" >${item.title}</a>
                                        
                                    </h5>

                                    <p class="card-text" style="font-size: 20px">
                                        By: ${item.author}
                                    </p>

                                    <p class="card-text" style="font-size: 20px">
                                        Published on: ${new Date(item.publishedAt).toLocaleDateString('en-GB')}
                                    </p>
                                </div>
                        </div>
                    </div>`)}
            </div>

            <nav aria-label="Page navigation example">
                <ul class="pagination">
                    <li class="page-item"><button @click="${pagination}" class="page-link" href="#">Previous</button></li>
                    <li class="page-item"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item"><a class="page-link" href="#">Next</a></li>
                </ul>
            </nav>
    `
    return el
}

// TODO: Figured out how to do the pagination. I am thinking of using a generator function that will slice the html collection. 