import { BrowserRouter, Routes, Route} from "react-router-dom";
import Home from "../pages/Home";
import Login from "../pages/Login";
import Footer from "./Footer";
import Header from "./Header"




export default
 function Body () {
    return (
            <BrowserRouter>
                <Header />
                
                <Routes>
                    {/* <Route path="/" element={<Home/>} /> */}
                    <Route path="/login" element= {<Login/>}/>
                </Routes>

                <Footer />  
            </BrowserRouter>
           
           
    )
}