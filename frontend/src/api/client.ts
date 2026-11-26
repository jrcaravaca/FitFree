import axios from 'axios'; 

const api = axios.create({
    baseURL: 'http://1º27.0.0.1:8000/api',
    headers: {
        'Content-Type' : 'application/json'
    },
}); 

// Interceptor de petición, adjunta el access token si existe en localstorage

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token'); 
        if (token && config.headers) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config; 
    },
    (error) => Promise.reject(error)
); 

// Interceptor de respuesta, si el access token caduca intenta renovarlo con el refresh token
api.interceptors.response.use(
    (response) => response, 
    async (error) => {
        const originalRequest = error.config; 

        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true; 
            const refreshToken = localStorage.getItem('refresh_token');

            if (refreshToken) {
                try {
                    const {data} = await axios.post('http://127.0.0.1:8000/api/token/refresh/', {
                        refresh: refreshToken
                    });
                    localStorage.setItem('access_token', data.access);
                    originalRequest.headers.Authorization = `Bearer ${data.access}`;
                    return api(originalRequest);
                } catch {
                    localStorage.removeItem('access_token'); 
                    localStorage.removeItem('refresh_token'); 
                    window.location.href = '/login';
                }
            }
        }
        return Promise.reject(error);
    }
); 

export default api; 