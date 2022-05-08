import { Button } from "bootstrap";
import { useState } from "react";
import { Form } from "react-bootstrap";
import Apis, { endpoints } from "../configs/Apis";
import { useDispatch } from "react-redux"
import { useHistory } from "react"
import loginUser from "../ActionCreator/UserCreater";
import cookies from "react-cookies";

export default function Login () {

    const [username, setUserName] = useState()
    const [password, setPassWord] = useState()
    const dispatch = useDispatch()
    const history = useHistory()

    const login = async (event) => {
        event.preventDefault()
        
        try{
            let info = await Apis.get(endpoints['oauth2-info'])
            let res = await Apis.post(endpoints['login'], {
                "client_id": info.data.client_id,
                "client_secret": info.data.client_secret,
                "username": username,
                "password": password,
                "grant_type": "password"
            })
//bật oauth2provier trong python
            // localStorage.setItem("accesss_token", res.data.access_token)
            cookies.save("accesss_token", res.data.access_token)

            let user = await Apis.get(endpoints['current-user'], {
                headers: {
                    'Authorization': `Bearer ${cookies.load("access_token")}`
                }
            })

            console.info(user)

            // localStorage.setItem("user", user.data)
            cookies.save("user", user.data)

            // dispatch({
            //     "type": "USER_LOGIN",
            //     "payload": user.data
            // })

            dispatch(loginUser(user.data))
            // dispatch({
            //     'type': 'login',
            //     'payload': user.data
            // })

            history.push("/")

        } catch(err) {
            console.info(err)
        }
    }

    return (
        <>
            <h1 className="text-center text-danger">LOG IN</h1>

            <Form onSubmit={login}>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Label>User name</Form.Label>
                    <Form.Control type="text"
                                  placeholder="User name"
                                  value={username}
                                  onChange={(event) => setUserName(event.target.value)}/>
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password"
                                  placeholder="Password"
                                  value={password}
                                  onChange={(event) => setPassWord(event.target.value)} />
                </Form.Group>
               
                <Button variant="primary" type="submit">
                    Log In
                </Button>
            </Form>

        </>
    )

}
