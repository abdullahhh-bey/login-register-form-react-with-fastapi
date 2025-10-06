import React, { useState } from "react";
import { useNavigate } from "react-router-dom";  
import apiCall from "./api/axios.js";
import "./Form.css";

function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");
  const [status, setStatus] = useState("");
  const navigate = useNavigate(); 


  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (name && email && pass) {
      try {
        const response = await apiCall.post("/register", {
          name,
          email,
          password: pass,
        });

        console.log("Server response:", response.data);
        setStatus("success");
        setName("");
        setEmail("");
        setPass("");
        
      } catch (error) {
        console.error("Registration error:", error);
        setStatus("error");
      }
    } else {
      alert("Please fill all fields!");
    }
  };

  if (status === "success") {
    return (
      <div className="Main-container">
        <h1 className="success-text">🎉 User Successfully Registered!</h1>
        <button className="btn-login" onClick={() => navigate("/")}>
          Go to Login
        </button>
      </div>
    );
  }

  if (status === "error") {
    return (
      <div className="Main-container">
        <h1 className="error-text">❌ Error registering user. Try again!</h1>
        <button className="btn-register" onClick={() => setStatus("")}>
          Try Again
        </button>
      </div>
    );
  }

  return (
    <div className="Main-container">
      <div className="Heading1">
        <h1>Create an Account</h1>
      </div>

      <form className="Input" onSubmit={handleSubmit}>
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          type="text"
          placeholder="Full Name"
        />
        <br />
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
        <button className="btn-register">Register</button>
      </form>

      <p>
        Already have an account?{" "}
        <span className="link-login" onClick={() => navigate("/")}>
          Log in
        </span>
      </p>
    </div>
  );
}

export default Register;
