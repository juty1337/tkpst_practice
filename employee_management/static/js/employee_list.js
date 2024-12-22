// Функция для установки информации сотрудника в поле ввода
function setEmployeeAccount(employeeId, employeeName, element) {
    // Формируем URL для редактирования аккаунта
    const adminUrl = `/admin/employees/employee/${employeeId}/change/`;
    const inputField = document.getElementById("employee-account");
    
    // Отображаем имя и фамилию в поле ввода
    inputField.value = employeeName;  
    inputField.setAttribute('data-url', adminUrl);  // Сохраняем URL редактирования как атрибут

    // Переключаем отображение информации о сотруднике
    const details = element.parentElement.nextElementSibling;  // Находим блок с деталями
    const arrow = element.querySelector(".arrow");

    // Переключаем видимость информации о сотруднике
    if (details.style.display === "none" || details.style.display === "") {
        details.style.display = "block";
        arrow.textContent = "▼";  // Стрелка вниз
    } else {
        details.style.display = "none";
        arrow.textContent = "▶";  // Стрелка вправо
    }
}

// Функция для открытия страницы редактирования сотрудника в админпанели
function openAdminPanel() {
    const inputField = document.getElementById("employee-account");
    const adminUrl = inputField.getAttribute('data-url');  // Получаем URL из атрибута

    if (adminUrl) {
        window.open(adminUrl, "_blank");  // Открытие страницы редактирования в новой вкладке
    } else {
        alert("Пожалуйста, выберите сотрудника для редактирования.");
    }
}
