// import { useRef } from "react"
// import { useState } from "react"
// import { Form, Button } from "react-bootstrap"
// import Apis, { endpoints } from "../configs/Apis"

// export default function AddRecruitment () {

//     const [newUser, setNewUser] = useState({
//         "content": '',
//         "title": '',
//         "contact_name": "",
//         "phone_number": "",
//         "email": "", 
//         "address": "",
//         "employer": "",
//         "salary": "",
//         "career": "",
//         "expericence": ""
//     })
//     const image = useRef()

//     const add = async (event) => {
//         event.preventDefault()

//         let data = new FormData()
//         data.append('content', newUser.content)
//         data.append('title', newUser.title)
//         data.append('contact_name', newUser.contact_name)
//         data.append('phone_number', newUser.phone_number)
//         data.append('email', newUser.email)
//         data.append('employer', newUser.employer)
//         data.append('salary', newUser.salary)
//         data.append('career', newUser.career)
//         data.append('experience', newUser.expericence)
//         data.append('image',image.current.files[0])

//         try {
//             const res = await Apis.post(endpoints['add-recruitment'], data)
//         } catch (error) {
//             console.error(error)
//         }
        
//     }

//     return (
//         <>
//             <h1 className="text-danger text-center">Add Recruitment</h1>

//             <Form onSubmit={add}>
//             <Form.Group className="mb-3" controlId="formBasicEmail">
//                 <Form.Label>Title</Form.Label>
//                 <Form.Control type="text" value={newUser.title} onChange={(evt) => change({'title': evt.target.value})} />
//             </Form.Group>

//             <Form.Group className="mb-3" controlId="formBasicEmail">
//                 <Form.Label>Content</Form.Label>
//                 <Form.Control type="text" value={newUser.content} onChange={(evt) => change({'content': evt.target.value})} />
//             </Form.Group>
//             <Form.Group className="mb-3" controlId="formBasicEmail">
//                 <Form.Label>Contact name:</Form.Label>
//                 <Form.Control type="text" value={newUser.contact_name} onChange={(evt) => change({'contact_name': evt.target.value})} />
//             </Form.Group>
//             <Form.Group className="mb-3" controlId="formBasicEmail">
//                 <Form.Label>Phone number</Form.Label>
//                 <Form.Control type="text" value={newUser.phone_number} onChange={(evt) => change({'phone_number': evt.target.value})} />
//             </Form.Group>
//             <Form.Group className="mb-3" controlId="formBasicEmail">
//                 <Form.Label>Email:</Form.Label>
//                 <Form.Control type="email" value={newUser.email} onChange={(evt) => change({'email': evt.target.value})} />
//             </Form.Group>
//             <Form.Group className="mb-3" controlId="formBasicEmail">
//                 <Form.Label>Experience:</Form.Label>
//                 <Form.Control type="email" value={newUser.expericence} onChange={(evt) => change({'experience': evt.target.value})} />
//             </Form.Group>
//             <Form.Group className="mb-3" controlId="formBasicEmail">
//                 <Form.Label>Career:</Form.Label>
//                 <Form.Control type="text" value={newUser.career} onChange={(evt) => change({'career': evt.target.value})} />
//             </Form.Group>
//             <Form.Group className="mb-3" controlId="formBasicEmail">
//                 <Form.Label>Address:</Form.Label>
//                 <Form.Control type="text" value={newUser.address} onChange={(evt) => change({'address': evt.target.value})} />
//             </Form.Group>
//             <Form.Group className="mb-3" controlId="formBasicEmail">
//                 <Form.Label>Salary:</Form.Label>
//                 <Form.Control type="text" value={newUser.salary} onChange={(evt) => change({'salary': evt.target.value})} />
//             </Form.Group>
//             <Form.Group className="mb-3" controlId="formBasicEmail">
//                 <Form.Label>avatar</Form.Label>
//                 <Form.Control type="file" ref={avatar} />
//             </Form.Group>
//             <Button variant="primary" type="submit">
//                 Dang Tin
//             </Button>
//             </Form>
//         </>
//     )
// }