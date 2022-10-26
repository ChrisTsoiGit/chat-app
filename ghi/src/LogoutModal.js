// import React from 'react';
// import { useToken } from './Auth';


// function LogoutModal({ closeLogout, closeSignup, closeLogin }) {
//     const [,, logout] = useToken();


//     return (

//         <div className="modalBackground" id='loginModal'>
//             <div className="modalContainer">
//                 <div className="titleCloseBtn">
//                     <button
//                         onClick={() => {
//                             closeLogout(false);
//                             closeSignup(false);
//                             closeLogin(false);
//                         }}
//                     >
//                         X
//                     </button>
//                 </div>
//                 <div className="title">
//                     <h1>Are you sure you want to logout?</h1>
//                 </div>
//                 <div className="footer">
//                     <button
//                         onClick={() => {
//                             closeLogout(false);
//                             closeSignup(false);
//                             closeLogin(false);
//                         }}
//                         id="cancelBtn"
//                     >
//                         Cancel
//                     </button>
//                     <button
//                         onClick={() => {
//                             logout();
//                         }} type='submit' className='btn btn-primary'>Logout</button>
//                 </div>
//             </div>
//         </div>
//     );
// }


// export default LogoutModal;
