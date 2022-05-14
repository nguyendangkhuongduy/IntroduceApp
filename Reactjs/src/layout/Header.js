import { Navbar, Container, Nav } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import cookies from "react-cookies";
import { logoutUser } from "../ActionCreator/UserCreater";

export default function Header () {

    const user = useSelector(state => state.user.user)

    const dispatch = useDispatch()

    const logout = (event) => {
        event.preventDefault()

        cookies.remove("access_token")
        cookies.remove("user")
        dispatch(logoutUser())
    }



    // let path =  <Link className="nav-link text-danger" to="/login">Log In</Link> 
    // if (user !== null)
    // {  
    //     path =  <Link className="nav-link text-danger" to="/">{user.username}</Link> 
    //     path =  <Link className="nav-link text-danger" to="/">Log out</Link> 
    // }

    let btn = <>
            <Link to="/login" className="nav-link text-danger">Dang nhap</Link>
            <Link to="/resgister" className="nav-link text-danger">Dang ky</Link>
    </>
    if (user != null)
        btn = <>
            <Link to="/home" className="nav-link text-danger">{user.username}</Link>
            <Link to="/home" className="nav-link text-danger" onClick={logout}>Dang xuat</Link>
            <Link to="/recruitment" className="nav-link text-danger">Them Tin Tuyen Dung</Link>
        </>
        

    return (
        <>
            <Navbar bg="light" expand="lg">
                <Container>
                    {/* <Navbar className="nav-link" to="/">Information Teachnology</Navbar> */}
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Link className="nav-link" to="/employer">Information Teachnology</Link>
                        <Link className="nav-link" to="/home">Company</Link> 
                        {/* {path} */}
                        {btn}
                        

                    </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    )
}