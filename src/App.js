import React, { useState } from "react";
import Register from "./Form/Register";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Form/Login";
import Users from "./Form/Users";

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/users" element={<Users />} />
      </Routes>
    </Router>
  );
}
export default App;
