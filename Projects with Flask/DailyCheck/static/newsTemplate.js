import { html, render } from 'https://unpkg.com/lit-html?module';
import { repeat } from './node_modules/lit-html/directives/repeat.js'


export function renderArticles(data){
    
    console.log()
    let el = html`
        <h1> ${data.length} result/s found

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
    `

    return el
}