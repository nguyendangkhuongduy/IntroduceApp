import { Card, Col } from "react-bootstrap";
import { Link } from "react-router-dom";

export default function FontCompany(props) {

    let path = `/recruitment/${props.obj.id}/`

    return (
        <Col md={4}>
            <Card>
                <Link to = {path}>
                    <Card.Img variant="top" src={props.obj.image} />
                </Link>
                
                <Card.Body>
                    <Card.Title>Job:{props.obj.title}</Card.Title>
                    <Card.Text>
                        Phone: {props.obj.phone_number}
                        <br></br>
                        Date: {props.obj.created_date}
                        <br></br>
                        Quantity: {props.obj.number}
                    </Card.Text>
                </Card.Body>
            </Card>
        </Col> 
    )
}