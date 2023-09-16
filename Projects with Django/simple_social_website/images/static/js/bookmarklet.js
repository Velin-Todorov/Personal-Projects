const siteUrl = '//127.0.0.1:8000';
const styleUlr = siteUrl + 'static/css/bookmarklet.css';
const minWidth = 250;
const minHeight = 250;

var head = document.getElementsByTagName('head')[0]
var link = document.createElement('link');
link.rel = 'stylesheet'
link.type = 'text/css'
link.href = styleUlr + '?r=' + Math.floor(Math.random()*9999999999)
head.appendChild(link);

var body = document.getElementsByTagName('body')[0];
let boxHtml = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1> Select an image to bookmark:</h1><div class="images"></div></div>'

body.innerHTML += boxHtml


function bookmarkletLaunch(){
    let bookmarklet = document.getElementById('bookmarklet');
    var imagesFound = bookmarklet.querySelector('.images');

    imagesFound.innerHTML = '';
    bookmarklet.style.display = 'blokc';
    bookmarklet.querySelector('#close').addEventListener('click', function(){
        bookmarklet.style.display = 'none'
    });


    let images = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"]');
    images.forEach(image => {
        if(image.naturalWidth >= minHeight){
            let imageFound = document.createElement('img');
            imageFound.src = image.src
            imagesFound.append(imageFound);
        }
    })



    imagesFound.querySelectorAll('img').forEach(image => {
        image.addEventListener('click', (e) => {
            let imgSelected = e.target;
            bookmarklet.style.display = 'none';
            window.open(
                siteUrl + 'images/create/?url='
                + encodeURIComponent(imgSelected.src)
                + '&title='
                +encodeURIComponent(document.title),
                '_blank');
            
        })
    })
    
}

bookmarkletLaunch();