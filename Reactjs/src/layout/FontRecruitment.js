import { Card, Col } from "react-bootstrap";
import { Link } from "react-router-dom";

export default function FontRecruitment(props) {
    let path = `/employer/${props.obj.id}`
    return (
        <Col md={4}>
            <Card>
                <Link to={path}>
                    <Card.Img variant="top" src={props.obj.image} />
                </Link>
                <Card.Body>
                    {/* <Card.Title>{props.obj.title}</Card.Title> */}
                    <Card.Text>
                        {props.obj.name}
                        <br></br>
                        Phone: {props.obj.phone_number}
                        <br></br>
                        Email: {props.obj.email}
                    </Card.Text>
                </Card.Body>
            </Card>
        </Col> 
    )
}