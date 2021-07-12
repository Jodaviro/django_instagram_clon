// onclick like or unlike functions
async function onclickFetch(url, postId){
	let response = await window.fetch(url);
	if (!response.ok){
		throw new Error(`HTTP error! status: ${response.status}`);
	}else{
		let jsonResponse = await response.json();
		const likesCount = jsonResponse.likes
    const likesDisplay = document.getElementById(postId)
    
    switch(likesCount){
    	
    	case 0:
    		likesDisplay.removeChild(likesDisplay.firstElementChild)
    		break;
    	
    	case 1:
    		const text = document.createElement('p')
    		text.className = 'fw-light'
    		text.innerText = likesCount + ' Likes'
    		likesDisplay.appendChild(text)
    		break;

    	default:
      likesDisplay.firstElementChild.innerText = likesCount + ' Likes'
		}
	} 
};

filledLike = (url, postId) =>{
  const unLike = document.getElementsByClassName("filledlike")
  for(node of unLike){
    if(node.dataset.href === url){
      node.className = 'emptylike'
      node.dataset.href = url.slice(0, -4) + 'like/'  
      node.setAttribute('onclick', `emptyLike('${node.dataset.href}', ${postId})`)
      node.firstElementChild.className = 'far fa-heart' 
			
			onclickFetch(url, postId)
			.catch(e => {
			console.log('There has been a problem with your fetch operation: ' + e.message);
			})
		}
	}
};

emptyLike = (url, postId) =>{
  const like = document.getElementsByClassName("emptylike")
  for(node of like){
    if(node.dataset.href === url){
      node.className = 'filledlike'
      node.dataset.href = url.slice(0, -5) + 'rmv/' 
      node.setAttribute('onclick', `filledLike('${node.dataset.href}', ${postId})`)
      node.firstElementChild.className = 'fas fa-heart'
      node.firstElementChild.id = 'liked'
      
      onclickFetch(url, postId)
			.catch(e => {
			console.log('There has been a problem with your fetch operation: ' + e.message);
			})
    }
  }
};