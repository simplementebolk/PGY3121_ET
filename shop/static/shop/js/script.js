document.addEventListener('DOMContentLoaded', () => {
    // Selecciona el formulario y el botón "Enviar"
    const form = document.getElementById('formulario-postulacion');

    // Añade un event listener al formulario para manejar el envío
    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Previene el envío del formulario
        if (validarFormulario()) { // Valida el formulario
            form.submit(); // Envía el formulario si es válido
        }
    });

    // Función para validar el formulario
    function validarFormulario() {
        // Obtiene los valores de los campos del formulario
        const rut = document.getElementById('id_rut').value.trim();
        const nombre = document.getElementById('id_nombre').value.trim();
        const direccion = document.getElementById('id_direccion').value.trim();
        const puesto = document.getElementById('id_puesto_empresa').value.trim();
        const genero = document.getElementById('id_sexo').value.trim();
        const celular = document.getElementById('id_telefono').value.trim();
        const profesion = document.getElementById('id_profesion').value.trim();

        // Expresiones para las validaciones
        const textoVal = /^[a-zA-Z\s]+$/;
        const numeroVal = /^\d+$/;

        // Validaciones de cada campo
        if (!rut || rut.length < 9 || rut.length > 10) {
            alert('RUT inválido. Debe tener entre 9 y 10 caracteres y sin punto ni dígito verificador.');
            return false;
        }
        if (!nombre.match(textoVal) || nombre.length < 3 || nombre.length > 20) {
            alert('El nombre debe tener entre 3 y 20 caracteres y solo debe contener letras.');
            return false;
        }
        if (!direccion.match(textoVal) || direccion.length < 3 || direccion.length > 40) {
            alert('Dirección inválida. Debe tener entre 3 y 40 caracteres y solo debe contener letras.');
            return false;
        }
        if (!puesto.match(textoVal) || puesto.length < 3 || puesto.length > 20) {
            alert('Puesto inválido. Debe tener entre 3 y 20 caracteres y solo debe contener letras.');
            return false;
        }
        if (!genero) {
            alert('Debe seleccionar un género.');
            return false;
        }
        if (!celular.match(numeroVal) || celular.length < 9 || celular.length > 12) {
            alert('El celular debe tener entre 9 y 12 caracteres y solo debe contener números.');
            return false;
        }
        if (!profesion.match(textoVal)) {
            alert('Profesión inválida. Solo debe contener letras.');
            return false;
        }

        // Si todo pasa, retorna true
        return true;
    }
});
