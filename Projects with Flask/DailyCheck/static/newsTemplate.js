import { html, render } from 'https://unpkg.com/lit-html?module';
import { repeat } from './node_modules/lit-html/directives/repeat.js'


const paginationLimit = 8
let currentPage;
let pageCount;

export function renderArticles(data){
    
    let el = html`
        <h1>

            <br>
            
            <div class="row m-5">
                ${repeat(data['articles'], (item) => html`
                    <div class="col py-3" style="max-width: 500px; height: 450px;">
                        <div class="card">
                            <img src="${item.urlToImage}" class="card-img-top" alt="...">
                                <div class="card-body">
                                    <h5 href=${item.url} class="card-title">${item.title}</h5>

                                    <p class="card-text" style="font-size: 15px">
                                        ${item.content}    
                                    </p>

                                    <p class="card-text" style="font-size: 15px">
                                        By: ${item.author}
                                    </p>

                                    <p class="card-text" style="font-size: 15px">
                                        Published on: ${item.publishedAt}
                                    </p>
                                </div>
                        </div>
                    </div>`)}
            </div>
        </h1>

        <nav class="pagination-container" aria-label="Page navigation example">
            <ul class="pagination">
                
                <li class="page-item">
                    <a class="page-link" href="#" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                        <span class="sr-only">Previous</span>
                    </a></li>

                <li class="page-item"><button class="page-link">1</a></li>
                <li class="page-item"><button class="page-link">2</a></li>
                <li class="page-item"><button class="page-link" href="#">3</a></li>
                <li class="page-item">
                    <a class="page-link" href="#" aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                        <span class="sr-only">Next</span>
                    </a>
                </li>
            </ul>
        </nav>
    `

    return el
}