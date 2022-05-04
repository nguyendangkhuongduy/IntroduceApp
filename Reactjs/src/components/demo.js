import { useNavigate } from "react-router-dom";

const nav = useNavigate()

const goToLesson = () => {
    nav(`/courses/${props.id}/ lesson`)
}