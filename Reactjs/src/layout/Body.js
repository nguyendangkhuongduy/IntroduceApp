import { BrowserRouter, Routes, Route} from "react-router-dom";
import Company from "../pages/Company";
import EmployerDetails from "../pages/EmployerDetails";
import RecruitmentDetails from "../pages/RecruitmentDetails";
import Home from "../pages/Home";
import Login from "../pages/Login";
import Recuitment from "../pages/Recuitment";
import Footer from "./Footer";
import Header from "./Header"
import Resgister from "../pages/Resgister";
import AddRecruitment from "../pages/AddRecruitment";
import Infor from "../pages/Infor";



export default
 function Body () {
    return (
            <BrowserRouter>
                <Header />
                
                <Routes>
                    <Route path="/home" element={<Home/>} />
                    <Route path="/login" element= {<Login/>}/>
                    <Route path="/employer" element= {<Company/>}/>
                    <Route path="/employer/:employerId/" element={<EmployerDetails/>}/>
                    <Route path="/recruitment/:recruitmentId/" element={<RecruitmentDetails/>}/>
                    <Route path="/employer/:employerId/recruitment" element={<Recuitment/>} />
                    <Route path="/resgister" element={<Resgister/>} />
                    <Route path="/recruitment" element={<AddRecruitment/>} />
                    <Route path="/info" element={<Infor/>} />
                </Routes>

                <Footer />  
            </BrowserRouter>
           
           
    )
}