import { html, render } from 'https://unpkg.com/lit-html?module';

export function nothingFound() {
    let el = html`
        <h1>No results</h1>
    `
    return el
}


export function renderWeatherData(info, city, country) {

    const weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];

    const data = info
    let date = new Date()

    let regex = /(?<=T)\d+:\d+/g;

    console.log(data)

    let el = html`
        <h1 class="forecast"> Daily Forecast for ${city}, ${country}
            <div class="day">${weekday[date.getDay()]}, ${date.getHours()}:${date.getMinutes()}
            </div>
        </h1>
        
        <div id="forecast">
            <div class="sun">
                <div class="row">
                    <div class="column">
                        <div class="sunCard">
                            <h3>Sun</h3>
                            <p class="sunRise">
                            Sun rose at: ${data['DailyForecasts'][0]['Sun']['Rise'].match(regex)[0]} AM
                            </p>
                            <p class="sunSet">
                            Sun set at: ${data['DailyForecasts'][0]['Sun']['Set'].match(regex)[0]} PM
                            </p>
                        </div>

                        <div class="tempCard">
                            <h3>Temperature</h3>
                            <p class="minTemp">
                                Minimum temperature: ${data['DailyForecasts'][0]['Temperature']['Minimum']['Value']}${data['DailyForecasts'][0]['Temperature']['Minimum']['Value']['Unit']}
                            </p>
                            <p class="maxTemp">
                                Maximum temperature: ${data['DailyForecasts'][0]['Temperature']['Maximum']['Value']}${data['DailyForecasts'][0]['Temperature']['Minimum']['Value']['Unit']}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>`

    return el
}