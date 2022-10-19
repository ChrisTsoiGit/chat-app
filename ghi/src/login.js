// import {useState, useEffect} from 'react';

// function BootstrapInput(props) {
//     const { id, placeholder, labelText, value, onChange, type } = props;

//     return (
//         <div className='mb-4'>
//             <label htmlFor={id} className='form-label'>{labelText}</label>
//             <input value={value} onChange={onChange} required_type={type} className='form-control' id={id} placeholder={placeholder}></input>
//         </div>
//     );
// }

// function Login(props) {
//     const [email, setEmail] = useState('');
//     const [username, setUsername] = useState('');
//     const [password, setPassword] = useState('');
//     const [token, setToken] = useState('');

//     useEffect(()=>{
//         async function gettoken(){
//             const url = `${process.env.REACT_APP_ACCOUNTS_HOST}/token`;
//             const response = await fetch(url);
//             if (response.ok) {
//                 const data = await response.json();
//                 setToken(data);
//             }
//         }

//         gettoken();
//     },[setToken])

//     return (
//         <form>
//             <BootstrapInput
//                 id='email'
//                 placeholder='youremail@example.com'
//                 labelText='Your email address'
//                 value={email}
//                 onChange={e => setEmail(e.target.value)}
//                 type='email' />
//             <BootstrapInput
//                 id='username'
//                 placeholder='Blah Blah'
//                 labelText='Your name'
//                 value={username}
//                 onChange={e => setUsername(e.target.value)}
//                 type='text' />
//             <BootstrapInput
//                 id='password'
//                 placeholder='Your secret password'
//                 labelText='Password'
//                 value={password}
//                 onChange={e => setPassword(e.target.value)}
//                 type='password' />
//             <button type='submit' className='btn btn-primary'>Submit</button>
//         </form>
//     );}
//         // <div className="footer">
//         //     <button
//         //         onClick={() => {
//         //             closeLogin(false);
//         //         }}
//         //         id="cancelBtn"
//         //     >
//         //         Cancel
//         //     </button>
//         //     <button type='submit' className='btn btn-primary'>Submit</button>
//         // </div>


// export default Login;

