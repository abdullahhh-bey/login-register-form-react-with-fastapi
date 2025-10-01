import React, { useState } from "react";
import { Users } from "./Users";
import "./Form.css";
function Login({ onSwitch }) {
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (email !== "" && pass !== "") {
      const foundUser = Users.find((U) => U.email === email && U.pass === pass);
      if (foundUser) {
        console.log("Login Successfull ✔", foundUser);
      } else {
        console.log("Invalid Information ✖");
      }
      console.log(email, pass);

      setEmail("");
      setPass("");
    } else {
      console.log("Please Fill all fields!");
    }
  };
  return (
    <div>
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
          />{" "}
          <br />
          <input
            value={pass}
            onChange={(e) => setPass(e.target.value)}
            type="password"
            placeholder="Password"
          />{" "}
          <br />
          <button className="btn-login">Login</button>
        </form>
        <div>
          <p>
            Don't have an account?{" "}
            <span className="link-register" onClick={onSwitch}>
              Register
            </span>
          </p>
        </div>
      </div>
    </div>
  );
}
export default Login;
