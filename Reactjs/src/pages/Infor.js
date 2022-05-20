import { useState } from "react";
import { useEffect } from "react";
import { Badge, Card} from "react-bootstrap";
import {useSelector } from "react-redux";
import Apis, { authApi, endpoints } from "../configs/Apis";


export default function Infor() {

    const [company, SetCompany] = useState([])
    const [profile, SetProfile] = useState([])
    const [education, SetEducation] = useState([])
    const [experience, SetExperience] = useState([])
    const [cv, SetCv] = useState([])
    const [num, SetNum] = useState(0)

    const user = useSelector(state => state.user.user)

    // let a = "1"

        

    useEffect(() => {
        let loadCompany = async () => {
            try {
                let res = await authApi().get(endpoints['company_user'](user.id))
                SetCompany(res.data)
            } catch(err) {
                console.error(err)
            }
        }

        let loadProfile = async () => {
            try {
                let res = await authApi().get(endpoints['profile'](user.id))
                SetProfile(res.data)
            } catch (err) {
                console.error(err)
            }
        }

        let loadEducation = async () => {
            try {
                let res = await Apis.get(endpoints['education'](profile.id))
                SetEducation(res.data)
            } catch (err) {
                console.error(err)
            }
        }

        let loadExperience = async () => {
            try {
                let res = await Apis.get(endpoints['experience'](profile.id))
                SetExperience(res.data)
            } catch (err) {
                console.error(err)
            }
        }

        let loadCV = async () => {
            try {
                let res = await Apis.get(endpoints['cv'](user.id))
                SetCv(res.data)
            } catch (err) {
                console.error(err)
            }
        }

            
            loadCompany()
            loadProfile()
            loadCV()
            loadEducation()
            loadExperience()
            // SetNum(num => num + 1)
        },[])

        let info = ""

        if (user !== null && user !== undefined && (user.Role === "2" && user.Role !== "3"))  {
            info = <><h1 className="text-center text-danger">Company Infor</h1>
            <p className="text-center">Join date: {company.created_date}</p>
            <p className="text-center">Company name: {company.name}</p>
            <p className="text-center">Phone: {company.phone_number}</p>
            <div>
                <h2 className="text-center text-danger">Description about Company:</h2>
                {/* <p>{s}</p> */}
                <div className="text-center"
                    dangerouslySetInnerHTML={{
                        __html: company.description,
                    }}
                />

            </div>
            </>
        }
        else if (user !== null && user !== undefined && user.Role === "1" && user.Role !== "2" && user.Role !== "3")  {
            info = <>
                <h1 className="text-center text-danger"> Your Profile </h1>
                <p className="text-center">Full name: {profile.full_name}</p>
                <p className="text-center">Phone: {profile.phone_number}</p>
                <p className="text-center">Gender: {profile.gender}</p>
                <p className="text-center">Date of birth: {profile.date_of_birth}</p>
                {/* <p className="text-center">Skill: {profile.skills}</p> */}
                <p className="text-center">Skills:
                <h3 
                    dangerouslySetInnerHTML={{
                        __html: profile.skills,
                    }}
                /> 
                </p>
                <h1 className="text-center text-danger">Education</h1>
                <p className="text-center" >Degree: {education.degree}</p>
                <p className="text-center">Major: {education.major}</p>
                <p className="text-center">Time start:{education.time_start}</p>
                <p className="text-center" >Time completed: {education.time_completed}</p>

                <h1 className="text-center text-danger">Experience</h1>
                <p className="text-center" >Jobs: {experience.job}</p>
                <p className="text-center">Position: {experience.position}</p>
                <p className="text-center">Time start:{experience.time_start}</p>
                <p className="text-center" >Time completed: {experience.time_end}</p>

                <h1 className="text-center text-danger">CV</h1>
                <p className="text-center" >Titile: {cv.title}</p>
                <p className="text-center">cv_url: <a href="">{cv.cv}</a> </p>

            </>
        }

    return (
        <>
            <h1 className="text-danger text-center">ProFile: {user.username}</h1>
            <Card.Img variant="top" src={user.avatar} />
            <h1 className="text-center text-danger">User Infor</h1>
            <p className="text-center">Username: {user.username}</p>
            <p className="text-center">Full name: {user.first_name} {user.last_name}</p>
            <p className="text-center">Email: {user.email}</p>
            <p className="text-center">Time join: {user.date_joined}</p>
            {info}
     
            
            {/* <p>
                {company.address.map(t => <Badge style={{backgroundColor: "blue"}} bg="secondary">{t.name}</Badge>)}
            </p> */}

        </>
    )
}