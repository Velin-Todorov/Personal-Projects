import { weatherApiKey } from "./api_key.js";

let submit = document.querySelector('#weatherApi')
submit.addEventListener('click', getLocationKey) 



async function getLocationKey(){

    let apiKey = weatherApiKey()
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

    if (data.length == 0){
        
    }


    console.log(data)

}

function returnWeatherData(){
    


}    

// returnWeatherData()

// let data = await getLocationKey()
// console.log(data)


// async function getWeatherData(){
//    const data = await getLocationKey()

//    const cityKey = data[0]['Key']

    

// }
