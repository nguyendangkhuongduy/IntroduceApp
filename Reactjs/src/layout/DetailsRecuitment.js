import { Card, Col } from "react-bootstrap";
import { Link } from "react-router-dom";

export default function DetailsRecuitment(props) {

    let path = `/employerdetail/${props.obj.id}`

    return (
        <Col md={4}>
            <Card>
                <Link to={path}>
                    <Card.Img variant="top" src={props.obj.image} />
                </Link>
                <Card.Body>
                    <Card.Title>{props.obj.name}</Card.Title>
                    <Card.Text>
                        Phone: {props.obj.phone_number}
                    </Card.Text>
                </Card.Body>
            </Card>
        </Col>
    )
}