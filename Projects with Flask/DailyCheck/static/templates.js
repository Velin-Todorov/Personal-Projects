import { html, render } from 'https://unpkg.com/lit-html?module';

export function nothingFound() {
    let el = html`
        <h1>No results</h1>
    `
    return el
}


export function renderWeatherData(info, city, country) {

    const data = info

    console.log(info)

    let el = html`
        <h1> Daily Forecast for ${city}, ${country}</h1>
        <div class="day">${new Date()}</div>
        
        <div id="forecast">
            <div class="sun">
                <p class="sunRise">
                    Sun rose at: ${data['DailyForecasts'][0]['Sun']['Rise']}
                </p>

                <p class="sunSet">
                    Sun set at: ${data['DailyForecasts'][0]['Sun']['Set']}
                </p>
            </div>

            <div class="temperature">
                <p class="minTemp">
                    Minimum temperature: ${data['DailyForecasts'][0]['Temperature']['Minimum']['Value']}${data['DailyForecasts'][0]['Temperature']['Minimum']['Value']['Unit']}
                </p>
                
                <p class="maxTemp">
                    Maximum temperature: ${data['DailyForecasts'][0]['Temperature']['Maximum']['Value']}${data['DailyForecasts'][0]['Temperature']['Minimum']['Value']['Unit']}

                </p>
            </div>
        </div>`

    return el
}