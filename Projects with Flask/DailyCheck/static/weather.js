import { weatherApiKey } from "./api_key.js";
import {html, render} from 'https://unpkg.com/lit-html?module';
import { nothingFound, renderWeatherData } from "./templates.js";


let submit = document.querySelector('#weatherApi')
let apiKey = weatherApiKey()

submit.addEventListener('click', getLocationKey) 

async function getLocationKey(){
    let input = document.querySelector('.searchBar').value
    
    let url = `http://dataservice.accuweather.com/locations/v1/cities/search?apikey=${apiKey}&q=${input}&details=false&offset=1`

    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Accept-Encoding': 'gzip',
        }
    })

    if(!response.ok){
        throw new Error('Something went wrong with fetching your resource')
    }

    const data = await response.json()

    getForecastData(data)

}

async function getForecastData(data){
    const info = await data

    if (data.length == 0){
        render(nothingFound(), document.querySelector('#content'))
    }

    const key = info[0]['Key']
    const cityName = info[0]['LocalizedName']
    const country = info[1]['EnglishName']

    const url = `http://dataservice.accuweather.com/forecasts/v1/daily/1day/${key}?apikey=${apiKey}&language=en-us&details=true&metric=true`

    const response = await fetch(url, {
        headers: {
            'Accept-Encoding': 'gzip'
        }
    })

    if (!response.ok){
        throw new Error('Something went wrong with fetching your resource')
    }

    const forecastData = await response.json()

    render(renderWeatherData(forecastData, cityName, country), document.querySelector('#content'))

}


