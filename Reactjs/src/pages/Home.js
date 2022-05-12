import { useState } from "react"
import { useEffect } from "react"
import { Row } from "react-bootstrap"
import Apis, { endpoints } from "../configs/Apis"
import FontRecruitment from "../layout/FontRecruitment"



export default function Home () {
    const [recruitment, setRecruitment] = useState([])


    useEffect(() => {
        let loadRecruitment = async () => {
            try {
                let res = await Apis.get(endpoints['employer'])
                setRecruitment(res.data)
            } catch(err) {
                console.error(err)
            }      
        } 
        loadRecruitment()
        
    }, [])

    return (
        <>
            <h1 className="text-center text-danger">ALL Company</h1>
            <Row>
                {recruitment.map(d => <FontRecruitment obj={d} />)}
                
            </Row>        
                     
        </>
    )
}