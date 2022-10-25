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
  const [connected, setConnected] = useState(false)
  const [message, setMessage] = useState('')
  const [loading, setLoading] = useState(true)
  const [trigger] = useLazyGetTokenQuery()
  const [socket, setSocket] = useState(null)
  const [username, setUsername] = useState("")

  useEffect(()=>{
    async function fetchData() {
      const tokenPromise = trigger().unwrap();
      tokenPromise.then((data) => {
        setUsername(data.account.username)
        const token = data["access_token"];
        const url = `ws://localhost:8000/chat`;
        const fullurl = url + "?token=" + token;
        const ws = new WebSocket(fullurl);
        setSocket(ws)
        return ws

      }).then((resp)=>{
        console.log("this is the ws", resp)
        resp.addEventListener('open', () => {
          setConnected(true);
          setLoading(false);
        });
    
        resp.addEventListener('close', () => {
          console.log("is closing")
          setConnected(false);
          setLoading(false);
        });
    
        resp.addEventListener('error', () => {
          setConnected(false);
          setLoading(false);
        });
    

        resp.addEventListener('message', message => {
          setMessages(current => 
            [...current, JSON.parse(message.data)]
          );
          
        });
      })

    
  }
  fetchData()
  },[]);


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
        <h1>Chat Room</h1>
        <h2>Your Username: {username}</h2>

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
            <button disabled={!sendMessage}
                    className="btn btn-primary">
              Send
            </button>
        </form> 
      </>
    )
  }


export default Chat;