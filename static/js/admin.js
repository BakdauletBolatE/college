// function ajaxnewSend(url,paremetres){
// 	fetch(url+paremetres)
// 	.then(response => response.json())
// 	.then(data => console.log(data))

// }

// const statForm = document.querySelectorAll('.stat');

// if (statForm){
// 	statForm.forEach(form=>{
// 		form.addEventListener('submit',function(e){
// 			e.preventDefault();
// 			let url = this.action;
// 			const group = this.querySelector('select[name="group"]').value
// 			const subject = this.querySelector('select[name="subject"]').value
// 			const cemester = this.querySelector('select[name="cemester"]').value
// 			paremetres = `?group=${group}&subject=${subject}&cemester=${cemester}`
// 			ajaxnewSend(url,paremetres);
// 		})
// 	})
// }