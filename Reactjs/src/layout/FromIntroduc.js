import { Card, Col } from "react-bootstrap";

export default function FromIntroduc(props) {
    return (
        <Col md={4}>
            <Card>
                <Card.Img variant="top" src={props.obj.image} />
                <Card.Body>
                    <Card.Title>{props.obj.name}</Card.Title>
                    <Card.Text>
                        Created_date: {props.obj.created_date}
                    </Card.Text>
                </Card.Body>
            </Card>
        </Col> 
    )
}