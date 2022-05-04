import { useContext } from "react"
import { UserContext } from "./Home"

const UserInfo = () => {

    const [user, dispatch] = useContext(UserContext)


    if(user == null)
        return <h1 className="text-center text-danger" >Please login to use the system</h1>

    // const logout = () => {
    //     dispatch({"type": "logout"})
    // }

    return (
        <>
            {/* <h1 className="text-center">WELCOME {user.name} </h1> */}
           
        </>
    )

}

export default UserInfo