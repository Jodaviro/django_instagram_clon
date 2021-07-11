// onclick like or unlike functions

filledLike = (url) =>{
  const unLike = document.getElementsByClassName("filledlike")
  for(node of unLike){
    if(node.dataset.href === url){
      node.className = 'emptylike'
      node.dataset.href = url.slice(0, -4) + 'like/'  
      node.setAttribute('onclick', `emptyLike('${node.dataset.href}')`)
      node.firstElementChild.className = 'far fa-heart' 
      
      window.fetch(url, {
        method: "GET",
        headers: {
          "X-Requested-With": "XMLHttpRequest"
        },
      })
      .then((response) => response.json())
      .then((jsonResponse) => {
        const likesCount = jsonResponse.likes
        const likesDisplay = document.getElementById(node.dataset.href)
  
        if(likesCount > 0){
          likesDisplay.firstElementChild.innerText = likesCount + ' Likes'
        }else{
          likesDisplay.firstElementChild.innerText = NONE
        }
      })
      .catch(error =>{
        console.log('error')
        console.error(error);
      })
    }else{console.log('node not found')}   
  }
};


emptyLike = (url) =>{
  const like = document.getElementsByClassName("emptylike")
  for(node of like){
    if(node.dataset.href === url){
      node.className = 'filledlike'
      node.dataset.href = url.slice(0, -5) + 'rmv/' 
      node.setAttribute('onclick', `filledLike('${node.dataset.href}')`)
      node.firstElementChild.className = 'fas fa-heart'
      node.firstElementChild.id = 'liked'

      window.fetch(url, {
        method: "GET",
        headers: {
          "X-Requested-With": "XMLHttpRequest"
        },
      })
      .then((response) => response.json())
      .then((jsonResponse) => { 
        const likesCount = jsonResponse.likes
        const likesDisplay = document.getElementById(url)
        if(likesCount > 0){
          likesDisplay.firstElementChild.innerText = likesCount + ' Likes'
        }
      })
      .catch(error =>{
        console.log('error')
        console.error(error);
      })
    }else{console.log('node not found')} 
  }
};

