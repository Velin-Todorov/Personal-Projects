import { html, render } from 'https://unpkg.com/lit-html?module';
import { repeat } from '../static/node_modules/lit-html/directives/repeat.js'
import { getForecastData } from './weather.js'


export function nothingFound() {
    let el = html`
        <h1>No results</h1>
    `
    return el
}


export function renderWeatherData(info, city, country) {

    const weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    const data = info
    let date = new Date()

    let regex = /(?<=T)\d+:\d+/g;

    let el = html`
    <h1>  Daily Forecast for ${ city }, ${ country }
        <div class="day" > ${weekday[date.getDay()]}, ${date.getHours()}:${date.getMinutes()}
        </div>
    </h1>

    <div class="col" style="max-width: 500px; height: 450px;">
        <div class="card">
            <img src="https://assets.website-files.com/5d9ba0eb5f6edb77992a99d0/5de7d426154e7edbf167cce8_Thermometer.gif" class="card-img-top" alt="...">
                <div class="card-body">
                    <h2 class="card-title">Temperature</h2>
                    <p class="card-text">
                        Minimum temperature: ${data['DailyForecasts'][0]['Temperature']['Minimum']['Value']} ${data['DailyForecasts'][0]['Temperature']['Minimum']['Unit']}
                    </p>
                    <p class="card-text">
                        Maximum temperature: ${data['DailyForecasts'][0]['Temperature']['Maximum']['Value']} ${data['DailyForecasts'][0]['Temperature']['Minimum']['Unit']}
                    </p>
                </div>
        </div>
    </div>

    <div class="col" style="max-width: 450px; height: 420px;">
        <div class="card">
            <img src="https://cdn.shopify.com/s/files/1/0605/8550/9029/files/wind.gif?v=1668056359" class="card-img-top" alt="...">
                <div class="card-body">
                    <h2 class="card-title">Real Feel Temperature</h2>
                    <p class="card-text">
                        Minimum: ${data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value']} ${data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Unit']}
                    </p>
                    <p class="card-text">
                        Maximum: ${data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value']} ${data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Unit']}
                    </p>
                </div>
        </div>
    </div>`

    return el
}

export function renderCityOptions(data){
    let el = html`
        <h1 class="forecast" > ${ data.length } result / s found</h1>
            ${
        repeat(data, (item) => html`
            <button id="${item['Key']}" class="button-3" @click="${getForecastData}">${item['EnglishName']}, ${item['Country']['LocalizedName']}</button>
        `)
    } `

    return el
}