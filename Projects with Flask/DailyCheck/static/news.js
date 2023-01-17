import { html, render } from 'https://unpkg.com/lit-html?module';
import { repeat } from '../static/node_modules/lit-html/directives/repeat.js'
import { newsApiKey } from './api_key.js';

let submit = document.querySelector('#submit')
let apiKey = weatherApiKey()

submit.addEventListener('click', getLocationKey)

