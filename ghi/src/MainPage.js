import * as React from "react";
// import { NavLink } from 'react-router-dom';


function MainPage() {
    return(
    
    <div className="container">
          <div className="row">
            <div className="col">
              <div className="card border border-warning mb-3 shadow eachCard">
                {/* <img src={inventory} height="600px" className="card-img-top" alt="This is a discription"/> */}
                <div className="card-body mainpageBotton cardTitle1 cardTitle">
                  <h4 className="card-title display-3 fw-bold">Chat</h4>
                  {/* <NavLink className="dropdown-item choice" to="/manufacturers">Manufacturers</NavLink>
                  <NavLink className="dropdown-item choice" to="/models">Vehicle Models</NavLink>
                  <NavLink className="dropdown-item choice" to="/automobiles">Automobiles</NavLink> */}
                </div>
              </div>
            </div>
            </div>
        
         </div>
    );
}

export default MainPage