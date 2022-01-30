const menuItems = document.querySelectorAll(".menu-item")
const sidebar = document.querySelector(".left")
const navTog = document.querySelector(".navTog")



function changeActive(){
    menuItems.forEach(item=>{
        item.classList.remove("active")
    })
}
menuItems.forEach(item=>{
    item.addEventListener("click",()=>{
        changeActive()
        item.classList.add("active")
        if(item.id != 'notif'){
            document.querySelector(".notifications-popup").style.display = 'none'
        }else{
            document.querySelector(".notifications-popup").style.display = 'block'
            document.querySelector(".notification-count").style.display = 'none'
        }
    })
})

navTog.addEventListener("click",()=>{
    sidebar.classList.toggle("open")
})