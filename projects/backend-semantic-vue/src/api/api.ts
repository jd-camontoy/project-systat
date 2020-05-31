import axios from "axios";
import { CurrentPeriod } from "@/api/interface";

const baseURL = 'http://localhost:5000';

const api = axios.create({
    baseURL,
    headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PATCH, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
    }
});

export async function getCurrentPeriod(): Promise<CurrentPeriod> {
    try {
        const response = await api.get('/period');
        return (response.data as CurrentPeriod);
    } catch (error) {
        throw new Error(error);
    }
}
