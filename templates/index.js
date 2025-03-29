const btnEL = document.getElementById("submit")

function findRep() {
    let user_zipcode = document.querySelector("#user_zipcode");
    let message = document.querySelector("#repInfo");
    if ( user_zipcode.value.length != 5) {
        message.innerHTML = "Invalid zipcode";
      }
    else {
        message.innerHTML = "[your rep info]";
    }
}

btnEL.addEventListener("click", findRep)