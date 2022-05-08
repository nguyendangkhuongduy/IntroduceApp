import axios from "axios";


export const endpoints = {
    "employer": "/employer/",
    "recruitment": "/recruitment/",
    "oauth2-info": "/oauth2-info/",
    "login": "/o/token/",
    "current-user": "/users/current-user/",
    "register": "/user/",
    // "comments": (lessonId) => `/lesson/${lessonId}/comments/`,
    // "add-comment": (lessonId) => `/lesson/${lessonId}/add-comment/`
}


export default axios.create({
    baseURL: "http://127.0.0.1:8000/"
})