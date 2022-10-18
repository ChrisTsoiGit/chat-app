// import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React, { useContext, useEffect, useState } from "react";
import Chat from './components/Chat.js';
// import Register from "./components/Register";
import Login from "./components/Login";
import { UserContext } from "./context/UserContext";

import './index.css';

const App = () => {
  // const [message, setMessage] = useState("");
  const [token] = useContext(UserContext);

  const getWelcomeMessage = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch("/api/accounts", requestOptions);
    const data = await response.json();

    if (!response.ok) {
      console.log("something messed up");
    }
    //  else {
    //   setMessage(data.message);
    // }
  };

  useEffect(() => {
    getWelcomeMessage();
  }, []);

  return (
    
     
    <div className="columns">
    <div className="column"></div>
    <div className="column m-5 is-two-thirds">
      {!token ? (
        <div className="columns">
           <Login />
        </div>
      ) : (
        <Chat />
      )}
    </div>
    <div className="column"></div>
  </div>
    
        );
};

export default App;