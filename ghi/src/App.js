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
    <Footer />
    </BrowserRouter>
  );
}

export default App;
