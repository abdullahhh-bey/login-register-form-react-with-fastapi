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
      <ul>
        {users.map((user, index) => (
          <li key={index}>
            <strong>{user.name}</strong> — {user.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Users;
