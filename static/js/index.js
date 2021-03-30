const section = document.querySelectorAll('.section');

const subsection = document.getElementById('subsection');
const specializationid = document.getElementById('specializationid');
const quaid = document.getElementById('quaid');


const speciliazationurl = 'http://185.146.3.237/speciliazation';

let loading = false;

async function getResourse(url){

    data = await fetch(url);

    return  await data.json()

}

function getAllSubSections(){
    return getResourse(`${speciliazationurl}/subsection/`)
}

function getSubSectionById(id){
    return getResourse(`${speciliazationurl}/subsection/${id}`)
}

function getSpecilaztionById(id){
    return getResourse(`${speciliazationurl}/specialization/${id}`)
}

function getQualificationById(id){
    return getResourse(`${speciliazationurl}/qualification/${id}`)
}



section.forEach(section => {
    section.addEventListener('click', (e)=>{
        id = e.target.getAttribute('data-id');
        specializationid.innerHTML = "";
        quaid.innerHTML = "";
        getSubSectionById(id)
        .then( res => render(res.data))  
    })
})

function render(data){
    subsectiondata = "";
    data.map(item =>{
        subsectiondata += `
        <li class="subsection" data-id="${item.id}"> ${item.uid} ${item.name}</li> 
    `
    })
    subsection.innerHTML = subsectiondata; 
    
    const speciliazation = document.querySelectorAll('.subsection');

    speciliazation.forEach(section => {
        section.addEventListener('click', (e)=>{
            id = e.target.getAttribute('data-id');
            quaid.innerHTML = "";
            getSpecilaztionById(id)
            .then( res => renderS(res.data)) 

            function renderS(data){
                subsectiondata = "";
                data.map(item =>{
                    subsectiondata += `
                    <li class="specialzization" data-id="${item.id}"> ${item.uid} ${item.name}</li> 
                `
                })
                specializationid.innerHTML = subsectiondata; 

                const qualiv = document.querySelectorAll('.specialzization');

                qualiv.forEach( q => {
                    q.addEventListener('click', (e) => {
                        id = e.target.getAttribute('data-id');
                        getQualificationById(id)
                        .then( res => renderQ(res.data) )

                        function renderQ(data){
                            subsectiondata = "";
                            data.map(item =>{
                                subsectiondata += `
                                <li class="qualiv" data-id="${item.id}"> ${item.uid} ${item.name}</li> 
                            `
                            })
                            quaid.innerHTML = subsectiondata; 
                        }
                    })
                })
            }
        })
    })



}


