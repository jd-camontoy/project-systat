import axios from "axios";
import { 
    CurrentPeriod,
    System,
    Defect
} from "@/api/interface";

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

export async function getDefects(systemId : number) : Promise<Defect[]> {
    try {
        const response = await api.get(`/defect?system_status_id=${systemId}`);
        const defects = [];
        for (const defect of response.data) {
            defects.push(defect as Defect);
        }
        return defects;
    } catch (error) {
        throw new Error(error);
    }
}

export async function getSystems(): Promise<System[]> {
    try {
        const periodId = localStorage.currentPeriodId;
        const response = await api.get(`/system?period_id=${periodId}`);
        const systems = [];
        for (const system of response.data) {
            systems.push(system as System);
        }
        return systems;
    } catch (error) {
        throw new Error(error);
    }
}