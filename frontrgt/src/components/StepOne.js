import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.css";
import logoGKFC from "./images/logoGKFC.png";
import paso1 from "./images/paso1.png";


const API = process.env.REACT_APP_API;

export const StepOne = ({ setStep, setFoundClient, setClientData, setId }) => {
  const [selectedType, setSelectedType] = useState("");
  const [searching, setSearching] = useState(false);
  const [formData, setFormData] = useState({ id: "" });
  const [message, setMessage] = useState("");

  
    const handleNextStep = async () => {
      if (selectedType === "" || !formData.id) {
        return;
      }

      setSearching(true);

      try {
        const response = await fetch(`${API}/consulta/${formData.id}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
          
        });
        
        if (response.status === 200) {
          const data = await response.json();
          setFoundClient(true);
          setMessage("Cliente encontrado en la API");
          // setClient(data.datos); //consulta todos los datos (NotFound)
          setClientData(data.datos.name);
          setId(data.datos._id);
          console.log(data.datos._id);
          console.log(data);
          console.log(data.datos.name);
          setStep(2);
        }
         
        
      } catch (error) {
        console.error("Error en la solicitud fetch:", error);
        setMessage("Cliente no encontrado");
        setClientData(""); // Establecer clientData como vacío
        setId(""); // Establecer clientData como vacío
        setStep(2); // Continuar al paso 2 sin datos de client
      }
    
    setSearching(false);
  };

  return (
    <div className="card card-body p-4 border border-3 border-danger rounded container" style={{ height: '700px' }}>
      <div className="d-flex justify-content-center">
          <img src={logoGKFC} className="w-25" alt="Logo de formulario"/>
        </div>
      <div className="d-flex justify-content-center">
          <img src={paso1} className="w-75" alt="paso1"/>
        </div>
      <div>
        {/* <h2>Paso 1: Seleccionar tipo de identificación</h2> */}
        <p><b>¿Quieres ser un beneficiario?</b></p>
      </div>
      <div className="form-group">
        <div className="form-control d-flex justify-content-between">
          <label className="form-check-label">
            
            <b>Pasaporte</b>
          </label>
          <input
            type="checkbox"
            value="Pasaporte"
            checked={selectedType === "Pasaporte"}
            onChange={() => setSelectedType("Pasaporte")}
            className="form-check-input p-2 btn btn-outline-primary"
          />

        </div>

        <div className="py-2">
          <div className="form-control d-flex justify-content-between">
            <label className="form-check-label">
              <b>Cédula</b>
            </label>
            <input
              type="checkbox"
              value="Cédula"
              checked={selectedType === "Cédula"}
              onChange={() => setSelectedType("Cédula")}
              className="form-check-input p-2 btn btn-outline-primary"
            />

          </div>
        </div>

        <div >
          <input
            type="text"
            value={formData.id}
            onChange={(e) => setFormData({ ...formData, id: e.target.value })}
            placeholder="Ingrese el documento de identidad"
            className="form-control"
          />
        </div>
        <br />
      </div>
      {message && <p className={message === "Cliente encontrado en la API" ? "text-success" : "text-danger"}>{message}</p>}
   
      <button onClick={handleNextStep} className="btn btn-danger">
        {searching ? "Buscando..." : "Siguiente"}
      </button>
      {/* <div>
      {!setClientData && (
        <small className="text-danger">Cliente no encontrado. Registrese para ser beneficiario!</small>
    )}
      </div> */}
    </div>
  );
};