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
    "add-comment": (employerId) => `/employer/${employerId}/add-comment/`,
    "rating": (employerId) => `/employer/${employerId}/rating/`,
    "company_user": (userId) => `/users/${userId}/company/`,
    "profile": (userId) => `/users/${userId}/profile/`,
    "education": (profileId) => `/profile/${profileId}/education/`,
    "experience": (profileId) => `/profile/${profileId}/experience/`,
    "cv": (userId) => `/users/${userId}/cv/`,
    "delete_recruitment": (recruitmentId) => `/recruitment/${recruitmentId}/`,
    "delete_employer": (employerId) => `/employer/${employerId}/`
}


export const authApi = () => {
    return axios.create({
        baseURL: "http://127.0.0.1:8000/",
        headers: {
            Authorization: `Bearer lXoxSOjCuAZ6w23HtV7kZeTGp0DS6D`
        }
    })
}

export default axios.create({
    baseURL: "http://127.0.0.1:8000/"
})

// qfk1z1sbGxFoNcNEktQPGzD8EDPtK7