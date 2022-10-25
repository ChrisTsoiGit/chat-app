// import { NavLink } from 'react-router-dom'

function Nav() {
  return (
    <div className="pos-f-t">
  <nav className="navbar navbar-dark bg-dark">
  <li><a className="navbar-brand" href="/">Login</a></li>
  <li><a className="navbar-brand" href="/">SignUp</a></li>
  <a className="navbar-brand" href="/">Logout</a>
</nav>

</div>
    // <nav className="navbar navbar-expand-lg navbar-dark bg-dark" >
    //   <div className="container-fluid">
    //     <NavLink className="navbar-brand" to="/">
    //       {/* < img id="logo" width="100px" height="auto" src={"logo.png"} /> */}
    //     </NavLink>
    //     <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    //       <span className="navbar-toggler-icon"></span>
    //     </button>
    //     <div className="collapse navbar-collapse" id="navbarSupportedContent">
    //       <ul className="navbar-nav me-auto mb-2 mb-lg-0">

    //       <li className="nav-item dropdown">
    //           <p className="nav-link dropdown-toggle" to="#" role="button" data-bs-toggle="dropdown" aria-expanded="false" id="a1">
    //             <b>Login</b>
    //           </p>
    //           <ul className="dropdown-menu">
    //             <li><NavLink className="dropdown-item" to="/manufacturers"> Manufacturers </NavLink></li>
    //           </ul>
    //         </li>
        
    //         <li className="nav-item dropdown">
    //           <p className="nav-link dropdown-toggle" to="#" role="button" data-bs-toggle="dropdown" aria-expanded="false" id="a1">
    //             <b>SIgn Up</b>
    //           </p>
    //           <ul className="dropdown-menu">
    //             <li><NavLink className="dropdown-item" to="/manufacturers"> Manufacturers </NavLink></li>
    //           </ul>
    //         </li>

    //         <li className="nav-item">
    //           <p className="nav-link dropdown-toggle" to="#" role="button"  aria-expanded="false" id="a1">
    //             <b>Logout <NavLink className="item" to="/manufacturers"> Logout </NavLink></b>
    //           </p>
            
    //         </li>
          

    //       </ul>
    //     </div>
    //   </div>
    // </nav>
  )
}

export default Nav;
