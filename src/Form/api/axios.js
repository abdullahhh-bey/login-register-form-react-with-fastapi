import axios from "axios";

const apiCall = axios.create({
  baseURL: "http://127.0.0.1:8008/auth",
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiCall;
