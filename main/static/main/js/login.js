let reg = document.getElementById('login_reg');
let log = document.getElementById('login_log');
let rec = document.getElementById('login_rec');
let tit = document.getElementById('login_title');
let sub = document.getElementById('submit');
let psw = document.getElementById('psw1c');
let psw2 = document.getElementById('psw2c');
let num = document.getElementById('type');
let usrc = document.getElementById('usrc');
let emlc = document.getElementById('emlc');
reg.onclick = () => {
    num.value = 0;
    reg.hidden = true;
    log.hidden = false;
    rec.hidden = false;
    tit.innerHTML = 'Регистрация'
    sub.value = 'Зарегистрироваться'
    psw.hidden = false;
    psw2.hidden = false;
    usrc.hidden = false;
    emlc.hidden = false;
};
log.onclick = () => {
    num.value = 1;
    reg.hidden = false;
    log.hidden = true;
    rec.hidden = false;
    tit.innerHTML = 'Вход'
    sub.value = 'Войти'
    psw.hidden = false;
    psw2.hidden = true;
    usrc.hidden = false;
    emlc.hidden = true;
};
rec.onclick = () => {
    num.value = 2;
    reg.hidden = false;
    log.hidden = false;
    rec.hidden = true;
    tit.innerHTML = 'Восстановление'
    sub.value = 'Восстановить'
    psw.hidden = true;
    psw2.hidden = true;
    usrc.hidden = true;
    emlc.hidden = false;
};