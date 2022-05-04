import { Container, Form, Button } from "react-bootstrap"
import { useNavigate } from "react-router-dom"

const SignUp = () => {

    const nav = useNavigate()

    const go = () => {
        nav("/")
    }

    return (
        <Container>
            <h3 className="text-center">Employer</h3>
            <Form>
                <div className="form-group">
                    <label>Company name</label>
                    <input type="text" className="form-control" placeholder="Enter company name...." />
                </div>
                <div className="form-group">
                    <label>Address</label>
                    <input type="text" className="form-control" placeholder="Enter address" />
                </div>
                <div className="form-group">
                    <label>Phone number</label>
                    <input type="email" className="form-control" placeholder="Enter phone" />
                </div>
                <div className="form-group">
                    <label>Logo company</label>
                    <input type="image" className="form-control" placeholder="Enter logo" />
                </div>
                <div className="form-group">
                    <label>Password</label>
                    <input type="password" className="form-control" placeholder="Enter password" />
                </div>
                
            </Form>
            <br></br>
            <Form>
                <Button style={{margin: "20px"}} type="submit" className="btn btn-primary btn-block" onClick={go}>Back to Sign In</Button>  
                <Button type="submit" className="btn btn-primary btn-block">Sign Up</Button>
            </Form>

            <Form style={{textAlign:"center"}}>
                    
                    <br/>
                    <br/>
                    
                 
                </Form>
        </Container>
    )
}

export default SignUp