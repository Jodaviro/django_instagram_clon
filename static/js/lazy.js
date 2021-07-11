// lazy loading API for post image and profile pic


const isIntersecting = (entry) =>{
	return entry.isIntersecting
};

const loadImage = (entry) =>{
	const image = entry.target
	const url =  image.dataset.src
	image.src = url
	observer.unobserve(image)
};

const observer = new IntersectionObserver((entries)=> {
	entries
		.filter(isIntersecting)
		.forEach(loadImage)
}); 

const registerImg = (image) => {
	observer.observe(image)
};


// Registration of elements 
const profilepic = document.getElementsByClassName('profilepic')
const post = document.getElementsByClassName('post')


for (let node of profilepic){
	registerImg(node)
};

for (let node of post){
	registerImg(node)
};


