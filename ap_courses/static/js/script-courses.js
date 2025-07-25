const url = window.location.href


let items = document.querySelectorAll('.carousel-item')

items[0].classList.add('active')

if(url === 'http://31.97.82.101:8000/create-course'){
    const detail_input = document.querySelector('#detailed_description')
    
    detail_input.addEventListener('keydown', (event) => {
        print(event.key)
        if(event.key == 'Enter'){
            event.preventDefault();
            detail_input.value += "\n";
            return false
        }

    })
}








