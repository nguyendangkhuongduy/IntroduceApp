import { useContext, useState } from "react"
import { Container, Form, Button } from "react-bootstrap"
import { useNavigate } from "react-router-dom"
import { UserContext } from "./Home"
import Jobs from "./Jobs"





const SignIn = () => {

    const [username, setUsername] = useState()
    const [password, setPassword] = useState()

    const nav = useNavigate()

    const navv = useNavigate()

    const navvv = useNavigate()

    const navvvv = useNavigate()

    const go = () => {
        nav("/options")
    }

    const gos = () => {
        navv("/jobs")
    }

    const gooo = () => {
        navvv("/signup")
    }


    const goooo = () => {
        navvvv("/signupp")
    }


    const [user, dispatch] = useContext(UserContext)

    const login = (event) => {
        event.preventDefault()

        if(username === "admin" && password === "123")
            dispatch({
                "type" : "login",
                "payload" : {
                    "name": "Duy",
                    "username": "admin"
                }
            })
    }
   

    if (user == null)
        return (
            <Container>
                <h3>Sign In</h3>
                <Form onSubmit={login}>
                    <div className="form-group">
                        <label>User name</label>
                        <input value={username} onChange={(evt) => setUsername(evt.target.value)} className="form-control" placeholder="Enter username" />
                    </div>
                    <div className="form-group">
                        <label>Password</label>
                        <input value={password} onChange={(evt) => setPassword(evt.target.value)} type="password"  className="form-control" placeholder="Enter password" />
                    </div>
                    <br></br>
                    <Button type="submit" className="btn btn-primary btn-block">Submit</Button>
                    {/* <p className="forgot-password text-right">
                        <button className="btn btn-primary btn-block" onClick={go}>Sign Up</button>
                    </p> */}
                    
                </Form>
                <Form style={{textAlign:"center"}}>
                    <br/>
                    <button className="text-center btn btn-primary btn-block" onClick={gooo}>Click here to register as an Employer</button>
                    <br/>
                    
                </Form>

                <Form style={{textAlign:"center"}}>
                    
                    <br/>
                    <button className="text-center btn btn-primary btn-block" onClick={goooo}>Click here to register as a Candidate</button>
                </Form>

                <Form style={{textAlign:"center"}}>
                    
                    <br/>
                    <br/>
                    <br/>
                    <br/>
                    <br/>
                 
                </Form>


            </Container>
        )


                    
    return <Jobs />
    // return <button onClick={gos} className="btn btn-primary btn-block ">Click here to enter system</button>
      
        
    // <h1>Xin chao {user.username}</h1> 
    
}
export default SignIn   

