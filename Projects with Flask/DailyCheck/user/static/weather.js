import { weatherApiKey } from "./api_key.js";

let apiKey = weatherApiKey()
let input = document.querySelector('.searchBar').textContent
let submit = document.querySelector('#weatherApi')

async function apiCall(){
    let url = ''
}