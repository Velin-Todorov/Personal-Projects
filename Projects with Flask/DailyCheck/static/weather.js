import { weatherApiKey } from "./api_key.js";
import {html, render} from 'https://unpkg.com/lit-html?module';
import { nothingFound, renderWeatherData, renderCityOptions } from "./templates.js";


let submit = document.querySelector('#submit')
let apiKey = weatherApiKey()

submit.addEventListener('click', getLocationKey) 

async function getLocationKey(){
    let input = document.querySelector('#searchBar').value
    
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
    render(renderCityOptions(data),  document.querySelector('#content'))

}

export async function getForecastData(ev){

    const key = ev.target.id

    let text = ev.target.textContent.split(', ')

    const url = `http://dataservice.accuweather.com/currentconditions/v1//${key}?apikey=${apiKey}&language=en-us&details=true&metric=true`
    const url2 = `http://dataservice.accuweather.com/forecasts/v1/daily/5day/${key}?apikey=${apiKey}&language=en-us&details=true&metric=true`
    
    const response = await fetch(url, {
        headers: {
            'Accept-Encoding': 'gzip'
        }
    })
    
    const response2 = await fetch(url2, {
        headers: {
            'Accept-Encoding': 'gzip'
        }
    })

    if (!response.ok || !response2.ok){
        throw new Error('Something went wrong with fetching your resource')
    }
    
    const currentData = await response.json()    
    const forecastData = await response2.json()

    console.log(forecastData)

    render(renderWeatherData(forecastData, currentData, text[0], text[1]), document.querySelector('#content'))

}

