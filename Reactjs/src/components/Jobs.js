import { Card, Col, Row, Button, Container } from "react-bootstrap"

const Jobs = () => {
    return (
        <Container>
            <h1 className="text-center">ALL JOBS</h1>

            <Row>
                <Col md={4} xs={12}>
                    <Card>
                        <Card.Img variant="top" src="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647930931/laoxgo0d5zx1jnwxbyqr.jpg" />
                        <Card.Body>
                            <Card.Title>ReactJs</Card.Title>
                            <Card.Text>
                            Nguyen Dang Khuong Duy
                            </Card.Text>
                            <Button variant="primary">Detail</Button>
                        </Card.Body>
                    </Card>
                </Col>

                <Col md={4} xs={12}>
                    <Card>
                        <Card.Img variant="top" src="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647930931/laoxgo0d5zx1jnwxbyqr.jpg" />
                        <Card.Body>
                            <Card.Title>ReactJs</Card.Title>
                            <Card.Text>
                            QQ
                            </Card.Text>
                            <Button variant="primary">Detail</Button>
                        </Card.Body>
                    </Card>
                </Col>

                <Col md={4} xs={12}>
                    <Card>
                        <Card.Img variant="top" src="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647930931/laoxgo0d5zx1jnwxbyqr.jpg" />
                        <Card.Body>
                            <Card.Title>ReactJs</Card.Title>
                            <Card.Text>
                            Nguyen Nguyen
                            </Card.Text>
                            <Button variant="primary">Detail</Button>
                        </Card.Body>
                    </Card>
                </Col>

                <Col md={4} xs={12}>
                    <Card>
                        <Card.Img variant="top" src="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647930931/laoxgo0d5zx1jnwxbyqr.jpg" />
                        <Card.Body>
                            <Card.Title>ReactJs</Card.Title>
                            <Card.Text>
                            Nguyen Dang Khuong Duy
                            </Card.Text>
                            <Button variant="primary">Detail</Button>
                        </Card.Body>
                    </Card>
                </Col>

                <Col md={4} xs={12}>
                    <Card>
                        <Card.Img variant="top" src="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647930931/laoxgo0d5zx1jnwxbyqr.jpg" />
                        <Card.Body>
                            <Card.Title>ReactJs</Card.Title>
                            <Card.Text>
                            Nguyen Dang Khuong Duy
                            </Card.Text>
                            <Button variant="primary">Detail</Button>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
    )
}

export default Jobs