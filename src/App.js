import React from "react";
import Register from "./Form/Register";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Form/Login";
import Users from "./Form/Users";
import ForgotPassword from "./Form/ForgotPassword";
import ResetPassword from "./Form/ResetPassword";

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/users" element={<Users />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/new-password" element={<ResetPassword />} />

      </Routes>
    </Router>
  );
}
export default App;
