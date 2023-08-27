
import React, { useState } from "react"
import "bootstrap/dist/css/bootstrap.css";


import { StepOne } from "./StepOne";
import { StepTwo } from "./StepTwo";
// import { StepThree } from "./components/StepThree";
import { StepThree } from "./StepThree";
import { ImageCarousel } from './ImageCarousel';

export const Home = () => {
  const [step, setStep] = useState(2);
  const [selectedIdType, setSelectedIdType] = useState("");
  const [name, setName] = useState("");
  const [foundClient, setFoundClient] = useState(false);
  const [clientData, setClientData] = useState(null);
  const [id, setId] = useState(null);

  return (
    <div className="container d-flex">
      <div className="row d-flex">
        <div className="col-md-5">
          <ImageCarousel />
        </div>
        <div className="col-md-1"></div> {/* Espacio entre carrusel y pasos */}

        <div className="col-md-6">

          {step === 1 && (

            <StepOne
              setStep={setStep}
              setSelectedIdType={setSelectedIdType}
              setFoundClient={setFoundClient}
              setClientData={setClientData}
              setId={setId}
            />
          )}
          {step === 2 && (
            <StepTwo
              name={name}
              setName={setName}
              setStep={setStep}
              selectedIdType={selectedIdType}
              foundClient={foundClient}
              clientData={clientData}
              id={id}
            />
          )}
          {step === 3 && <StepThree name={name} setStep={setStep} />}
        </div>
      </div>
    </div>
  );
};


