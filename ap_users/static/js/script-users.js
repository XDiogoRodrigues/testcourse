const url = window.location.href

if(url === 'http://31.97.82.101:8000/udemy-create-login' || url === 'http://31.97.82.101:8000/udemy-login'){
    window.addEventListener('resize', () => {

        let width = window.innerWidth
        if (width <= 992){
            let image = document.querySelector('.image') 
            image.src = '../static/images/mobile.webp'

        }else{
            let image = document.querySelector('.image')
            image.src = '../static/images/desktop.webp'
        }
    
    })

}