// import { useEffect, useState } from "react";
// import Construct from "./Construct.js";
// import ErrorNotification from "./ErrorNotification";
// import "./App.css";

// function App() {
//   const [launch_info, setLaunchInfo] = useState([]);
//   const [error, setError] = useState(null);

//   useEffect(() => {
//     async function getData() {
//       let url = `${process.env.REACT_APP_API_HOST}/api/launch-details`;
//       console.log("fastapi url: ", url);
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
//   }, []);

//   return (
//     <div>
//       <ErrorNotification error={error} />
//       <Construct info={launch_info} />
//     </div>
//   );
// }

// export default App;

import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
// import Nav from "./Nav";
import SignUpModal from "./SignUpModal";
import LogInModal from "./LogInModal";
import UserList from "./UserList";
import Chat from "./Chat.js";
import MainPage from "./MainPage";
import "./index.css";

function App() {
  return (
    <BrowserRouter>
      <div className="container">
        <Routes>
          <Route path="/users/new" element={<SignUpModal />} />
          <Route path="/users" element={<UserList />} />
          <Route path="/login" element={<LogInModal />} />
          <Route path="/chat" element={<Chat />} />
          <Route path="/main" element={<MainPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
