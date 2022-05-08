import { useState } from "react"
import { useEffect } from "react"
import { Row } from "react-bootstrap"
import Apis, { endpoints } from "../configs/Apis"
// import Apis, { endpoints } from "../configs/Apis"
import FormIntroduc from "../layout/FromIntroduc"


export default function Home () {
    const [recruitment, setRecruitment] = useState()


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
            <h1 className="text-center text-danger">ALL JOBS</h1>
            {/* <Row>
                {recruitment.map(c => <FormIntroduc obj={c} />)}
            </Row> */}

            {/* {recruitment.map(c =>
                    {
                        return <FormIntroduc image={c.image} name={c.name} created_date={c.created_date} />
                    })} */}
                     
        </>
    )
}