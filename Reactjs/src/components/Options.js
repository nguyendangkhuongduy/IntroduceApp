import { useNavigate } from "react-router-dom"
import SignIn from "./SignIn"
import UserInfo from "./UserInfo"

const Options = () => {

    const navSignup = useNavigate()

    const gooo = () => {
        navSignup("/signup")
    }

    const navSignupp = useNavigate()

    const goooo = () => {
        navSignupp("/signupp")
    }

    return (
        <>
            <SignIn />
            <button className="text-center btn btn-primary btn-block" onClick={gooo}>Click here to register as an employer</button>
            <button className="text-center btn btn-primary btn-block" onClick={goooo}>Click here to register as a candidate</button>
        </>
    )
}

export default Options