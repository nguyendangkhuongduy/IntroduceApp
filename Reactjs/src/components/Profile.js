import { useContext, useReducer } from "react"
import { Form } from "react-bootstrap"
import { UserContext } from "../components/Home"


const Profile = () => {

    const [user, dispatch] = useContext(UserContext)

    // const [user, dispatch] = useReducer(userReducer)

    if(user != null)
        return <h1>{user.name}</h1>
        
    return (
        <>
            <h1 style={{textAlign:"center"}}>No information</h1>

            <Form style={{textAlign:"center"}}>
                    
                    <br/>
                    <br/>
                    <br/>
                    <br/>
                    <br/>
                    <br/>
                    <br/>
                    <br/>
                 
            </Form>
        </>
    )
   
}

export default Profile