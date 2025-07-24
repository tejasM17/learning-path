import Header from "./Header"
import Footer from "./Footer"
import { NavLink } from "react-router";

function App() {
  return (
    <div>
      <Header />
      <h1>hello React</h1>
      {/* <a href="/about">About here </a> */}
      <br />
      <br />
      <NavLink to="/about">About page</NavLink>
      <br />
      <br />
      <NavLink to="/services">Go to services</NavLink>
      <Footer />
    </div>
  )
}

export default App