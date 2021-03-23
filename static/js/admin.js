function ajaxnewSend(url,data){
	fetch(url)
	.then(response => response.json())
	.then(data => console.log(data))

}

const statForm = document.querySelectorAll('.stat');

if (statForm){
	statForm.forEach(form=>{
		form.addEventListener('submit',function(e){
			e.preventDefault();
			let url = this.action;
			const form = this.parentElement;
            console.log(form)
			const group = this.querySelector('select[name="group"]').value
			const subject = this.querySelector('select[name="subject"]').value
			const cemester = this.querySelector('select[name="cemester"]').value
			const data = new FormData()
			data.append('group',group)
			data.append('subject',subject)
			data.append('cemester',cemester)
			ajaxnewSend(url,data);
		})
	})
}