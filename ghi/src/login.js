// import React from 'react';
// import './Modal.css';
// import { useState } from 'react';
// import { useToken } from './Auth';

// function BootstrapInput(props) {
//     const { id, placeholder, labelText, value, onChange, type } = props;

//     return (
//         <div className='mb-4'>
//             <label htmlFor={id} className='form-label'>{labelText}</label>
//             <input value={value} onChange={onChange} type={type} className='form-control' id={id} placeholder={placeholder}></input>
//         </div>
//     );
// }

// function LoginModal({ closeLogin }) {
//     const [email, setEmail] = useState('');
//     const [password, setPassword] = useState('');
//     const [_, login] = useToken();
    

//     return (

//         <div className="modalBackground" id='loginModal'>
//             <div className="modalContainer">
//                 <div className="titleCloseBtn">
//                     <button
//                         onClick={() => {
//                             closeLogin(false);
//                         }}
//                     >
//                         X
//                     </button>
//                 </div>
//                 <div className="title">
//                     <h1>Login to your account</h1>
//                 </div>
//                 <form>
//                     <BootstrapInput
//                         id='email'
//                         placeholder='youremail@example.com'
//                         labelText='Your email address'
//                         value={email}
//                         onChange={e => setEmail(e.target.value)}
//                         type='email' />
//                     <BootstrapInput
//                         id='password'
//                         placeholder='Your secret password'
//                         labelText='Password'
//                         value={password}
//                         onChange={e => setPassword(e.target.value)}
//                         type='password' />
//                 </form>
//                 <div className="footer">
//                     <button
//                         onClick={() => {
//                             closeLogin(false);
//                         }}
//                         id="cancelBtn"
//                     >
//                         Cancel
//                     </button>
//                     <button
//                         onClick={() => {
//                             login(email, password);
//                             setPassword('')
//                             setEmail('')
//                         }} type='submit' className='btn btn-primary'>Submit</button>
//                 </div>
//             </div>
//         </div>
//     );
// }


// export default LoginModal;


