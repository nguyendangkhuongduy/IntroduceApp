import { createContext, useReducer } from "react"
import { BrowserRouter, Route, Routes } from "react-router-dom"
import Footer from "../layout/Footer"
import Header from "../layout/Header"
import userReducer from "../reducers/MyReducer"
import Companies from "./Companies"
import Jobs from "./Jobs"
import Options from "./Options"
import Profile from "./Profile"
import SignIn from "./SignIn"
import SignUp from "./SignUp"
import SignUpp from "./SignUpp"
import UserInfo from "./UserInfo"



export const UserContext = createContext()

const Home = () => {
    const [user, dispatch] = useReducer(userReducer)


    return (
        <BrowserRouter>
            <UserContext.Provider value={[user, dispatch]}>
                <Header />
                <UserInfo/>
            
                <Routes>
                    <Route path="/profile" element={<Profile/>} />
                    <Route path="/signin" element={<SignIn/>} />
                    <Route path="/" element={<Jobs/>} />
                    <Route path="/options" element={<Options />} />
                    <Route path="/signup" element={<SignUp/>} />
                    {/* <Route path="/home" element={<Home />} /> */}
                    <Route path="/jobs" element={<Jobs />} />
                    <Route path="/signupp" element={<SignUpp />} />
                    <Route path="/companies" element={<Companies/>} />
                </Routes>
            <Footer />  
            </UserContext.Provider> 
        </BrowserRouter>
          
    )
}
export default Home