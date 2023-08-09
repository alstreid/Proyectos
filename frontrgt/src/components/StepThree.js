import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import logoGKFC from "./images/logoGKFC.png";
import paso3 from "./images/paso3.png";
import checkPaso3 from "./images/checkPaso3.png";

export const StepThree = ({ name, setStep }) => {


  return (
    <div className="border border-3 border-danger rounded">
      <div className="card card-doby p-4 container" style={{ height: '700px' }}>
        <div className="d-flex justify-content-center">
          <img src={logoGKFC} className="w-25" alt="Logo de formulario" />
        </div>
        <div className="d-flex justify-content-center">
          <img src={paso3} className="w-75" alt="paso3" />
        </div>
        {/* <h2>Paso 3: Confirmación</h2> */}
        <p>Nos vemos <b>{name}</b>!!</p>
        <div className="d-flex justify-content-center p-4">
          <img src={checkPaso3} className="w-75" alt="Check Paso3" />
        </div>
        <div className="d-flex justify-content-center">
          <button
          type="button"
          className="btn btn-danger w-50"
          onClick={() => setStep(1)}>
          Aceptar</button>
        </div>
          <div >
            
          </div>
      </div>
    </div>


  );
};