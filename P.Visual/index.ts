class PacienteHospital {
    Nombres: string;
    Apellidos: string;
    Edad: number;
    Sexo: string;
    Domicilio: string;
    Telefono: string;
    Diagnostico: string;
  
    constructor(
      nombres: string,
      apellidos: string,
      edad: number,
      sexo: string,
      domicilio: string,
      telefono: string,
      diagnostico: string
    ) {
      this.Nombres = nombres;
      this.Apellidos = apellidos;
      this.Edad = edad;
      this.Sexo = sexo;
      this.Domicilio = domicilio;
      this.Telefono = telefono;
      this.Diagnostico = diagnostico;
    }
  
    MostrarDatosPersonales() {
      console.log(`Datos Personales del Paciente:`);
      console.log(`Nombre: ${this.Nombres} ${this.Apellidos}`);
      console.log(`Edad: ${this.Edad} años`);
      console.log(`Sexo: ${this.Sexo}`);
      console.log(`Domicilio: ${this.Domicilio}`);
      console.log(`Teléfono: ${this.Telefono}`);
    }
  
    MostrarDatosHospitalarios() {
      console.log(`Datos Hospitalarios del Paciente:`);
      console.log(`Diagnóstico: ${this.Diagnostico}`);
    }
  }
  
const paciente1 = new PacienteHospital(
    "Juan",
    "Pérez",
    35,
    "Masculino",
    "Calle Principal 123",
    "123-456-7890",
    "Fractura en el brazo"
  );
  
  paciente1.MostrarDatosPersonales();
  paciente1.MostrarDatosHospitalarios();
  