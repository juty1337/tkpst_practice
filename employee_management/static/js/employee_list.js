
function setEmployeeAccount(employeeId, employeeName, element) {
    const adminUrl = `/admin/employees/employee/${employeeId}/change/`;
    const inputField = document.getElementById("employee-account");
    
    inputField.value = employeeName;  
    inputField.setAttribute('data-url', adminUrl);  

    const details = element.parentElement.nextElementSibling;  
    const arrow = element.querySelector(".arrow");

   
    const allDetails = document.querySelectorAll(".employee-details");
    const allArrows = document.querySelectorAll(".employee-name .arrow");

    allDetails.forEach((detail) => {
        if (detail !== details) {
            detail.style.display = "none"; 
        }
    });

    allArrows.forEach((arrowElement) => {
        if (arrowElement !== arrow) {
            arrowElement.textContent = "▶";
        }
    });

    if (details.style.display === "none" || details.style.display === "") {
        details.style.display = "block";
        arrow.textContent = "▼"; 
    } else {
        details.style.display = "none";
        arrow.textContent = "▶";  
    }
}


function openAdminPanel() {
    const inputField = document.getElementById("employee-account");
    const adminUrl = inputField.getAttribute('data-url'); 

    if (adminUrl) {
        window.open(adminUrl, "_blank"); 
    } else {
        alert("Пожалуйста, выберите сотрудника для редактирования.");
    }
}
 
  function createNewEmployee() {
    const newEmployeeUrl = "/admin/employees/employee/add"; 
    window.open(newEmployeeUrl, "_blank"); 
}