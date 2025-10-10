import React, { useState } from "react";
import { useNavigate } from "react-router-dom"; 
import apiCall from "./api/axios.js";
import "./Form.css";

function Login() {
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");
  const navigate = useNavigate(); 

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (email && pass) {
      try {
        const response = await apiCall.post("/login", {
          email,
          password: pass,
        });

        console.log("Login successful:", response.data);
        // ✅ After successful login, redirect to /users
        navigate("/users");
      } catch (error) {
        console.error("Login failed:", error);
        alert("Invalid credentials. Please try again!");
      }
    } else {
      alert("Please fill all fields!");
    }
  };

  return (
    <div className="second-container">
      <div className="Heading1">
        <h1>Welcome Back</h1>
      </div>

      <form className="Input" onSubmit={handleSubmit}>
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          type="email"
          placeholder="Email"
        />
        <br />
        <input
          value={pass}
          onChange={(e) => setPass(e.target.value)}
          type="password"
          placeholder="Password"
        />
        <br />
        <button className="btn-login">Login</button>
      </form>
      <p className="forgot-pass link-register" onClick={() => navigate("/forgot-password")}>
        Forgot Password?
      </p>

      <p>
        Don’t have an account?{" "}
        <span className="link-register" onClick={() => navigate("/register")}>
          Register
        </span>
      </p>

    </div>
  );
}

export default Login;
