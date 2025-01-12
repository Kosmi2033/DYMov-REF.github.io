let tg = window.Telegram.WebApp;
let button = document.getElementById("button");
tg.expand();

button.addEventListener("click", () => {
    document.getElementById("user_name").value = tg.initDataUnsafe.user.first_name; 
})
// document.getElementById("user_name").value = tg.initDataUnsafe.user.first_name;