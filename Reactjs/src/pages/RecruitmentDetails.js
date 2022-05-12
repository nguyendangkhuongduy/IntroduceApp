import { useEffect } from "react"
import { useState } from "react"
import { Col, Row, Spinner, Image, Badge } from "react-bootstrap"
import { Link, useParams } from "react-router-dom"
import Apis, { endpoints } from "../configs/Apis"



export default function RecruitmentDetails () {


    const [recruitment, SetRecruitment] = useState(null)

    let {recruitmentId} = useParams()

    useEffect(() =>{
        let loadRecruitment = async () => {
            try {
                let res = await Apis.get(endpoints['recruitment-detail'](recruitmentId))
                SetRecruitment(res.data)
            } catch(err) {
                console.error(err)
            }
        }

        loadRecruitment()
    }, [])

    
    
    // let myHTML = <p>{recruitment.content}</p>
    // let s = myHTML.replace(/<[^>]+>/g, '');

    if(recruitment === null)
        return <Spinner animation="border" />

    let path = `/recruitment/${recruitmentId}`


      



    return (  
        <>
               
            <h1 className="text-danger text-center">Details Jobs</h1>

            <Row>
                <Col md={4} xs={12}>
                    <Link to={path}>
                        <Image src={recruitment.image} rounded fluid />
                    </Link>
                     {/* <Image src={employer.image} rounded fluid /> */}
                </Col>
                <Col md={8} xs={12}>
                    <h2>Jobs name:{recruitment.title}</h2>
                    <p>Contact: {recruitment.contact_name}</p>
                    <p>Phone: {recruitment.phone_number}</p>
                    <p>Date join: {(recruitment.created_date)}</p>
                    <p>Date update: {recruitment.updated_date}</p>
                    <p>
                        {recruitment.tags.map(t => <Badge style={{backgroundColor: "blue"}} bg="secondary">{t.name}</Badge>)}
                    </p>
                    <h1>Infor Company:</h1>
                    <p>Email: {recruitment.employer.email}</p>
                    <p>Phone: {recruitment.employer.phone_number}</p>
                    <p>Join: {recruitment.employer.created_date}</p>


                    <p></p>

                </Col>
            </Row>
            <hr/>
            <div>
                <h2>Description about job:</h2>
                {/* <p>{s}</p> */}
                <div
                    dangerouslySetInnerHTML={{
                        __html: recruitment.content,
                    }}
                />
                <p></p>
                {/* <RichTextField source={recruitment.content} stripTags /> */}
                {/* <RichTextField><p>{recruitment.content}</p></RichTextField> */}
            </div>
        </>
    )
}