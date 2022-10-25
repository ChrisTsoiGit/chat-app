import { NavLink } from "react-router-dom";


function Nav() {
  // const { user, logoutUser } = useContext(AuthContext);
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-secondary">
      
      <div className="navbar-brand">
      <button className="btn btn-outline-warning " type="button">Home </button>
      <button className="btn btn-outline-warning " type="button">LogIn </button>
      <button className="btn btn-outline-warning" type="button">LogOut </button>
      <button className="btn btn-outline-warning" type="button">SignUp </button>
      </div>


    </nav>
  );
};

export default Nav;

