var PacienteHospital = /** @class */ (function () {
    function PacienteHospital(nombres, apellidos, edad, sexo, domicilio, telefono, diagnostico) {
        this.Nombres = nombres;
        this.Apellidos = apellidos;
        this.Edad = edad;
        this.Sexo = sexo;
        this.Domicilio = domicilio;
        this.Telefono = telefono;
        this.Diagnostico = diagnostico;
    }
    PacienteHospital.prototype.MostrarDatosPersonales = function () {
        console.log("Datos Personales del Paciente:");
        console.log("Nombre: ".concat(this.Nombres, " ").concat(this.Apellidos));
        console.log("Edad: ".concat(this.Edad, " a\u00F1os"));
        console.log("Sexo: ".concat(this.Sexo));
        console.log("Domicilio: ".concat(this.Domicilio));
        console.log("Tel\u00E9fono: ".concat(this.Telefono));
    };
    PacienteHospital.prototype.MostrarDatosHospitalarios = function () {
        console.log("Datos Hospitalarios del Paciente:");
        console.log("Diagn\u00F3stico: ".concat(this.Diagnostico));
    };
    return PacienteHospital;
}());
var paciente1 = new PacienteHospital("Juan", "Pérez", 35, "Masculino", "Calle Principal 123", "123-456-7890", "Fractura en el brazo");
paciente1.MostrarDatosPersonales();
paciente1.MostrarDatosHospitalarios();
