import { Navbar, Container, Nav, Form, FormControl, Button, Spinner } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { Link, useParams } from "react-router-dom";
import cookies from "react-cookies";
import { logoutUser } from "../ActionCreator/UserCreater";
import { useState } from "react";
import {useNavigate} from "react-router-dom"



export default function Header () {


    const user = useSelector(state => state.user.user)

    const [q, setQ] = useState("")



    const [salary_id, SetSalary] = useState("")

    const[experience_id, SetExperience] = useState("")

    const dispatch = useDispatch()

    const history= useNavigate()

    const searchq = (event) => {
        event.preventDefault()
        history(`/employer/?q=${q}`)
    }


    const searchS = (event) => {
        event.preventDefault()
        history(`/employer/?salary_id=${salary_id}`)

    }

    const searchE = (event) => {
        event.preventDefault()
        history(`/employer/?experience_id=${experience_id}`)

    }

    const [kw, setC] = useState("")

    const searchC = (event) => {
        event.preventDefault()
        history(`/home/?kw=${kw}`)

    }

    const logout = (event) => {
        event.preventDefault()

        cookies.remove("access_token")
        cookies.remove("user")
        dispatch(logoutUser())
    }

    let btn = <>
            <Link to="/login" className="nav-link text-danger">Dang nhap</Link>
            <Link to="/resgister" className="nav-link text-danger">Dang ky</Link>
    </>
    if (user != null)
        btn = <>
            <em><p className="nav-link text-danger">Your Name: {user.username}</p></em>
            <Link to="/home" className="nav-link text-danger" onClick={logout}>Log out</Link>
            <Link to="/info" className="nav-link text-danger">Person</Link>
        </>
        

    return (
        <>
            <Navbar bg="light" expand="lg">
                <Container>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Link className="nav-link" to="/employer">Information Teachnology</Link>
                        <Link className="nav-link" to="/home">Company</Link> 
                        {btn} 
                    </Nav>       

                    </Navbar.Collapse>
                </Container>
            </Navbar>
            <Navbar bg="light" expand="lg">
                <Container>
                <Form className="d-flex" onSubmit={searchq}>
                        <FormControl
                        value={q}
                        onChange={(event) => setQ(event.target.value)}
                        type="search"
                        placeholder="Search for title jobs"
                        className="me-2"
                        aria-label="Search"
                        />
                        <Button type="submit" variant="outline-success">Search</Button>
                </Form>

                    <Form className="d-flex" onSubmit={searchS}>
                        <FormControl
                        value={salary_id}
                        onChange={(event) => SetSalary(event.target.value)}
                        type="search"
                        placeholder="Search for salary"
                        className="me-2"
                        aria-label="Search"
                        />
                        <Button type="submit" variant="outline-success">Search</Button>
                    </Form>


                    <Form className="d-flex" onSubmit={searchE}>
                        <FormControl
                        value={experience_id}
                        onChange={(event) => SetExperience(event.target.value)}
                        type="search"
                        placeholder="Search Year for jobs"
                        className="me-2"
                        aria-label="Search"
                        />
                        <Button type="submit" variant="outline-success">Search</Button>
                    </Form>


                    <Form className="d-flex" onSubmit={searchC}>
                        <FormControl
                        value={kw}
                        onChange={(event) => setC(event.target.value)}
                        type="search"
                        placeholder="Search Company"
                        className="me-2"
                        aria-label="Search"
                        />
                        <Button type="submit" variant="outline-success">Search</Button>
                    </Form> 

                  
                </Container>
            </Navbar>
            


        </>
    )
}