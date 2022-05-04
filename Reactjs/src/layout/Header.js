import { useContext } from "react"
import { Container, Nav, Navbar } from "react-bootstrap"
import { Link, useNavigate } from "react-router-dom"
import { UserContext } from "../components/Home"

const Header  = () => {
    // const user = useContext(UserContext)

    const [user, dispatch] = useContext(UserContext)

    const nav = useNavigate()

    const go = () => {
        nav("/jobs")
    }

    const navv = useNavigate()

    const goo = () => {
        navv("/companies")
    }

    const navvvvv = useNavigate()

    const gooooo = () => {
        navvvvv("/profile")
    }

    const logout = (evt) => {
        evt.preventDefault()
        dispatch({"type": "logout"})
    }
    // const logout = () => {
    //     dispatch({"type": "logout"})
    // }
    let btn = <Link to="/signin" className="nav-link text-danger">Log In</Link>
    if (user != null)
       
        btn = <>
            <Link to="/jobs" className="nav-link text-danger">{user.name}</Link>
            <a href="#" onClick={logout} className="nav-link text-danger">Log Out</a>
        </>


    // let btn = <h1 className="nav-link text-danger">User name: {user}</h1>
    // let btnn = <h1 className="nav-link text-danger">Log Out {user}</h1>

    return (
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Container>
            <Navbar.Brand href="#home" onClick={go}>IT VietNam</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="me-auto">
                <Nav.Link href="#features" onClick={go}>All Jobs</Nav.Link>
                <Nav.Link href="#pricing" onClick={goo}>Companies</Nav.Link>
                {btn}
                <Nav.Link href="#features" onClick={gooooo}>Profile</Nav.Link>
                
               
               
                {/* <NavDropdown title="Dropdown" id="collasible-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                </NavDropdown>
                </Nav>
                <Nav> */}
                {/* <Nav.Link href="#deets">More deets</Nav.Link>
                <Nav.Link eventKey={2} href="#memes">
                    Dank memes  
                </Nav.Link> */}
                </Nav>
                
                {/* <h1>Your name: {user}</h1> */}
                {/* <button onClick={logout}>Log Out</button> */}
            </Navbar.Collapse>
            
            </Container>
        </Navbar>
    )
}

export default Header