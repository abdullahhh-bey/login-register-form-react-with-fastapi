import React, { useState } from "react";
import { Users } from "./Users";
import "./Form.css";
function Register({ onSwitch }) {
  const [name, setNAme] = useState("");
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (name !== "" && email !== "" && pass !== "") {
      Users.push({ name, email, pass });
      console.log("Registered Users:", Users);
      setNAme("");
      setEmail("");
      setPass("");
    } else {
      console.log("Please Fill all fields!");
    }
  };
  return (
    <div className="Main-container">
      <div className="Heading1">
        <h1>Create an Account</h1>
      </div>

      <form className="Input" onSubmit={handleSubmit}>
        <input
          value={name}
          onChange={(e) => setNAme(e.target.value)}
          type="text"
          placeholder="Full Name"
        />{" "}
        <br />
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          type="email"
          placeholder="Email"
        />{" "}
        <br />
        <input
          value={pass}
          onChange={(e) => setPass(e.target.value)}
          type="password"
          placeholder="Password"
        />{" "}
        <br />
        <button className="btn-register">Register</button>
      </form>
      <div>
        <p>
          Already have an account?{" "}
          <span className="link-login" onClick={onSwitch}>
            Log in
          </span>
        </p>
      </div>
    </div>
  );
}
export default Register;
