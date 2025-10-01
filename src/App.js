import React, { useState } from "react";
import Register from "./Form/Register";
import Login from "./Form/Login";

function App() {
  const [page, setPage] = useState("register");

  return (
    <div>
      {page === "register" ? (
        <Register onSwitch={() => setPage("login")} />
      ) : (
        <Login onSwitch={() => setPage("register")} />
      )}
    </div>
  );
}
export default App;
