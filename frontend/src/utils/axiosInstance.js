// frontend/src/utils/axiosInstance.js
import axios from 'axios';

const instance = axios.create({
  baseURL: process.env.REACT_APP_API_URL || '', // default fallback
});

export default instance;
