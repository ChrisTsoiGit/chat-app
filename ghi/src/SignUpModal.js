import { useCallback } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useSignUpMutation } from './app/api';
import { updateField } from './app/accountSlice';
import Notification from './Notification';
import { useNavigate } from "react-router-dom";

function SignUpModal() {
  const dispatch = useDispatch();
  const { username, password, email, full_name } = useSelector(state => state.account);
  // const modalClass = `modal ${show === SIGN_UP_MODAL ? 'is-active' : ''}`;
  const [signUp, { error, isLoading: signUpLoading }] = useSignUpMutation();
  const field = useCallback(
    e => dispatch(updateField({field: e.target.name, value: e.target.value})),
    [dispatch],
  );

  let navigate = useNavigate();
  const routeChange = async (e) =>{
    // console.log("this is e", new FormData(e.target))
    e.preventDefault()
    await signUp({username, password, email, full_name})
    let path = `/login`;
    navigate(path);
  }

  return (
    // <div className={modalClass} key="signup-modal">
    //   <div className="modal-background"></div>
    <div className="ccontainer py-10 h-100">
    <div className="row d-flex justify-content-center align-items-center h-100">
    <div className="col-12 col-md-8 col-lg-6 col-xl-5">
    <div className="card bg-warning mb-3 p-5 text-center">
      <h3 className = "display-3 fw-bold mb-2 text-uppercase">Sign Up</h3>
      { error ? <Notification type="danger">{error.data.detail}</Notification> : null }
      {/* <form method="POST" onSubmit={preventDefault(signUp, () => ({ username, password, email, full_name }))}> */}
      <form method="POST" onSubmit={routeChange}>
        <div className="field">
          <div className="form-outline form-white mb-4">
            <input required onChange={field} value={username} name="username" className="form-control form-control-lg" type="username" placeholder="Username" />
          </div>
        </div>
        <div className="field">
          <div className="form-outline form-white mb-4">
            <input required onChange={field} value={password} name="password" className="form-control form-control-lg"  type="password" placeholder="Password" />
          </div>
        </div>
        <div className="field">
          <div className="form-outline form-white mb-4">
            <input required onChange={field} value={email} name="email" className="form-control form-control-lg"  type="email" placeholder="Email" />
          </div>
        </div>
        <div className="field">
          <div className="form-outline form-white mb-4">
            <input required onChange={field} value={full_name} name="full_name" className="form-control form-control-lg"  type="text" placeholder="Full Name" />
          </div>
        </div>
        <div className="field is-grouped">
          <div className="control p-2">
            {/* <button disabled={signUpLoading} className="button is-primary">Submit</button> */}
            <button disabled={signUpLoading}  className="btn btn-dark btn-lg px-5">Submit</button>
          </div>
          {/* <div className="control p-2">
            <button
              type="button"
              onClick={() => dispatch(showModal(null))}
              className="btn btn-outline-warning btn-lg px-5">Cancel</button>
          </div> */}
        </div>
        
      </form>
    </div>
  </div>
  </div>
  </div>

);
}

export default SignUpModal;
