import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import apiCall from "./api/axios";
import "./Form.css";

function ForgotPassword() {
  const [email, setEmail] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!email) {
      alert("Please enter your email!");
      return;
    }

    try {
      const response = await apiCall.post("/forgot-password",  {email});
      alert("Verification token sent to your email!");
      console.log(response.data);
      navigate("/new-password");
    } catch (error) {
      console.log(error.message);
      alert(`${error.message}. Please try again!`);
    }
  };

  return (
    <div className="second-container">
      <div className="Heading1">
        <h1>Forgot Password</h1>
      </div>

      <form className="Input" onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <br />
        <button className="btn-login">Send Verification</button>
      </form>

      <p className="back-link" onClick={() => navigate("/login")}>
        Back to Login
      </p>
    </div>
  );
}

export default ForgotPassword;
