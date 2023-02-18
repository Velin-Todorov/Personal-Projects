import { html, render } from 'https://unpkg.com/lit-html?module';
import { repeat } from '../static/node_modules/lit-html/directives/repeat.js'
import { newsApiKey } from './api_key.js';
import { renderArticles} from './newsTemplate.js';

let submit = document.querySelector('#submit')

let apiKey = newsApiKey()
let current_page = 1
let items_per_page = 9


submit.addEventListener('click', getArticles)

async function getArticles(){

    const searchTerm = document.querySelector('#searchBar').value

    const url = `https://newsapi.org/v2/everything?q=${searchTerm}&apiKey=${apiKey}`

    const response = await fetch(url)

    if (!response.ok){
        throw new Error('Something went wrong with fetching your resources')
    }

    const data = await response.json()
    let totalResults = data['totalResults']
    let articles = data['articles']


    render(renderArticles(
        displayList(articles, items_per_page, current_page), totalResults), 

        document.querySelector('#content')
        )



    function displayList(items, items_per_page, page){
        page--;

        let start = items_per_page * page
        let end = start + items_per_page
        let paginatedItems = items.slice(start, end)

        function pagination(items, wrapper, items_per_page) {
            wrapper.innerHTML = '';
            let page_count = Math.ceil(items.length / items_per_page);

            for (let i = 1; i < page_count + 1; i++){
                let btn = PaginationButton(i, items);
                wrapper.appendChild(btn); 
            }
        }

        function PaginationButton(page, items){

            let button = document.createElement('button');
            let li = document.createElement('li')
            li.classList.add('page-item')

            button.innerText = page;

            if (current_page == page) {
                button.classList.add('active');
            }
            
            button.classList.add('page-link')

            button.addEventListener('click', function() {
                current_page = page;

                render(renderArticles(
                    displayList(articles, items_per_page, current_page), totalResults), 
            
                    document.querySelector('#content')
                    )
            })

            li.appendChild(button)
            return li
        }


        pagination(items, document.querySelector('#pageNumbers'), items_per_page)
        return paginatedItems
    }

}


