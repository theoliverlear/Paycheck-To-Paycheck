import {Paycheck} from "../models/paycheck/types";

export const emptyPaycheck: Paycheck = {
    dateRange: {
        endDate: new Date(),
        startDate: new Date()
    },
    leftOverIncome: 0,
    oneTimeBills: [],
    oneTimeIncomes: [],
    recurringBills: [],
    recurringIncomes: [],
    wageIncomes: [],
    totalBills: 0,
    totalIncome: 0
};

export function isEmptyPaycheck(paycheck: Paycheck): boolean {
    return emptyPaycheck === paycheck;
}