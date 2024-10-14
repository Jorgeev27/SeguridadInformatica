document.getElementById('passwordForm').addEventListener('submit', function (e) {
    e.preventDefault();

    /** 
     * Obtiene los valores del formulario (longitud, mayúsculas, minúsculas, números y símbolos)
    */
    const length = parseInt(document.getElementById('length').value);
    const includeUppercase = document.getElementById('uppercase').checked;
    const includeLowercase = document.getElementById('lowercase').checked;
    const includeNumbers = document.getElementById('numbers').checked;
    const includeSymbols = document.getElementById('symbols').checked;

    /** 
     * Define los conjuntos de caracteres
    */
    const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lowercaseChars = 'abcdefghijklmnopqrstuvwxyz';
    const numberChars = '0123456789';
    const symbolChars = '!@#$%^&*()_+-=[]{}|;:,.<>?';
    let allChars = '';
    if (includeUppercase) allChars += uppercaseChars;
    if (includeLowercase) allChars += lowercaseChars;
    if (includeNumbers) allChars += numberChars;
    if (includeSymbols) allChars += symbolChars;

    /** 
     * Valida que al menos una opción esté seleccionada
    */
    if (!includeUppercase && !includeLowercase && !includeNumbers && !includeSymbols) {
        alert("Debes seleccionar al menos una opción para generar la contraseña.");
        return;
    }

    /** 
     * Valida la longitud de la contraseña
    */
    if (isNaN(length) || length < 8 || length > 30) {
        alert("La longitud debe ser un número entre 8 y 30");
        location.reload();
        document.getElementById('passwordForm').reset();
        return;
    }

    /**
     * Genera una contraseña aleatoria
     */
    const password = generarContraseña(length, allChars);

    /**
     * Muestra la contraseña aleaoria que se creó
     */
    mostrarResultado(password);
});

/**
 * Genera una contraseña aleatoria basada en la longitud y el conjunto de caracteres proporcionados
 * @param {*} length La longitud de la contraseña
 * @param {*} characters Los caracteres
 * @returns La password
 */
function generarContraseña(length, characters) {
    let password = '';
    const charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
        const randomIndex = crypto.getRandomValues(new Uint32Array(1))[0] % charactersLength;
        password += characters.charAt(randomIndex);
    }
    return password;
}

/**
 * Función para copiar al portapapeles
 * @param {*} text Texto para copiar al portapapeles
 */
function copiarAlPortapapeles(text) {
    navigator.clipboard.writeText(text).then(function () {
        // Opcional: mostrar una notificación de éxito
        alert('Contraseña copiada al portapapeles');
    }, function (err) {
        console.error('Error al copiar al portapapeles: ', err);
    });
}

/**
 * Mostrar el resultado de la password
 * @param {*} password mostrar la password
 */
function mostrarResultado(password) {
    const resultDiv = document.getElementById('result');
    const errorDiv = document.getElementById('error');
    resultDiv.textContent = `Contraseña generada: ${password}`;
    resultDiv.classList.remove('d-none');
    errorDiv.classList.add('d-none');

    // Mostrar el botón de copiar
    const copyButton = document.getElementById('copyButton');
    copyButton.classList.remove('d-none');
    copyButton.onclick = function () {
        copiarAlPortapapeles(password);
    };
}

/**
 * Función para mostrar errores
 * @param {*} mensaje para mostrar los errores
 */
function mostrarError(mensaje) {
    const errorDiv = document.getElementById('error');
    const resultDiv = document.getElementById('result');
    errorDiv.textContent = mensaje;
    errorDiv.classList.remove('d-none');
    resultDiv.classList.add('d-none');

    // Ocultar el botón de copiar
    const copyButton = document.getElementById('copyButton');
    copyButton.classList.add('d-none');
}