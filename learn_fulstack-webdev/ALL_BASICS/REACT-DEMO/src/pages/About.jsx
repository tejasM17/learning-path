import { NavLink } from "react-router";

function About() {
    return (
        <div>
            <h1>About page</h1>
            <br />
            <NavLink to="/">Go to home</NavLink>
            <br />
            <NavLink to="/services">Go to services</NavLink>
        </div>
    )
}
export default About;