import { html, render } from 'https://unpkg.com/lit-html?module';
import { repeat } from '../static/node_modules/lit-html/directives/repeat.js'
import { newsApiKey } from './api_key.js';
import { renderArticles } from './newsTemplate.js';

let submit = document.querySelector('#submit')

let apiKey = newsApiKey()

submit.addEventListener('click', getArticles)

async function getArticles(){

    const searchTerm = document.querySelector('#searchBar').value

    const url = `https://newsapi.org/v2/everything?q=${searchTerm}&apiKey=${apiKey}`

    const response = await fetch(url)

    if (!response.ok){
        throw new Error('Something went wrong with fetching your resources')
    }

    const data = await response.json()
    
    render(renderArticles(data), document.querySelector('#content'))

}


export function pagination(){

    let data = document.getElementsByClassName('col')
    console.log(data)
}

pagination()

