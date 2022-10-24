import { applyMiddleware } from '@reduxjs/toolkit';
import React from 'react';
import { useGetTokenQuery } from './app/api';
import { useEffect, useState } from 'react'


function MessageRow(props) {
  const when = new Date(props.message.timestamp);
  return (
    <tr>
      <td>{props.message.client_id}</td>
      <td>{when.toLocaleString()}</td>
      <td>{props.message.content}</td>
    </tr>
  )
}

const Chat = () => {

  const [messages, setMessages] = useState([])
  const [connected, setConnected] = useState(false)
  const [message, setMessage] = useState('')
  const [loading, setLoading] = useState(true)
  const { data, error, isLoading } = useGetTokenQuery()
  const token = data["access_token"]

  const url = `ws://localhost:8000/chat`;
  const fullurl = url + "?token=" + token
  const socket = new WebSocket(fullurl);

  

  useEffect(()=>{
    function fetchData() {
      

    socket.addEventListener('open', () => {
      setConnected(true);
      setLoading(false);
    });

    socket.addEventListener('close', () => {
      setConnected(false);
      setLoading(false);
    });

    socket.addEventListener('error', () => {
      setConnected(false);
      setLoading(false);
    });

    socket.addEventListener('message', message => {
      setMessages(
        [
          JSON.parse(message.data),
          ...messages,
        ],
      );
    });
  }
  fetchData()
  },[]);


  const sendMessage = () =>{
    socket.send(message);
    setMessage('');
  }

  const updateMessage = (e) => {
    setMessage(e.target.value);
  }

  return (
      <>
        <h1>Chat Room</h1>
        {/* <h2>Your ID: {state.clientId}</h2> */}

        <h2>Messages</h2> 
        <div className="container mt-4">
        <div className="card mx-auto" style={{ background : '400 px' }}>
          
              
        
        <table className="table"  >
          <thead>
            <tr>
              <th>Username</th>
              <th>Date/Time</th>
              <th>Message</th>
            </tr>
          </thead>
          <tbody>
            {messages.map(message => (
              <MessageRow key={message.username + message.timestamp}
                          message={message} />
            ))}
          </tbody>
        </table>
        </div>
        </div>
    

  
        <form onSubmit={sendMessage}>
            <input value={message}
                  className="form-control "
                  type="text"
                  id="messageText"
                  autoComplete="off"
                  onChange={updateMessage}/>
            <button disabled={!connected}
                    className="btn btn-primary">
              Send
            </button>
        </form> 
      </>
    )
  }


export default Chat;