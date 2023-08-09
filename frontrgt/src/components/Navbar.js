import React from "react"
import {Link} from "react-router-dom"

export const Navbar = () => (
    <nav className="navbar navbar-expand-lg bg-danger">
        <div className="container-fluid">
            <Link className="navbar-brand text-white" to="/Prueba">
                Prueba C.
            </Link>
            <button
                className="navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarNav"
                aria-controls="navbarNav"
                aria-expanded="false"
                aria-label="Toggle navigation"
            >
                <span className="navbar-toggler-icon" />
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav">
                    <li className="nav-item">
                        <Link className="nav-link text-white" aria-current="page" to="/Home">
                            Formulario
                        </Link>
                    </li>
                </ul>
                <ul className="navbar-nav">
                    <li className="nav-item">
                        <Link className="nav-link text-white" aria-current="page" to="/Registro">
                            Panel administrador
                        </Link>
                    </li>
                </ul>
             </div>
        </div>
    </nav>

)