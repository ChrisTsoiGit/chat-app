function AccountForm(props) {
  return (
    // <div>
    //   <header classNName="App-header">
    //     <h1>Hooks example</h1>
    //     <p>Form here</p>
    //   </header>
    // </div>

    <form>
      <div className="mb-3">
        <label htmlFor="email" className="form-label">
          Email address:
        </label>
        <input
          required
          type="email"
          className="form-control"
          id="emai"
          placeholder="name@example.com"
        />
      </div>

      <div className="mb-3">
        <label htmlFor="full_name" className="form-label">
          Full name:
        </label>
        <input
          required
          type="text"
          className="form-control"
          id="full_name"
          placeholder="John Doe"
        />
      </div>

      <div className="mb-3">
        <label htmlFor="username" className="form-label">
          Username:
        </label>
        <input
          required
          type="text"
          className="form-control"
          id="username"
          placeholder="your username"
        />
      </div>

      <div className="mb-3">
        <label htmlFor="password" className="form-label">
          Password:
        </label>
        <input
          required
          type="passwordd"
          className="form-control"
          id="password"
          placeholder="your password"
        />
      </div>

      <button type="submit" className="btn btn-primary">
        Submit
      </button>
    </form>
  );
}

export default AccountForm;
