// import { Alert, link } from "react-bootstrap"
import './Footerr.css'

const Footer = () => {
    return (
        // <Alert variant="success">
        //     <Alert.Heading>Hey, nice to see you</Alert.Heading>
        //     <p>
        //         Aww yeah, you successfully read this important alert message. This example
        //         text is going to run a bit longer so that you can see how spacing within an
        //         alert works with this kind of content.
        //     </p>
        // </Alert>
        <>
        {/* <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" />
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css" integrity="sha384-oS3vJWv+0UjzBfQzYUhtDYW+Pj2yciDJxpsK1OYPAYjqT085Qq/1cq5FLXAZQ7Ay" crossorigin="anonymous" />
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" /> */}
        <body>
            <div id="container">
                <div id="part1">
                    <div id="companyinfo">
                        <a id="sitelink" href="#">QDcompany</a>
                        <p id="title">Job search for information technology people</p>
                        <p id="detail">We create the best environment for applicants and employers</p>
                    </div>
                    {/* <div id="explore">
                        <p id="txt1">About Us</p>
                        <a class="link" href="#">Home</a>
                        <a class="link" href="#">About</a>
                        <a class="link" href="#">Snippet</a>
                        <a class="link" href="#">Careers</a>
                    </div> */}
                    <div id="explore">
                        <p id="txt2">Visit</p>
                        <p class="text">Home</p>
                        <p class="text">About</p>
                        <p class="text">Snippet</p>
                        <p class="text">Careers</p>
                       
                    </div>
                    <div id="visit">
                        <p id="txt2">Visit</p>
                        <p class="text">Lincoln House </p>
                        <p class="text">Ho Chi Minh </p>
                        <p class="text">Mumbai 400 026 </p>
                        <p class="text">Phone: (22) 2363-3611 </p>
                        <p class="text">Fax: (22) 2363-0350 </p>
                    </div>

                    <div id="legal">
                        <p id="txt2">Terms & Conditions</p>
                        <p class="text">Operating Regulation</p>
                        <p class="text">Complaint Handling</p>
                        <p class="text">Private Policy</p>
                        <p class="text">Terms and Conditions</p>
                    </div>
                    {/* <div id="legal">
                        <div id="txt3">Terms & Conditions</div>
                        <a class="link1" href="#">Operating Regulation</a>
                        <a class="link1" href="#">Complaint Handling</a>
                        <a class="link1" href="#">Private Policy</a> 
                    </div> */}
                    <div id="subscribe">
                        <p id="txt4">Subscribe to US</p>
                        <form>
                            <input id="email" type="email" placeholder="Email" />
                        </form>
                        <a class="waves-effect waves-light btn">Subscribe</a>
                        <p id="txt5">Connect With US</p>
                        <i class="fab fa-facebook-square social fa-2x"></i>
                        <i class="fab fa-linkedin social fa-2x"></i>
                        <i class="fab fa-twitter-square social fa-2x"></i>
                    </div>  
                </div>
                <div id="part2">
                    <p id="txt6"><i class="material-icons tiny">Nguyen Dang Khuong Duy</i></p> 
                </div>
            </div>
        </body>
        </>
    )
    
}

export default Footer