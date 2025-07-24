import { NavLink } from "react-router";

function Services() {
  return (
    <div>
      <h1>Our Services</h1>
      <ul>
        <li>Service 1</li>
        <li>Service 2</li>
        <li>Service 3</li>
      </ul>
    <NavLink to="/">Go to home</NavLink>
    <br />
    <NavLink to='/about'>About page</NavLink>
    </div>
    
  );
}
export default Services