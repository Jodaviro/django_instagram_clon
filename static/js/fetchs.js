
filledLike = () =>{
  const likeUrl = document.querySelector("#filledlike");
  fetch (likeUrl.href, {
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest"
    },
  })
  .then((response) => response.json())

  .then((jsonResponse) => {
    console.log(jsonResponse.likes)
  })
  .catch(error =>{
    console.log('error')
    console.error(error);
  })
  
}


// emptyLike = () =>{
//   fetch ('/submit-form', {
//     method: "GET",
//     ...
//     headers: {
//       "X-Requested-With": "XMLHttpRequest"
//     },
//     ...
//   });
// }

