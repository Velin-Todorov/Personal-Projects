function showDetails(){
    let el = event.target.parentElement

    if (event.target.textContent == 'Show Password'){
        adjustDisplay('block')
        event.target.textContent = 'Hide'
    }

    
    else if (event.target.textContent == 'Hide'){
        adjustDisplay('none')
        event.target.textContent = 'Show Password'

    } 


    function adjustDisplay(style){
        el.querySelector('.password').style.display = style
        el.querySelector('.uri').style.display = style
    }

}

