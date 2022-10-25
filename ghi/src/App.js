// import { useEffect, useState } from 'react';
// import Construct from './Construct.js'
// import ErrorNotification from './ErrorNotification';
// import './App.css';

// function App() {
//   const [launch_info, setLaunchInfo] = useState([]);
//   const [error, setError] = useState(null);  

//   useEffect(() => {
//     async function getData() {
//       let url = `${process.env.REACT_APP_API_HOST}/api/launch-details`;
//       console.log('fastapi url: ', url);
//       let response = await fetch(url);
//       console.log("------- hello? -------");
//       let data = await response.json();

//       if (response.ok) {
//         console.log("got launch data!");
//         setLaunchInfo(data.launch_details);
//       } else {
//         console.log("drat! something happened");
//         setError(data.message);
//       }
//     }
//     getData();
//   }, [])


//   return (
//     <div>
//       <ErrorNotification error={error} />
//       <Construct info={launch_info} />
//     </div>
//   );
// }

// export default App;
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Chat from './chat.js';
import SignUpModal from './SignUpModal';
import './index.css';
import LogInModal from './LoginModal';
import "bootstrap/dist/css/bootstrap.min.css";
import Nav from './Nav';
import Footer from './Footer'



function App() {
  return (
    <BrowserRouter>
    <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/chat" element={<Chat/>} />
          <Route path="/login" element={<LogInModal/>} />
          <Route path="/signup" element={<SignUpModal/>} />

        </Routes>
      </div>
    {/* <Footer /> */}
    </BrowserRouter>
  );
}

export default App;
