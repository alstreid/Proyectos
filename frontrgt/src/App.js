import React from "react";
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

import { Navbar } from "./components/Navbar";
// eslint-disable-next-line
import { Prueba } from "./components/Prueba";
import { Login } from "./components/login";
import { Registro } from "./components/Registro";
import { Home } from "./components/Home";
import { StepOne } from "./components/StepOne";
import { StepTwo } from "./components/StepTwo";
import { StepThree } from "./components/StepThree";



function App() {
  return (
    <Router>
      <Navbar/>
      <div className="container py-4 ">
      
        <Routes>
          {/* <Route path="/prueba" element={<Prueba/>}/>  */}
          <Route path="/home" element={<Home/>}/>
          <Route path="/registro" element={<Registro/>}/>
          <Route path="/login" element={<Login/>}/>
          <Route path="/prueba" element={<Prueba/>}/>
          <Route path="/StepOne" element={<StepOne/>}/>
          <Route path="/StepTwo" element={<StepTwo/>}/>
          <Route path="/StepThree" element={<StepThree/>}/>
        </Routes>

      </div>

    </Router>
  );
}

export default App;
