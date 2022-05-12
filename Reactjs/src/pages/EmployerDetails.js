import { useEffect } from "react"
import { useState } from "react"
import { Col, Row, Spinner, Image, Form } from "react-bootstrap"
import { Link, useParams } from "react-router-dom"
import Apis, { authApi, endpoints } from "../configs/Apis"
import { Button } from "react-bootstrap";
import Moment from "react-moment"
import { useSelector } from "react-redux"
// import cookies from "react-cookies"

export default function EmployerDetails () {

  
    const [employer, SetEmployer] = useState(null)
    const [comments, Setcomments] = useState([])
    const [commentContent, SetCommentContent] = useState([])
    const [change, SetChange] = useState(1)

    let user  = useSelector(state => state.user.user)
    let {employerId} = useParams()
    let comment = <em><Link to="/login">Log In</Link> to comment</em>
    let path = `/employer/${employerId}/recruitment/`


    const addComment = async (event) => {
        event.prevenDefault()

        try {
            const res = await authApi().post(endpoints['add-comment'], {
                'content': commentContent
            }
            )
            comments.push(res.data)
            Setcomments(comments)
            SetChange(comments.length)
        } catch (err) {
            console.info(err)
        }

    }


    if (user !== null && user !== undefined) {
        comment = <Form onSubmit={addComment}>
        <Form.Group className="mb-3" controlId="commentControl">
            <Form.Control type="text" value={commentContent} onChange={(event) => SetCommentContent(event.target.value)}
                                         placeholder="Type comment..." rows={3} />
        </Form.Group>
        <Button type="submit" variant="info">Send</Button>
    </Form>
    }

    useEffect(() =>{
        let loadEmployer = async () => {
            try {
                let res = await Apis.get(endpoints['employer-detail'](employerId))
                SetEmployer(res.data)
            } catch(err) {
                console.error(err)
            }
        }

        let loadComments = async () => {
            try {
                let res = await Apis.get(endpoints['comments'](employerId))
                Setcomments(res.data)
            } catch (err) {
                console.error(err)
            }
            
        }

        loadEmployer()
        loadComments()
    }, [change])
    

    if(employer === null)
        return <Spinner animation="border" />

    
         
        
    return (
        <>
            <h1 className="text-center text-danger">Company Details</h1>

            <Row>
                <Col md={4} xs={12}>
                    {/* <Link to={path}>
                        <Image src={employer.image} rounded fluid />
                    </Link> */}
                     <Image src={employer.image} rounded fluid />
                </Col>
                <Col md={8} xs={12}>
                    <h2>{employer.name}</h2>
                    <p>Phone: {employer.phone_number}</p>
                    {/* <p>
                        {employer.address.map(t => <Badge style={{backgroundColor: "blue"}} bg="secondary">{t.name}</Badge>)}
                    </p> */}
                    <p>Email: {employer.email}</p>
                    {/* <p>From: {employer.address.name}</p> */}
                    <p>Date join: {employer.created_date}</p>
                    <Link to={path}>
                        <Button>All jobs for company</Button>
                    </Link>
                </Col>
            </Row>
            <hr/>
            <div
                    dangerouslySetInnerHTML={{
                        __html: employer.description,
                    }}
                />

            <hr>
            </hr>
            {comment}
            <hr>
            </hr>
            {comments.map(c => <Row>
                        <Col md={3}>
                            {/* <Image src={c.user.email} roundedCircle fluid/> */}
                            <p>By:{c.user.username}</p>
                            <p>{c.user.email}</p>
                        </Col>
                        <Col md={9}>
                            <p>Comment:{c.content}</p>
                            <p>Time: <Moment fromNow>{c.user.created_date}</Moment></p>
                        </Col>
            </Row>)}
            
        </>
    )
}