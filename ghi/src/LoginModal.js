import { useCallback } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useLogInMutation } from './app/api';
// import { eventTargetSelector as target, preventDefault } from './app/utils';
// import { showModal, updateField } from './app/accountSlice';
import { updateField } from './app/accountSlice';
import Notification from './Notification';
import { useNavigate } from "react-router-dom";

function LogInModal() {
  const dispatch = useDispatch();
  const { username, password } = useSelector(state => state.account);
  // const modalClass = `modal ${show === LOG_IN_MODAL ? 'is-active' : ''}`;
  const [logIn, { error, isLoading: logInLoading }] = useLogInMutation();
  const field = useCallback(
    e => dispatch(updateField({field: e.target.name, value: e.target.value})),
    [dispatch],
  );

  let navigate = useNavigate();
  const routeChange = async (e) =>{
    // console.log("this is e", new FormData(e.target))
    e.preventDefault()
    await logIn(e.target)
    let path = `/chat`;
    // navigate(path);
    console
  }

  let signupNavigate = useNavigate();
      const signupChange = (e) =>{
        e.preventDefault()
        let path = `/signup`;
        signupNavigate(path);
      }



  return (
    
      <div className="container py-5 h-100">
        <div className="row d-flex justify-content-center align-items-center h-100">
        <div className="col-12 col-md-8 col-lg-6 col-xl-5">
        <div className="card-body p-5 text-center">
        <div className="p-3 mb-2 bg-secondary ">
          <h3 className = "fw-bold mb-4 text-uppercase">Log In</h3>
          
          { error ? <Notification type="danger">{error.data.detail}</Notification> : null }
          {/* <form method="POST" onSubmit={() => {preventDefault(logIn, target); routeChange();}}> */}
          <form method="POST" onSubmit={routeChange}>
            <div className="field">
              {/* <label className="label" htmlFor="username">Username</label> */}
              <div className="form-outline form-white mb-4">
                <input required onChange={field} value={username} name="username" className="form-control form-control-lg" type="username" placeholder="Username" />
              </div>
            </div>
            <div className="field">
              {/* <label className="label">Password</label> */}
              <div className="form-outline form-white mb-4">
                <input required onChange={field} value={password} name="password" className="form-control form-control-lg" type="password" placeholder="Password" />
              </div>
            </div>
            <div className="field is-grouped">
              <div className="control p-2">
                <button disabled={logInLoading}  className="btn btn-outline-warning btn-lg px-5">Log In</button>
              </div>
              {/* <div className="control p-2">
                <button
                  type="button"
                  onClick={() => dispatch(showModal(null))}
                  className="btn btn-outline-warning btn-lg px-5">Cancel</button>
              </div> */}

              <div className="control p-2">
                <button onClick={signupChange} className="btn btn-outline-warning btn-lg px-5">Sign Up</button>
              </div>
      
            </div>
          </form>
        </div>

        </div>
        </div>
        </div>
      </div>
    
  );
}

export default LogInModal;


