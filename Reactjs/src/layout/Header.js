import { Navbar, Container, Nav } from "react-bootstrap";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";

export default function Header () {

    const user = useSelector(state => state.user.user)



    // let path =  <Link className="nav-link text-danger" to="/login">Log In</Link> 
    // if (user !== null)
    // {  
    //     path =  <Link className="nav-link text-danger" to="/">{user.username}</Link> 
    //     path =  <Link className="nav-link text-danger" to="/">Log out</Link> 
    // }

    let btn = <Link to="/login" className="nav-link text-danger">Dang nhap</Link>
    if (user != null)
        btn = <>
            <Link to="/" className="nav-link text-danger">{user.username}</Link>
            <a href="#" className="nav-link text-danger">Dang xuat</a>
        </>
        

    return (
        <>
            <Navbar bg="light" expand="lg">
                <Container>
                    <Navbar.Brand href="#home">Information Teachnology</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Link className="nav-link" to="#home">News</Link>
                        <Link className="nav-link" to="#link">Company</Link> 
                        {/* {path} */}
                        {btn}

                    </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    )
}