import axios from "axios";


export const endpoints = {
    "employer": "/employer/",
    "recruitment": "/recruitment/",
    "employer-detail": (employerId) => `/employer/${employerId}/`,
    "recruitment-detail": (recruitmentId) => `/recruitment/${recruitmentId}/`,
    "employer-recruitment": (employerId) => `/employer/${employerId}/recruitment/`,
    "oauth2-info": "/oauth2-info/",
    "login": "/o/token/",
    "current-user": "/users/current-user/",
    "register": "/users/",
    "comments": (employerId) => `/employer/${employerId}/get-comment/` ,
    "add-comment": (employerId) => `/employer/${employerId}/add-comment/`
    // "comments": (lessonId) => `/lesson/${lessonId}/comments/`,
    // "add-comment": (lessonId) => `/lesson/${lessonId}/add-comment/`
}


export const authApi = () => {
    return axios.create({
        baseURL: "http://127.0.0.1:8000/",
        headers: {
            Authorization: `Bearer sFLxOyBKHk88KhuWrZm6gCygTNQCKW`
        }
    })
}

export default axios.create({
    baseURL: "http://127.0.0.1:8000/"
})