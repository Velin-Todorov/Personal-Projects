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

    const weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

    const data = info[0]
    let date = new Date()
    let time = data['LocalObservationDateTime']

    let regex = /(?<=T)\d+:\d+/g;
    
    let timeRegex = /\d+:\d+/g;
    let hours = time.match(regex)

    console.log(hours[1])
    console.log(hours)

    let el = html`
    <h1>Current conditions and forecast for ${ city }, ${ country }
        <div class="day" >Local Time: ${weekday[date.getDay()]}, ${hours[0]}</div>
    </h1>
    
    <hr class="border border-success border-8 opacity-75">
    <h2>Current Conditions - ${data['WeatherText']}
        <div class="row m-5">
            <div class="col" style="max-width: 500px; height: 450px;">
                <div class="card">
                    <img src="https://assets.website-files.com/5d9ba0eb5f6edb77992a99d0/5de7d426154e7edbf167cce8_Thermometer.gif" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h2 class="card-title">Temperature</h2>
                            <p class="card-text" style="font-size: 15px">
                                Current temperature: ${data['Temperature']['Metric']['Value']} ${data['Temperature']['Metric']['Unit']}
                            </p>
                            <p class="card-text" style="font-size: 15px">
                                Real-feel temperature: ${data['RealFeelTemperature']['Metric']['Value']} ${data['RealFeelTemperature']['Metric']['Unit']}
                        </div>
                </div>
            </div>

            <div class="col" style="max-width: 450px; height: 420px;">
                <div class="card">
                    <img src="https://cdn.shopify.com/s/files/1/0605/8550/9029/files/wind.gif?v=1668056359" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h2 class="card-title">Wind</h2>
                            <p class="card-text" style="font-size: 15px">
                                Speed: ${data['Wind']['Speed']['Metric']['Value']} ${data['Wind']['Speed']['Metric']['Unit']}
                            </p>
                        </div>
                </div>
            </div>

            <div class="col" style="max-width: 450px; height: 420px;">
                <div class="card">
                    <img src="https://services.garmin.cn/appsLibraryBusinessServices_v0/rest/apps/c4c7fb2b-05ba-4b01-9dcd-f19fa2c298b5/icon/bbe3c402-959c-4ca5-91c3-bdbbd8b96efe" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h2 class="card-title">Pressure</h2>
                            <p class="card-text" style="font-size: 15px">
                                Pressure: ${data['Pressure']['Metric']['Value']}${data['Pressure']['Metric']['Unit']}
                            </p>
                            <p class="card-text" style="font-size: 15px">
                                Tendency: ${data['PressureTendency']['LocalizedText']}
                            </p>
                        </div>
                </div>
            </div>

            <div class="col" style="max-width: 450px; height: 420px;">
                <div class="card">
                    <img src="https://media.tenor.com/rX7mEsN3hToAAAAM/water-lww.gif" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h2 class="card-title">Humidity</h2>
                            <p class="card-text" style="font-size: 15px">
                                Humidity: ${data['RelativeHumidity']}%
                            </p>
                            <p class="card-text" style="font-size: 15px">
                                Indoor Relative Humidity: ${data['IndoorRelativeHumidity']}%
                            </p>
                        </div>
                </div>
            </div>

            <div class="col" style="max-width: 450px; height: 420px;">
                <div class="card">
                    <img src="https://www.deliveringinnovation.com/images/InformedVisibility_1.gif" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h2 class="card-title">Visibility</h2>
                            <p class="card-text" style="font-size: 15px">
                                Visibility: ${data['Visibility']['Metric']['Unit']}${data['Visibility']['Metric']['Value']}
                            </p>
                        </div>
                </div>
            </div>
        </div>
    <h2>
    <hr class="border border-success border-8 opacity-75">
    <h2>Forecast for the next 5 days
        <div class="row m-5">
            <div class="col" style="max-width: 500px; height: 450px;">
                <div class="card">
                    <img src="https://assets.website-files.com/5d9ba0eb5f6edb77992a99d0/5de7d426154e7edbf167cce8_Thermometer.gif" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h2 class="card-title">Temperature</h2>
                            <p class="card-text" style="font-size: 15px">
                                Current temperature: ${data['Temperature']['Metric']['Value']} ${data['Temperature']['Metric']['Unit']}
                            </p>
                            <p class="card-text" style="font-size: 15px">
                                Real-feel temperature: ${data['RealFeelTemperature']['Metric']['Value']} ${data['RealFeelTemperature']['Metric']['Unit']}
                            </p>
                        </div>
                </div>
            </div>



        </div>
    </h2>`

    
    return el
}

export function renderCityOptions(data){
    let el = html`
        <h1 class="forecast" > ${ data.length } result/s found

            <ul class="list-group" style="
            list-style: none;">
            ${
        repeat(data, (item) => html`
            <li class="p-3"><button class="btn btn-primary" id="${item['Key']}" @click="${getForecastData}">${item['EnglishName']}, ${item['Country']['LocalizedName']}</button></li>
            </ul>
        </h1>`
        )
        
    } `

    return el
}