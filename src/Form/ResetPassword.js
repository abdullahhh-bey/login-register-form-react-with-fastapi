import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import apiCall from "./api/axios";
import "./Form.css";

function ResetPassword() {
  const [token, setToken] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!token || !newPassword) {
      alert("Please fill all fields!");
      return;
    }

    try {
      const response = await apiCall.post("/new-password", {
        token,
        new_password: newPassword,
      });

      alert(response.data || "Password reset successfully!");
      navigate("/login")
    } catch (error) {
      console.error(error);
      alert("Invalid token or server error!");
    }
  };

  return (
    <div className="second-container">
      <div className="Heading1">
        <h1>Reset Password</h1>
      </div>

      <form className="Input" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter token"
          value={token}
          onChange={(e) => setToken(e.target.value)}
        />
        <br />
        <input
          type="password"
          placeholder="Enter new password"
          value={newPassword}
          onChange={(e) => setNewPassword(e.target.value)}
        />
        <br />
        <button className="btn-login">Reset Password</button>
      </form>

      <p className="back-link" onClick={() => navigate("/login")}>
        Back to Login
      </p>
    </div>
  );
}

export default ResetPassword;
