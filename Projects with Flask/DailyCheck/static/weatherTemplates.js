import { html, render } from 'https://unpkg.com/lit-html?module';
import { repeat } from '../static/node_modules/lit-html/directives/repeat.js'
import { getForecastData } from './weather.js'


export function nothingFound() {
    let el = html`
        <h1>No results</h1>
    `
    return el
}


export function renderWeatherData(forecast, info, city, country) {

    const weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

    const data = info[0]
    
    let date = new Date()
    let time = data['LocalObservationDateTime']

    let regex = /(?<=T)\d+:\d+/g;
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
                                Visibility: ${data['Visibility']['Metric']['Value']}${data['Visibility']['Metric']['Unit']}
                            </p>
                        </div>
                </div>
            </div>
        </div>
    <h2>
    <hr class="border border-success border-8 opacity-75">
    <h2>Forecast for the next 5 days
        <div class="row m-5">
            <div class="col" style="max-width: 410px; height: 450px;">
                <div class="card">
                    <img src="https://media.istockphoto.com/id/1291592209/vector/calendar-day-1-number-one.jpg?s=170667a&w=0&k=20&c=d0LHJ9mAhMcXglz5HmYQVsNBzZ_5h4YKKz9RrU5LAd4=" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h3 class="card-title">${new Date(forecast['DailyForecasts'][0]['Date']).toLocaleDateString('en-GB')}</h3>
                            <p class="card-text" style="font-size: 15px">
                                Minimum temperature: ${forecast['DailyForecasts'][0]['Temperature']['Minimum']['Value']}${forecast['DailyForecasts'][0]['Temperature']['Minimum']['Unit']}
                            </p>
                            <p class="card-text" style="font-size: 15px">
                                Real feel minimum temperature: ${forecast['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value']}${forecast['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Unit']}
                            </p>
                            <p class="card-text" style="font-size: 15px">
                                Maximum temperature:  ${forecast['DailyForecasts'][0]['Temperature']['Maximum']['Value']}${forecast['DailyForecasts'][0]['Temperature']['Maximum']['Unit']}
                            </p>
                            <p class="card-text" style="font-size: 15px">
                                Real feel maximum temperature: ${forecast['DailyForecasts'][0]['RealFeelTemperature']['Maximum']['Value']}${forecast['DailyForecasts'][0]['RealFeelTemperature']['Maximum']['Unit']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                During the day: ${forecast['DailyForecasts'][0]['Day']['LongPhrase']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                During the night: ${forecast['DailyForecasts'][0]['Night']['LongPhrase']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Chances of rain during the day: ${forecast['DailyForecasts'][0]['Day']['RainProbability']}%
                            </p>
                            <p class="card-text" style="font-size: 15px">
                                Chances of rain during the day: ${forecast['DailyForecasts'][0]['Night']['RainProbability']}%
                            </p>
                        </div>
                </div>
            </div>
            
            <div class="col" style="max-width: 410px; height: 450px;">
                <div class="card">
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4sZfuqFk3eCgYTmdNMzbndDJKuXn_tSWQ4LNFkt3y0Jxr5-_bHmW1S3s9UwR1qNq5W80&usqp=CAU" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h3 class="card-title">${new Date(forecast['DailyForecasts'][1]['Date']).toLocaleDateString('en-GB')}</h3>

                            <p class="card-text" style="font-size: 15px">
                                Minimum temperature: ${forecast['DailyForecasts'][1]['Temperature']['Minimum']['Value']}${forecast['DailyForecasts'][1]['Temperature']['Minimum']['Unit']}
                            </p>
                            <p class="card-text" style="font-size: 15px;">
                                Real feel minimum temperature: ${forecast['DailyForecasts'][1]['RealFeelTemperature']['Minimum']['Value']}${forecast['DailyForecasts'][1]['RealFeelTemperature']['Minimum']['Unit']}
                            </p>
                            
                            <p class="card-text" style="font-size: 15px">
                                Maximum temperature:  ${forecast['DailyForecasts'][1]['Temperature']['Maximum']['Value']}${forecast['DailyForecasts'][1]['Temperature']['Maximum']['Unit']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Real feel maximum temperature: ${forecast['DailyForecasts'][1]['RealFeelTemperature']['Maximum']['Value']}${forecast['DailyForecasts'][1]['RealFeelTemperature']['Maximum']['Unit']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                During the day: ${forecast['DailyForecasts'][1]['Day']['LongPhrase']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                During the night: ${forecast['DailyForecasts'][1]['Night']['LongPhrase']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Chances of rain during the day: ${forecast['DailyForecasts'][1]['Day']['RainProbability']}%
                            </p>
                                
                            <p class="card-text" style="font-size: 15px">
                                Chances of rain during the day: ${forecast['DailyForecasts'][1]['Night']['RainProbability']}%
                            </p>

                        </div>
                </div>
            </div>

            <div class="col" style="max-width: 410px; height: 450px;">
                <div class="card">
                    <img src="https://thumbs.dreamstime.com/b/vector-icon-calendar-day-number-th-month-days-illustration-flat-style-date-week-year-sunday-monday-tuesday-wednesday-207522124.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h3 class="card-title">${new Date(forecast['DailyForecasts'][2]['Date']).toLocaleDateString('en-GB')}</h3>

                            <p class="card-text" style="font-size: 15px">
                                Minimum temperature: ${forecast['DailyForecasts'][2]['Temperature']['Minimum']['Value']}${forecast['DailyForecasts'][2]['Temperature']['Minimum']['Unit']}\n
                            </p>
                                
                            <p class="card-text" style="font-size: 15px">
                                Real feel minimum temperature: ${forecast['DailyForecasts'][2]['RealFeelTemperature']['Minimum']['Value']}${forecast['DailyForecasts'][2]['RealFeelTemperature']['Minimum']['Unit']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Maximum temperature:  ${forecast['DailyForecasts'][2]['Temperature']['Maximum']['Value']}${forecast['DailyForecasts'][2]['Temperature']['Maximum']['Unit']}\n
                            </p>
                                
                            <p class="card-text" style="font-size: 15px">
                                Real feel maximum temperature: ${forecast['DailyForecasts'][2]['RealFeelTemperature']['Maximum']['Value']}${forecast['DailyForecasts'][2]['RealFeelTemperature']['Maximum']['Unit']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                During the day: ${forecast['DailyForecasts'][2]['Day']['LongPhrase']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                During the night: ${forecast['DailyForecasts'][2]['Night']['LongPhrase']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Chances of rain during the day: ${forecast['DailyForecasts'][2]['Day']['RainProbability']}%
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Chances of rain during the day: ${forecast['DailyForecasts'][2]['Night']['RainProbability']}%
                            </p>
                        </div>
                </div>
            </div>

            <div class="col" style="max-width: 410px; height: 450px;">
                <div class="card">
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2BS60qXh4QcxWoX4UQax--p8NC8YdPTb0zw&usqp=CAU" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h3 class="card-title">${new Date(forecast['DailyForecasts'][3]['Date']).toLocaleDateString('en-GB')}</h3>
                            <p class="card-text" style="font-size: 15px">
                                Minimum temperature: ${forecast['DailyForecasts'][3]['Temperature']['Minimum']['Value']}${forecast['DailyForecasts'][3]['Temperature']['Minimum']['Unit']}
                            </p>
                                
                            <p class="card-text" style="font-size: 15px">
                                Real feel minimum temperature: ${forecast['DailyForecasts'][3]['RealFeelTemperature']['Minimum']['Value']}${forecast['DailyForecasts'][3]['RealFeelTemperature']['Minimum']['Unit']}
                            </p>
                            
                            <p class="card-text" style="font-size: 15px">
                                Maximum temperature:  ${forecast['DailyForecasts'][3]['Temperature']['Maximum']['Value']}${forecast['DailyForecasts'][3]['Temperature']['Maximum']['Unit']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Real feel maximum temperature: ${forecast['DailyForecasts'][3]['RealFeelTemperature']['Maximum']['Value']}${forecast['DailyForecasts'][3]['RealFeelTemperature']['Maximum']['Unit']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                During the day: ${forecast['DailyForecasts'][3]['Day']['LongPhrase']}
                            </p>
                                
                            <p class="card-text" style="font-size: 15px">    
                                During the night: ${forecast['DailyForecasts'][3]['Night']['LongPhrase']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Chances of rain during the day: ${forecast['DailyForecasts'][3]['Day']['RainProbability']}%
                            </p>
                                
                            <p class="card-text" style="font-size: 15px">    
                                Chances of rain during the day: ${forecast['DailyForecasts'][3]['Night']['RainProbability']}%
                            </p>

                        </div>
                </div>
            </div>
            
            <div class="col" style="max-width: 410px; height: 450px;">
                <div class="card">
                    <img src="https://thumbs.dreamstime.com/z/calendar-day-number-five-white-paper-red-border-blue-background-vector-calendar-day-number-five-204813762.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h3 class="card-title">${new Date(forecast['DailyForecasts'][4]['Date']).toLocaleDateString('en-GB')}</h3>

                            <p class="card-text" style="font-size: 15px">
                                Minimum temperature: ${forecast['DailyForecasts'][4]['Temperature']['Minimum']['Value']}${forecast['DailyForecasts'][4]['Temperature']['Minimum']['Unit']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Real feel minimum temperature: ${forecast['DailyForecasts'][4]['RealFeelTemperature']['Minimum']['Value']}${forecast['DailyForecasts'][4]['RealFeelTemperature']['Minimum']['Unit']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Maximum temperature:  ${forecast['DailyForecasts'][4]['Temperature']['Maximum']['Value']}${forecast['DailyForecasts'][4]['Temperature']['Maximum']['Unit']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Real feel maximum temperature: ${forecast['DailyForecasts'][4]['RealFeelTemperature']['Maximum']['Value']}${forecast['DailyForecasts'][4]['RealFeelTemperature']['Maximum']['Unit']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                During the day: ${forecast['DailyForecasts'][4]['Day']['LongPhrase']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                During the night: ${forecast['DailyForecasts'][4]['Night']['LongPhrase']}
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Chances of rain during the day: ${forecast['DailyForecasts'][4]['Day']['RainProbability']}%
                            </p>

                            <p class="card-text" style="font-size: 15px">
                                Chances of rain during the day: ${forecast['DailyForecasts'][4]['Night']['RainProbability']}%
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