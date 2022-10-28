import { useLogOutMutation } from './app/api';
import { useNavigate } from "react-router-dom";

function Nav() {
  // const [openLogin, setOpenLogin] = useState(false)
  // const [openLogout, setOpenLogout] = useState(false)
  const [logOut] = useLogOutMutation();

    let logOutNavigate = useNavigate();
      const LogoutChange = (e) =>{
        // console.log("this is e", new FormData(e.target))
        e.preventDefault()
        logOut(e.target)
        let path = `/login`;
        logOutNavigate(path);
      }

      let logInNavigate = useNavigate();
      const LoginChange = (e) =>{
        e.preventDefault()
        let path = `/login`;
        logInNavigate(path);
      }

      let signupNavigate = useNavigate();
      const signupChange = (e) =>{
        e.preventDefault()
        let path = `/signup`;
        signupNavigate(path);
      }

      let homeNavigate = useNavigate();
      const homeChange = (e) =>{
        e.preventDefault()
        let path = `/`;
        homeNavigate(path);
      }

      let chatNavigate = useNavigate();
      const chatChange = (e) =>{
        e.preventDefault()
        let path = `/chat`;
        chatNavigate(path);
      }
  
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-secondary">     
      <div className="navbar-brand">
      <button className="btn btn-outline-warning " onClick={homeChange} type="button">Home </button>
      </div>
      <div className="navbar-brand">
      <button className="btn btn-outline-warning " onClick={LoginChange} type="button">LogIn </button>
      </div>
      <div className="navbar-brand">
      <button className="btn btn-outline-warning " onClick={signupChange} type="button">SignUp </button>
      </div>
      <div className="navbar-brand">
      <button className="btn btn-outline-warning" onClick={chatChange} type="button">  ChatRoom </button>
      </div>
      <div className="navbar-brand">
      <button className="btn btn-outline-warning" onClick={LogoutChange} type="button">  Logout </button>
      </div>
    </nav>

  );
};

export default Nav;
