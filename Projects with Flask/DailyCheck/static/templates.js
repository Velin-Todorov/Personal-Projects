import { html, render} from 'https://unpkg.com/lit-html?module';
import { repeat } from '../static/node_modules/lit-html/directives/repeat.js'
import {getForecastData} from './weather.js'


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
        <h1 class="forecast" > Daily Forecast for ${ city }, ${ country }
            <div class="day" > ${ weekday[date.getDay()] }, ${ date.getHours() }:${ date.getMinutes() }
            </div>
        </h1>

        <div id="forecast">
            <div class="container text-center">
                <div class="row">
                    <div class="col">
                        <h3>Sun</h3>
                        <p>
                            Sun rose at: ${data['DailyForecasts'][0]['Sun']['Rise'].match(regex)[0]} AM
                        </p>
                        <p>
                            Sun set at: ${data['DailyForecasts'][0]['Sun']['Set'].match(regex)[0]} PM
                        </p>
                    </div>
                    <div class="col">
                        <h3>Temperature</h3>
                        <p>
                            Minimum temperature: ${data['DailyForecasts'][0]['Temperature']['Minimum']['Value']} ${data['DailyForecasts'][0]['Temperature']['Minimum']['Unit']}
                        </p>
                        <p>
                            Maximum temperature: ${data['DailyForecasts'][0]['Temperature']['Maximum']['Value']} ${data['DailyForecasts'][0]['Temperature']['Minimum']['Unit']}
                        </p>
                    </div>
                    <div class="col">
                        <h3>Real Feel Temperature</h3>
                        <p>
                            Minimum: ${data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value']} ${data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Unit']}
                        </p>
                        <p>
                            Maximum: ${data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value']} ${data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Unit']}
                        </p>
                    </div>
                
                    <div class="col">
                        <h3>Air Quality</h3>
                        <p>${data['DailyForecasts'][0]['AirAndPollen'][0]['Category']}</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <h3>Test col</h3>
                    </div>
                    <div class="col">
                        <h3>Test col</h3>
                    </div>
                    <div class="col">
                        <h3>Test col</h3>
                    </div>
                    <div class="col">
                        <h3>Test col</h3>
                    </div>
                </div>
            </div>
        </div>`

    return el
}

export function renderCityOptions(data){
    let el = html`
        <h1 class="forecast">${data.length} result/s found</h1>
        ${repeat(data, (item) => html`
            <button id="${item['Key']}" class="button-3" @click="${getForecastData}">${item['EnglishName']}, ${item['Country']['LocalizedName']}</button>
        `)}`

    return el
}