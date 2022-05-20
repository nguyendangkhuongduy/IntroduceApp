import { useEffect } from "react"
import { useState } from "react"
import { Col, Row, Spinner, Image, Form, div } from "react-bootstrap"
import { Link, useNavigate, useParams } from "react-router-dom"
import Apis, { authApi, endpoints } from "../configs/Apis"
import { Button } from "react-bootstrap";
import Moment from "react-moment"
import { useSelector } from "react-redux"
import Rating from "react-rating"
// import cookies from "react-cookies"

export default function EmployerDetails () {

  
    const [employer, SetEmployer] = useState(null)
    const [deletee, SetDelete] = useState(null)
    const [comments, Setcomments] = useState([])
    const [commentContent, SetCommentContent] = useState([])
    const [change, SetChange] = useState(1)
    const [changee, SetChangee] = useState(1)
    const [rating, SetRating] = useState(0)

    const nav = useNavigate()

    let user  = useSelector(state => state.user.user)
    let {employerId} = useParams()
    let comment = <em><Link to="/login">Log In</Link> to comment <h3 className="text-danger">Note: No comment or rating for Company account</h3></em>
    let r = ""
    let path = `/employer/${employerId}/recruitment/`

    const saveRating = async(rate) => {
        if(window.confirm("do you want to rate this company?")==true) {
            try {
                let res = await authApi().post(endpoints['rating'](employerId), {
                    "rating" : rate
                })

                console.info(res.data)
            } catch(err) {
                console.error(err)
            }
        }
    }


    const addComment = async (event) => {
        event.preventDefault()

        try {
            const res = await authApi().post(endpoints['add-comment'](employerId), {
                "content": commentContent }
            )
            console.info(res.data)
            comments.push(res.data)
            Setcomments(comments)
            SetChange(comments.length)

            
        } catch (err) {
            console.info(err)
        }

    }

    const deleteCompany = async (event) => {
        event.preventDefault()

        try {
            let delete_company = async () => {
                try {
                    let res = await Apis.delete(endpoints['delete_employer'](employerId))
                    SetDelete(res.data)
                } catch (err) {
                    console.error(err)
                }
            }
            SetEmployer(employer)
            SetChangee(employer.count)
            delete_company()
            nav(`/home`)
           
        } catch (err) {
            console.info(err)
        }

    }

    let u = ""
    if(user !== null && user !== undefined && user.Role == "3") {
        u = <>
        <Form onSubmit={deleteCompany}>
            <Button variant="primary" type="submit">
                    Delete
                </Button>
        </Form>
        </> 
    }


   

    useEffect(() =>{
        let loadEmployer = async () => {
            try {
                let res = await authApi().get(endpoints['employer-detail'](employerId))
                SetEmployer(res.data)   
                console.info(res.data)
                SetRating(res.data.rate)
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
    }, [change, changee])
    

    if(employer === null)
        return <Spinner animation="border" />

    if (user !== null && user !== undefined && user.Role !== "2")  {
        comment = <Form onSubmit={addComment}> 
        <Form.Group className="mb-3" controlId="commentControl">
            <Form.Control type="text" value={commentContent} onChange={(event) => SetCommentContent(event.target.value)}
                                    placeholder="Type comment..." rows={3} />
            </Form.Group>
            <Button type="submit" onclick="alert('Học Code Tốt Xin chào các bạn')" variant="info">Send</Button>
        </Form>
    
            r = <Rating
            initialRating={rating} onClick={saveRating}
            // readonly
          />
        }
    
        
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
                    <p>{r}</p>
                    {u}
                </Col>
            </Row>
            <hr/>
            <p>Descriptions:</p>
            <div className="text-center"
                    dangerouslySetInnerHTML={{
                        __html: employer.description,
                    }}
                /> 
            <hr />
            {comment}
            <hr>
            </hr>
            {comments.map(c => <Row>
                        <Col md={3}>
                            <Image src={employer.image} roundedCircle fluid/>
                            {/* <p>By:{c.user.username}</p> */}
                            <p>By:{user.username}</p>
                        </Col>
                        <Col md={9}>
                            <p>{c.content}</p>
                            <p>Time: <Moment fromNow>{c.user.created_date}</Moment></p>
                        </Col>
            </Row>)}
            
        </>
    )
}