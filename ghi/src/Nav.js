// import { NavLink } from 'react-router-dom';
// import { useLazyGetTokenQuery, useLogOutMutation } from './app/api';
// import { useDispatch } from 'react-redux';
// import { useNavigate } from 'react-router-dom';
// import { showModal, LOG_IN_MODAL, SIGN_UP_MODAL } from './app/accountSlice';
// import LogInModal from './LoginModal';
// import SignUpModal from './SignUpModal';
// import { useEffect } from 'react';


// function LoginButtons(props) {
//   const dispatch = useDispatch();
//   const classNames = `buttons ${props.show ? '' : 'is-hidden'}`;

//   return (
//     <div className={classNames}>
//       <button onClick={() => dispatch(showModal(SIGN_UP_MODAL))} className="button is-primary">
//         <strong>Sign up</strong>
//       </button>
//       <button onClick={() => dispatch(showModal(LOG_IN_MODAL))} className="button is-light">
//         Log in
//       </button>
//     </div>
//   );
// }

// function LogoutButton() {
//   const navigate = useNavigate();
//   const [logOut, { data }] = useLogOutMutation();

//   useEffect(() => {
//     if (data) {
//       navigate('/');
//     }
//   }, [data, navigate]);

//   return (
//     <div className="buttons">
//       <button onClick={logOut} className="button is-light">
//         Log out
//       </button>
//     </div>
//   );
// }


function Nav() {
  
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-secondary">     
      <div className="navbar-brand">
      <button className="btn btn-outline-warning " type="button">Home </button>
      <button className="btn btn-outline-warning " type="button">LogIn </button>
      <button className="btn btn-outline-warning" type="button" >LogOut </button>
      <button className="btn btn-outline-warning" type="button">SignUp </button>
      </div>
    </nav>

  );
};

export default Nav;

