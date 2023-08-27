import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.css";
import logoGKFC from "./images/logoGKFC.png";


const API = process.env.REACT_APP_API;

export const StepTwo = ({ setStep, selectedIdType, setName, clientData }) => {
    const [formData, setFormData] = useState({
        name: "",
        lastname: "",
        d_i: "",
        cel: "",
        email: "",
        address: "",
        acceptPromotions: "",
    });
    const [message, setMessage] = useState("");
    const [queryResult, setQueryResult] = useState(null);
    const [selectedType, setSelectedType] = useState("Cédula");
    const [id, setId] = useState("");


    const handleQuery = async () => {
        if (formData.d_i) {
            try {
                const response = await fetch(`${API}/consulta/${formData.d_i}`);
                if (response.status === 200) {
                    const data = await response.json();
                    setQueryResult(data); // Almacenar el resultado de la consulta
                    setId(data.datos._id); // Almacenar el resultado de la consulta
                    console.log(id);
                    console.log();
                    console.log(data);
                    setMessage(""); // Limpiar el mensaje de error
                } else {
                    setQueryResult(null); // Limpiar el resultado en caso de error
                    setMessage("No se encontraron datos para el documento ingresado.");
                }
            } catch (error) {
                console.error("Error en la consulta:", error);
                setQueryResult(null);
                setMessage("Cliente no encontrado");
            }
        }
    };

    useEffect(() => {
        handleQuery();
    }, [formData.d_i]); // Ejecutar la consulta cuando cambie el valor de "d_i"

    // ...




    const handleNextStep = async () => {
        if (
            formData.name &&
            formData.lastname &&
            formData.d_i &&
            formData.cel &&
            formData.email &&
            formData.acceptPromotions
        ) {
            let response;
            if (id) {
                // Si clientData tiene un valor, usar método PUT
                response = await fetch(`${API}/clients/${id}`, {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(formData),
                });
            } else {
                // Si clientData está vacío, usar método POST
                response = await fetch(`${API}/clients`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(formData),
                });
            }

            if (response.status === 200) {
                setName(formData.name); // Guardar el nombre para mostrar en el paso 3
                setStep(3);
            } else {
                setMessage("Hubo un problema al enviar los datos.");
            }


        } else {
            // Mostrar mensaje de que faltan campos por completar
            setMessage("Completa todos los campos antes de continuar.");
        }
    };

    return (

        <div className="border border-3 border-danger rounded h-100 ">
            <div className="card card-doby p-4 container" style={{ height: '700px' }}>
                <div className="d-flex justify-content-center">
                    <img src={logoGKFC} className="w-25" alt="Logo de formulario" />
                </div>
                {/* <div className="d-flex justify-content-center">
                    <img src={paso2} className="w-75" alt="paso2" />
                </div> */}
                {/* <h2>Paso 2: Ingresar datos</h2> */}
                {clientData ? (
                    <div>
                        <p>¡<b>Hola de nuevo, </b>{clientData}!</p>
                    </div>
                ) : (
                    <div className="d-flex justify-content-between">
                        <h6><b>Información de tu cuenta</b></h6>
                        
                        {/* <h6>Campos Obligatorios*</h6> */}
                    </div>
                )}

                <div className="d-flex justify-content-center py-2">
                    <div className="btn-group" role="group" aria-label="Basic radio toggle button group">
                        <input
                            type="checkbox"
                            className="btn-check"
                            name="btnradio"
                            id="btnradio1"
                            autocomplete="off"
                            value="Cédula"
                            checked={selectedType === "Cédula"}
                            onChange={() => setSelectedType("Cédula")}
                            defaultChecked
                        />
                        <label class="btn btn-outline-primary" for="btnradio1"> Cédula</label>


                        <input
                            type="checkbox"
                            className="btn-check"
                            name="btnradio"
                            id="btnradio3"
                            autocomplete="off"
                            value="Pasaporte"
                            checked={selectedType === "Pasaporte"}
                            onChange={() => setSelectedType("Pasaporte")}
                        />
                        <label class="btn btn-outline-primary" for="btnradio3">Pasaporte</label>
                    </div>
                </div>

                <div className="form-group py-2">
                    <input
                        type="number"
                        onChange={(e) =>
                            setFormData({ ...formData, d_i: e.target.value })
                        }
                        value={formData.d_i}
                        className="form-control"
                        placeholder="Documento de Identidad"
                        required
                    />
                </div>
                {/* {!formData.d_i && (
                        <small className="text-danger">Este campo es requerido.</small>
                    )} */}

                {/* {queryResult && (
                            <div>
                                <h6>Resultado de la consulta:</h6>
                                <pre>{JSON.stringify(queryResult, null, 2)}</pre>
                            </div>
                        )} */}
                {message && (
                    <small className="text-danger">{message}</small>
                )}
                <div className="row">

                    <div className="col-md-6">
                        <div className="form-group py-2">
                            <input
                                type="text"
                                onChange={(e) =>
                                    setFormData({ ...formData, name: e.target.value })
                                }
                                value={formData.name}
                                className="form-control"
                                placeholder="Nombre"
                                required
                            />
                        </div>
                        {/* {!formData.name && (
                            <small className="text-danger">Este campo es requerido.</small>
                        )} */}
                    </div>
                    <div className="col-md-6">
                        <div className="form-group py-2">
                            <input
                                type="text"
                                onChange={(e) =>
                                    setFormData({ ...formData, lastname: e.target.value })
                                }
                                value={formData.lastname}
                                className="form-control"
                                placeholder="Apellido"
                                required
                            />
                        </div>
                        {/* {!formData.lastname && (
                            <small className="text-danger">Este campo es requerido.</small>
                        )} */}
                    </div>
                </div>
                
                        <div className="form-group py-2">
                            <input
                                type="number"
                                onChange={(e) => setFormData({ ...formData, cel: e.target.value })}
                                value={formData.cel}
                                className="form-control"
                                placeholder="Celular"
                                required
                            />
                        </div>
                        {/* {!formData.cel && (
                            <small className="text-danger">Este campo es requerido.</small>
                        )} */}

                    
                        <div className="form-group py-2">
                            <input
                                type="email"
                                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                                value={formData.email}
                                className="form-control"
                                placeholder="Correo"
                                required
                            />
                        </div>
                        {/* {!formData.email && (
                            <small className="text-danger">Este campo es requerido.</small>
                        )} */}
                 

                <div className="form-group py-2">
                    <div className="form-check">
                        <input
                            type="checkbox"
                            value="Terminos y condiciones"
                            required
                            onChange={(e) =>
                                setFormData({ ...formData, acceptPromotions: e.target.checked })
                            }
                            checked={formData.acceptPromotions}
                            className="form-check-input"
                        />
                        <label className="form-check-label" htmlFor="acceptTermsCheckbox">
                            Acepto los <b>términos y condiciones</b>, considerando las políticas de la
                            empresa.
                        </label>
                    </div>
                    <div className="form-check">
                        <input
                            type="checkbox"
                            value="Terminos y condiciones"
                            required
                            onChange={(e) =>
                                setFormData({ ...formData, acceptPromotions: e.target.checked })
                            }
                            checked={formData.acceptPromotions}
                            className="form-check-input"
                        />
                        <label className="form-check-label" htmlFor="acceptTermsCheckbox">
                            Conozco y acepto el uso de mis datos.
                        </label>
                    </div>
                    {/* {!formData.acceptPromotions && (
                        <small className="text-danger">Debe aceptar los términos y condiciones.</small>
                    )} */}
                </div>
                <button onClick={handleNextStep} className="btn btn-danger btn-block">
                    Registrarme
                </button>
                {message && <b><p className={message === "Campos completos" ? "text-success" : "text-danger "}>{message}</p></b>}
            </div>
        </div>

    );
};