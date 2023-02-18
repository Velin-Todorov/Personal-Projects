import { html, render } from 'https://unpkg.com/lit-html?module';
import { repeat } from './node_modules/lit-html/directives/repeat.js'

export function renderArticles(data, totalResults){
    
    let el = html`
        <h1> ${totalResults} result/s found</h1>

        <br>
        <div class="row m-5">
            ${data.map((item) => html`
                <div class="col-md-5 offset-md-3" style="align-items: center">
                    <div class="card border-dark mb-5 card text-dark">
                        <img src="${item.urlToImage}" style="aspect-ratio: 1 / 1; object-fit:cover;">
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


    `
    return el
}

