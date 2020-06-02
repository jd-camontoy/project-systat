export interface CurrentPeriod {
    id: number,
    period_name: string,
    period_start_date: string,
    period_end_date: string
}

export interface Defect {
    id: number,
    defect_description: string,
    date_reported: string,
    date_fixed_released: string
}

export interface System {
    id: number,
    system_name: string,
    percentage: number,
    defects?: Defect[]
}