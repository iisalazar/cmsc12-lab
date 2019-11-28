let form = document.getElementById('orderForm');


const showAlert = msg => {
    alert(msg);
}

const getName = () => {
    const [ el ] = document.getElementsByName('name');
    const { value } = el
    if(value !== '') return value
    else showAlert('Name should not be blank');
}

const getNumber = () => {
    const [ el ] = document.getElementsByName('mobile');
    const { value } = el;
    if( Number.isInteger( parseInt(value, 10) ) ) return value;
    else showAlert('Invalid phone number');
}

const getEmail = () => {
    const [ el ] = document.getElementsByName('email');
    const { value } = el
    if(value !== '') return value
    else showAlert('E-mail should not be blank');
}

const getFlavor = () => {
    const el = document.getElementById('flavors');
    const { value } = el;
    return value;
}

const getSize = () => {
    const els = document.getElementsByName('size');
    let value = '';
    for(let i = 0; els[i] !== undefined; i++){
        if(els[i].checked){
            value = els[i].value;
            break
        }
    }
    return value;
}


const getToppings = () => {
    const els = document.getElementsByName('toppings');
    let toppings = [];
    for(let i = 0; els[i] !== undefined; i++){
        if(els[i].checked){
            toppings.push(els[i].value);
        }
    }
    console.log(toppings.join())
    return toppings.join();
}

const getDelDate = () => {
    const el = document.getElementById('delDate');
    const inputDate = new Date(el.value);
    const date = new Date();
    const today = new Date(`${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`);
    if( inputDate < today ){
        showAlert('Please add a date not lower than today');
        return
    }
    return inputDate;
}

const getDelTime = () => {
    const el = document.getElementById('delTime')
    const [hour, min] = el.value.split(':');
    const inputTime = new Date();
    const current = new Date();
    inputTime.setHours( Number(hour), Number(min) );
    if( inputTime < current ) {
        showAlert('Delivery time should be later than current time');
    }
    else return inputTime;
}

const getDelAdddress = () => {
    const el = document.getElementById('delAddress');
    if(el.value === '') {
        showAlert('Delivery Address should not be blank');
    }
    else return el.value;
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log("SUBMIT!!!");
    const name = getName();
    const email = getEmail();
    const number = getNumber();
    const flavor = getFlavor();
    const size = getSize();
    const toppings = getToppings();
    const delDate = getDelDate();
    const delTime = getDelTime();
    const delAddress = getDelAdddress();
    if(name !== undefined && email !== undefined && number !== undefined){
        showAlert(`Name: ${name}\nMobile: ${number}\nE-mail: ${email}\nFlavor: ${flavor}\nSize: ${size}\nToppings: ${toppings}\nDel. Date: ${delDate}\nDel. Time: ${delTime}\nDel. Address: ${delAddress}`);
    }
})