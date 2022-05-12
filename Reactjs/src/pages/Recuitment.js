import { useEffect } from "react"
import { useState } from "react"
import { Row, Spinner } from "react-bootstrap"
import { useParams } from "react-router-dom"
import Apis, { endpoints } from "../configs/Apis"
import FontCompany from "../layout/FontCompany"
// import EmployerDetails from "./EmployerDetails"
// import DetailsEmployer from "../layout/DetailsEmployer"
// import FontCompany from "../layout/FontCompany"
// import DetailsRecuitment from "../layout/DetailsRec

export default function Recuitment () {
    
    const [recuitmentt, SetRecuitmentt] = useState([])

    const  { employerId } = useParams()

    useEffect(() => {
        let loadRecruitmentt = async () => {
            try {
                let res = await Apis.get(endpoints['employer-recruitment'](employerId))
                SetRecuitmentt(res.data)
            } catch(err) {
                console.error(err)
            }
        }

        loadRecruitmentt()
    }, [])

    return (    
        <>
            <h1 className="text-danger text-center">All jobs for company</h1>

            {recuitmentt.length == 0 && <Spinner animation="grow" />}

            <Row>
                {recuitmentt.map(c => {return <FontCompany obj={c} /> })}
            </Row>

        </>
    )
}