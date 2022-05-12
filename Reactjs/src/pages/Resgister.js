// import { Button } from "react-bootstrap";
// import { useRef } from "react";
// import { useState } from "react";
// import { Form } from "react-bootstrap";
// import { useNavigate } from 'react-router-dom'
// import { useHistory } from "react"
// import Apis, { endpoints } from "../configs/Apis";

// export default function Resgister() {
//     const [username, setUserName] = useState()
//     const [password, setPassWord] = useState()
//     const [firstName, setFirstName] = useState()
//     const [lastName, setLastName] = useState()
//     const [conFirmpassWord, setConFirmPassWord] = useState()
//     const [email, setEmail] = useState()
//     const avatar = useRef()
    // const nav = useNavigate()
    // const history = useHistory()


    // const register = async (event) => {
    //     event.preventDefault()
    //     let registerUser = async () => {
    //         const form = new formData
    //         form.append("first_name", firstName)
    //         form.append("last_name", lastName)
    //         form.append("email", email)
    //         form.append("password", password)
    //         form.append("username", username)
    //         form.append("avatar", avatar.current.files[0])

    //         try {
    //             let res = await Apis.post(endpoints['register'], form, {
    //                 headers: {
    //                     "Content-Type": "multipart/form-data"
    //                 }
    //             })
    //             console.info(res.data)
                // history.push("/login")

    //         } catch(err) {
    //             console.info(err)
    //         }    
    //     }

    //     if(password !== null && password === conFirmpassWord) {
    //         registerUser()
    //     }
    // }
// import React, { useState, useRef } from 'react'
// import { Form, Button, Container } from "react-bootstrap"

// import Apis, { endpoints } from '../configs/Apis'

// const Resgister = () => {
//     const [newUser, setNewUser] = useState({
//         "first_name": '',
//         "last_name": '',
//         "username": "",
//         "password": ""
//     })
//     const avatar = useRef()
    

//     const change = (obj) => {
//         setNewUser({
//             ...newUser, 
//             ...obj
//         })
//     }

    // const register = async (event) => {
    //     event.preventDefault()

    //     let data = new FormData()
    //     data.append("first_name", firstName)
    //     data.append("last_name", lastName)
    //     data.append("email", email)
    //     data.append("password", password)
    //     data.append("username", username)
    //     data.append("avatar", avatar.current.files[0])
        // data.append('first_name', newUser.first_name)
        // data.append('last_name', newUser.last_name)
        // data.append('username', newUser.username)
        // data.append('password', newUser.password)
        // data.append('avatar', avatar.current.files[0])

    //     try {
    //         const res = await Apis.post(endpoints['users'], data, {
    //             headers: {
    //                 'Content-Type': 'multipart/form-data'
    //             }
    //         })
    //         if (res.status === 201)
    //             nav("/login")
    //     } catch (error) {
    //         console.error(error)
    //     }

    //     if(password !== null && password === conFirmpassWord) {
    //         register()
    //     }
        
    // }

//     return (
//         <>
//             <h1 className="text-center text-danger">Register</h1>

            
//             <Form onSubmit={register}>
//                 <RegisterForm id="firstName" Label="First Name" 
//                               type="text"  value={firstName} 
//                               change={(event) => setFirstName(event.target.value)} />

//                 <RegisterForm id="lastName" Label="Last Name" 
//                               type="text"  value={lastName} 
//                               change={(event) => setLastName(event.target.value)} />


//                 <RegisterForm id="email" Label="Email" 
//                               type="text"  value={email} 
//                               change={(event) => setEmail(event.target.value)} />


//                 <RegisterForm id="userName" Label="User Name" 
//                               type="text"  value={username} 
//                               change={(event) => setUserName(event.target.value)} />


//                 <RegisterForm id="passWord" Label="Pass Word" 
//                               type="password"  value={password} 
//                               change={(event) => setPassWord(event.target.value)} />

                
//                 <RegisterForm id="conFirmpassWord" Label="ConFirm PassWord" 
//                               type="password"  value={conFirmpassWord} 
//                               change={(event) => setConFirmPassWord(event.target.value)} />


//                 <Form.Group className="mb-3" controlId="avatar">
//                     <Form.Label>Avatar</Form.Label>
//                     <Form.Control type="file" ref={avatar} className="form-control" />
//                 </Form.Group>

               
//                 <Button variant="primary" type="submit">
//                     Register
//                 </Button>
//             </Form>
//         </>
//     )
// }

// function RegisterForm(props) {
//     return (
//         <Form.Group className="mb-3" controlId={props.id}>
//             <Form.Label>{props.Label}</Form.Label>
//                 <Form.Control type={props.type}
//                         value={props.value}
//                         onChange={props.change}/>
//         </Form.Group>
//     )
// }

// // export default Registerr
import React, { useState, useRef } from 'react'
import { Form, Button, Container } from "react-bootstrap"
import { useNavigate } from 'react-router-dom'
import Apis, { endpoints } from "../configs/Apis";

const Resgister = () => {
    const [newUser, setNewUser] = useState({
        "first_name": '',
        "last_name": '',
        "username": "",
        "password": "",
        "email": "", 
        "confirm": ""
    })
    const avatar = useRef()
    const nav = useNavigate()

    const change = (obj) => {
        setNewUser({
            ...newUser, 
            ...obj
        })
    }

    const register = async (event) => {
        event.preventDefault()

        let data = new FormData()
        data.append('first_name', newUser.first_name)
        data.append('last_name', newUser.last_name)
        data.append('username', newUser.username)
        data.append('password', newUser.password)
        data.append('email', newUser.email)
        data.append('avatar', avatar.current.files[0])

        try {
            const res = await Apis.post(endpoints['register'], data, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            if(newUser.password !== null && newUser.password === newUser.confirm) {
                if (res.status === 201)
                    nav("/login")
                 }
            
        } catch (error) {
            console.error(error)
        }
        
    }

    return (
        <Container>
            <h1 className="text-center text-danger">DANG KY NGUOI DUNG</h1>
            <Form onSubmit={register}>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>First Name</Form.Label>
                <Form.Control type="text" value={newUser.first_name} onChange={(evt) => change({'first_name': evt.target.value})} />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Last Name</Form.Label>
                <Form.Control type="text" value={newUser.last_name} onChange={(evt) => change({'last_name': evt.target.value})} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Username</Form.Label>
                <Form.Control type="text" value={newUser.username} onChange={(evt) => change({'username': evt.target.value})} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Password</Form.Label>
                <Form.Control type="password" value={newUser.password} onChange={(evt) => change({'password': evt.target.value})} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Confirm Password</Form.Label>
                <Form.Control type="password" value={newUser.confirm} onChange={(evt) => change({'confirm': evt.target.value})} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>Email:</Form.Label>
                <Form.Control type="email" value={newUser.email} onChange={(evt) => change({'email': evt.target.value})} />
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicEmail">
                <Form.Label>avatar</Form.Label>
                <Form.Control type="file" ref={avatar} />
            </Form.Group>
            <Button variant="primary" type="submit">
                Dang ky
            </Button>
            </Form>
        </Container>
    )
}

export default Resgister