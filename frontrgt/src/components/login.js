import React, { useState} from "react"
const API = process.env.REACT_APP_API;

export const Login = () => {

    const [auth, setAuth] = useState(false);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const token = sessionStorage.getItem('token');
    console.log('Tu token: ',token);

    const handleClick = async(e) => {
        e.preventDefault();

        if (!auth) {
            const response = await fetch(`${API}/auth`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username,
                    password
                })
            })
            const data = await response.json();
            sessionStorage.setItem('token',data.token);
            
            setAuth(true)

            const response2 = await fetch(`${API}/token`, {
                method: 'GET', // O el método HTTP que corresponda (GET, POST, PUT, DELETE, etc.)
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${sessionStorage.getItem('token')}` // Agregar el token al encabezado "Authorization"
                }
            });
            
            const data2 = await response2.json();
            console.log(data2);

        }else {
            alert("Ocurrio un problema al iniciar sesión, revisa tus credenciales")}

    }
    return (
        <div className="text-center mt-5">
            <h1>
                Login
            </h1>
            {token && token !== "" && token!=="null" && token !=="undefined" ? (
                    "Has ingresado exitosamente"
                ) : (
            <div>
                <input 
                    type="text"
                    placeholder="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)} />
                    
                <input 
                    type="password"
                    placeholder="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)} />
                <button onClick={handleClick} type="submit">Ingresar</button>
            </div>
            )}
        </div>
    )

}
    