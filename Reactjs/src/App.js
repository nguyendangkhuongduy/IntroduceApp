import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Header from './layout/Header';
import Footer from './layout/Footer';
import 'bootstrap/dist/css/bootstrap.min.css';
import SignIn from './components/SignIn';
import Jobs from './components/Jobs';
import SignUp from './components/SignUp';
import Home from './components/Home';


const App = () => {

  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Jobs />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/home" element={<Home />}/>
        
      </Routes>
      <Footer />  
    </BrowserRouter>
  )
}

export default App;
