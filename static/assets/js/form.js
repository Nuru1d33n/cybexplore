function openForm() {
    console.log('Clock');
    document.getElementById("form-container").classList.add("show");
    document.getElementById("form").classList.add("show");

    // document.getElementById('body').classList
}

function closeForm() {
    document.getElementById("form-container").classList.remove("show");
    document.getElementById("form").classList.remove("show");
}



const RateNum = document.querySelector('.rateD').innerText;
console.log(RateNum)


for (let i = 0; i < RateNum; i++) {
    console.log('Num :> '+ i);
    document.querySelector('.set').innerText = "<span class='bi bi-star-fill'></span>";
}


