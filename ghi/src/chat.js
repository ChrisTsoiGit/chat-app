import React from 'react';
import { useLazyGetTokenQuery } from './app/api';
import { useEffect, useState } from 'react'


function MessageRow(props) {
  const when = new Date(props.message.timestamp);
  return (
    <tr>
      <td>{props.message.username}</td>
      <td>{when.toLocaleString()}</td>
      <td>{props.message.content}</td>
    </tr>
  )
}

const Chat = () => {
  const [messages, setMessages] = useState([])
  // const [connected, setConnected] = useState(false)
  const [message, setMessage] = useState('')
  // const [loading, setLoading] = useState(true)
  const [trigger] = useLazyGetTokenQuery()
  const [socket, setSocket] = useState(null)
  const [username, setUsername] = useState("")
  const [data, setData] = useState(false)

  useEffect(()=>{
    async function fetchData() {
      const tokenPromise = trigger().unwrap();
      tokenPromise.then((data) => {
        setUsername(data.account.username)
        const token = data["access_token"];
        console.log("this is token", token)
        // const url = `ws://localhost:8000/chat`;
        const url = "wss://newchat-heroku.herokuapp.com/chat";
        // const url = `${process.env.WEBSOCKET_HOST}/chat`
        const fullurl = url + "?token=" + token;
        const ws = new WebSocket(fullurl);
        setSocket(ws)
        setData(true)
        return ws

      }).then((resp)=>{


        resp.addEventListener('message', message => {
          setMessages(current => 
            [...current, JSON.parse(message.data)]
          );
          
        });
      })
      
    
  }
  fetchData()
  // window.location.reload()
  },[trigger]);


  const sendMessage = (e) =>{
    e.preventDefault();
    socket.send(message);
    setMessage('');
  }

  const updateMessage = (e) => {
    setMessage(e.target.value);
  }

  return (
    <>
    {data ? (<>
      <><h1>Chat Room</h1><h2>Your Username: {username}</h2><h2>Messages</h2><div className="container mt-4">
      <div className="card mx-auto" style={{ background: '400 px' }}>

        <table className="table">
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
    </div><form onSubmit={sendMessage}>
        <input value={message}
          className="form-control "
          aria-label="Large"
          type="text"
          id="messageText"
          autoComplete="off"
          onChange={updateMessage} />

        <button disabled={!sendMessage}
          className="btn btn-outline-warning">
          Send
        </button>

      </form></> 
    </>) : (<></>)}
    </>
      
    )
  }


export default Chat;