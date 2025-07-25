if(window.location.href === 'http://31.97.82.101:8000/udemy-cart'){
        window.addEventListener('resize', () => {
        let width = window.innerWidth
        let value_total = document.querySelector('#value_total')

        if(width <= 600){
            value_total.classList.remove('w-50')
            value_total.classList.add('w-75')

        }else{
            value_total.classList.remove('w-75')
            value_total.classList.add('w-50')

        }
    

    })

}

if(window.location.href === 'http://31.97.82.101:8000/udemy-service-teach'){
    const informatios = document.querySelectorAll('.action')

    const curricular = document.querySelector('.container-curricular')
    curricular.style.display = 'flex'

    const active = document.querySelector('.active-information')
    active.style.color = 'black'
    active.style.fontWeight = 'bold'

   

    informatios.forEach((element) => {
        let actions = document.querySelectorAll('.action')
        element.addEventListener('click', () => {
            const containerCurricular = document.querySelector('.container-curricular')
            const containerVideo = document.querySelector('.container-video')
            const containerCourse = document.querySelector('.container-course')

          if(element.innerText.toLowerCase() === 'planeje sua grade curriculuar'){
            containerCurricular.style.display = 'flex'
            containerVideo.style.display = 'none'
            containerCourse.style.display = 'none'
            actions[1].style.color = null
            actions[1].style.fontWeight = null
            actions[2].style.color = null
            actions[2].style.fontWeight = null

          } else if(element.innerText.toLowerCase() === 'grave seu vídeo'){
            containerVideo.style.display = 'flex'
            containerCurricular.style.display = 'none'
            containerCourse.style.display = 'none'
            actions[0].style.color = null
            actions[0].style.fontWeight = null
            actions[2].style.color = null
            actions[2].style.fontWeight = null
            
           
          }else if(element.innerText.toLowerCase() === 'lance seu curso'){
            containerCourse.style.display = 'flex'
            containerVideo.style.display = 'none'
            containerCurricular.style.display = 'none'
            actions[0].style.color = null
            actions[0].style.fontWeight = null
            actions[1].style.color = null
            actions[1].style.fontWeight = null
           
          }
          element.style.color = 'black'
          element.style.fontWeight = 'bold'
        })    
    })
}
