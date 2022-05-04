import { Container, Form, Button } from "react-bootstrap"
import { useNavigate } from "react-router-dom"

const SignUpp = () => {

    const nav = useNavigate()

    const go = () => {
        nav("/")
    }

    return (
        <Container>
            <h3 className="text-center">Candidate</h3>
            <Form>
                <div className="form-group">
                    <label>Name</label>
                    <input type="text" className="form-control" placeholder="Enter name...." />
                </div>
                <div className="form-group">
                    <label>Gender</label>
                    <input type="text" className="form-control" placeholder="Enter gender...." />
                </div>
                <div className="form-group">
                    <label>Birthday</label>
                    <input type="text" className="form-control" placeholder="Enter birthday...." />
                </div>
                <div className="form-group">
                    <label>Specialized</label>
                    <input type="text" className="form-control" placeholder="Enter specialized...." />
                </div>
                <div className="form-group">
                    <label>Address</label>
                    <input type="text" className="form-control" placeholder="Enter address...." />
                </div>
                <div className="form-group">
                    <label>Phone number</label>
                    <input type="email" className="form-control" placeholder="Enter phone...." />
                </div>
                <div className="form-group">
                    <label>Avatar</label>
                    <input type="image" className="form-control" placeholder="Enter avatar...." />
                </div>
                <div className="form-group">
                    <label>Password</label>
                    <input type="password" className="form-control" placeholder="Enter password..." />
                </div>
                
                <br></br>
                <Form>
                    <Button style={{margin:"20px"}} type="submit" className="btn btn-primary btn-block" onClick={go}>Back to Sign In</Button>  
                    <Button type="submit" className="btn btn-primary btn-block">Sign Up</Button>
                </Form>

            </Form>
        </Container>
    )
}

export default SignUpp