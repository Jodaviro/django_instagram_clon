
const filledLike = ()=>{
    const response = document.getElementById("filledlike")
    const href = response.href
    fetch (href)
    .then(x => console.log(x))
    .then(y => document.getElementById("demo").innerHTML = y);
    
}


const emptyLike = () => {
    const response = document.getElementById("emptylike")
    const href = response.href
    fetch (href)
    .then(x => console.log(x))
    .then(y => document.getElementById("demo").innerHTML = y);
}
