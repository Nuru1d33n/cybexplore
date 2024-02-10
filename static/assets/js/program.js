window.addEventListener('load', () => {
    // function toggleSchoolNameField() {
    //   const inSchoolCheckbox = document.getElementById('id_in_school');
    //   const schoolNameField = document.getElementById('id_school_name');
  
    //   if (inSchoolCheckbox.checked) {
    //       schoolNameField.style.display = 'block';
    //   } else {
    //       schoolNameField.style.display = 'none';
    //   }
    // }
    const NameOfSchlClass = document.querySelector(".id_name_of_school");
    const CheckShl = document.querySelector("#id_are_you_a_student");
    
    // NameOfSchlClass.className = 'no-show';

    CheckShl.addEventListener("click", function() {
        NameOfSchlClass.className = 'no-show' ? 'showDiv' : 'no-show';
        console.log(CheckShl.checked);        
    })

})




