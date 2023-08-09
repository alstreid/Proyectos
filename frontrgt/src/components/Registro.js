
import React, { useState, useEffect } from "react"

const API = process.env.REACT_APP_API;

export const Registro = () => {

    const [name, setName] = useState('');
    const [lastname, setLastname] = useState('');
    const [d_i, setDi] = useState('');
    const [cel, setCel] = useState('');
    const [email, setEmail] = useState('');
    const [address, setAddress] = useState('')
    const [acceptPromotions, setAcceptPromotions] = useState('')

    const [edit, setEdit] = useState(false);
    const [id, setId] = useState('');
    const [clients, setClients] = useState([])


    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!edit) {
            const response = await fetch(`${API}/clients`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name,
                    lastname,
                    d_i,
                    cel,
                    email,
                    address,
                    acceptPromotions
                })
            })
            const data = await response.json();
            console.log(data)
        } else {
            const response = await fetch(`${API}/clients/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name,
                    lastname,
                    d_i,
                    cel,
                    email,
                    address,
                    acceptPromotions,
                })
            })
            const data = await response.json();
            console.log(data)
            setEdit(false);
            setId('');

        }

        await getClients();
        setName('');
        setLastname('');
        setDi('');
        setCel('');
        setEmail('');
        setAddress('');
        setAcceptPromotions('');

    }

    const getClients = async () => {
        const response = await fetch(`${API}/clients`)
        const data = await response.json();

        setClients(data)
        console.log(data)
    }

    useEffect(() => {
        getClients();
    }, [])

    const updateClient = async (id) => {
        const response = await fetch(`${API}/clients/${id}`)
        const data = await response.json();
        console.log(data)

        setEdit(true);
        setId(id)

        setName(data.datos.name)
        setLastname(data.datos.lastname)
        setDi(data.datos.d_i)
        setCel(data.datos.cel)
        setEmail(data.datos.email)
        setAddress(data.datos.address)
        setAcceptPromotions(data.datos.acceptPromotions)
    }

    const deleteClient = async (id) => {
        const apiresponse = window.confirm('¿Estás seguro de eliminar el cliente?');
        if (apiresponse) {
            const response = await fetch(`${API}/clients/${id}`, {
                method: 'DELETE',
            });
            const data = await response.json();
            console.log(data);
            await getClients();

        }


    }

    return (
        <div className="m-0 row justify-content-center">
            <div className="col-md-6">
                <form onSubmit={handleSubmit} className="card card-body">
                    <div className="row">
                        <div className="col-md-6">
                            <div className="form-group p-2">
                                <input
                                    type="text"
                                    onChange={e => setName(e.target.value)}
                                    value={name}
                                    className="form-control"
                                    placeholder="Nombre"
                                />
                            </div>
                        </div>
                        <div className="col-md-6">
                            <div className="form-group p-2">
                                <input
                                    type="text"
                                    onChange={e => setLastname(e.target.value)}
                                    value={lastname}
                                    className="form-control"
                                    placeholder="Apellido"
                                />
                            </div>
                        </div>
                    </div>
                    <div className="row">
                        <div className="col-md-6">
                            <div className="form-group p-2">
                                <input
                                    type="number"
                                    onChange={e => setDi(e.target.value)}
                                    value={d_i}
                                    className="form-control"
                                    placeholder="Documento de Identidad"
                                />
                            </div>
                        </div>
                        <div className="col-md-6">
                            <div className="form-group p-2">
                                <input
                                    type="number"
                                    onChange={e => setCel(e.target.value)}
                                    value={cel}
                                    className="form-control"
                                    placeholder="Celular"
                                />
                            </div>
                        </div>
                    </div>
                    <div className="form-group p-2">
                        <input
                            type="email"
                            onChange={e => setEmail(e.target.value)}
                            value={email}
                            className="form-control"
                            placeholder="Correo"
                        />
                    </div>
                    <div className="form-group p-2">
                        <input
                            type="text"
                            onChange={e => setAddress(e.target.value)}
                            value={address}
                            className="form-control"
                            placeholder="Dirección de Domicilio"
                        />
                    </div>
                    <div className="form-group p-2">
                        <input
                            type="checkbox"
                            onChange={e => setAcceptPromotions(e.target.value)}
                            value={acceptPromotions}
                            className="form-check-input"
                        />
                        <label className="form-check-label" htmlFor="acceptTermsCheckbox">Acepto los términos y condiciones, además  de las políticas de la empresa.</label>
                    </div>
                    <button type="submit" className="btn btn-primary btn-block">
                        {edit ? 'Editar' : 'Registrar'}
                    </button>
                </form>
            </div>
            <div className="m-0 mt-5" >
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Nombre</th>
                            <th>Apellido</th>
                            <th>Documento de Identidad</th>
                            <th>Celular</th>
                            <th>Correo</th>
                            <th>Dirección de Domicilio</th>
                            <th>Beneficiario</th>
                            <th>Modificar</th>
                        </tr>
                    </thead>
                    <tbody>
                        {Array.isArray(clients.datos) ? (
                            clients.datos.map((client) => (
                                <tr key={client._id}>
                                    <td>{client.name}</td>
                                    <td>{client.lastname}</td>
                                    <td>{client.d_i}</td>
                                    <td>{client.cel}</td>
                                    <td>{client.email}</td>
                                    <td>{client.address}</td>
                                    <td>{client.acceptPromotions}</td>
                                    <td>
                                        <button className="btn btn-secondary btn-sm btn-block"
                                            onClick={() => updateClient(client._id)}
                                        >
                                            Editar
                                        </button>
                                        <button className="btn btn-danger btn-sm btn-block"
                                            onClick={() => deleteClient(client._id)}
                                        >
                                            Eliminar
                                        </button>
                                    </td>
                                </tr>
                            ))
                        ) : (
                            <tr>
                                <td colSpan="7">Cargando clientes...</td>
                            </tr>
                        )}
                    </tbody>

                </table>
            </div>
        </div>
    )
}