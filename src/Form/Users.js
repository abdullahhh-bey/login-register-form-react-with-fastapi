import React, { useEffect, useState } from "react";
import apiCall from "./api/axios.js";
import "./Form.css";

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await apiCall.get("/users");
        console.log(response.data)
        setUsers(response.data);
      } catch (error) {
        console.error("Error fetching users:", error);
      }
    };
    fetchUsers();
  }, []);

  return (
    <div className="Main-container">
      <h1>All Registered Users</h1>
      <div className="row my-4 container-lg d-flex justify-content-center align-items center">
        {users.map((user, index) => (
          <>
          <div key={index} className="col-lg-4 d-flex flex-column text-center" style={{width: "23rem"}}>
            <div className="card-body">
              <h5 className="card-title">{user.name}</h5>
              <p>{user.email}</p>
            </div>
          </div>
          </>
        ))}
      </div>
    </div>
  );
}

export default Users;
