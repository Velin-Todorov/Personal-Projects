import { html, render } from 'https://unpkg.com/lit-html?module';
import { repeat } from '../static/node_modules/lit-html/directives/repeat.js'
import { newsApiKey } from './api_key.js';

let submit = document.querySelector('#submit')
let apiKey = weatherApiKey()

submit.addEventListener('click', getArticles)

async function getArticles(){

    const searchTerm = document.querySelector('#searchBar').value
    const url = `https://newsapi.org/v2/everything?q=${searchTerm}&apiKey=${newsApiKey}`

    const request = await fetch(url)

    const response = await request.json()

    console.log(response)

}