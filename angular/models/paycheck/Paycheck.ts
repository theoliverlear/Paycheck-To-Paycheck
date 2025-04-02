import {Income} from "../income/Income";
import {Bill} from "../bill/Bill";

export class Paycheck {
    public startDate: Date;
    public endDate: Date;
    public incomes: Income[];
    public bills: Bill[];
    public totalIncome: number;
    public totalBills: number;
    public leftOverIncome: number;
    public constructor(startDate: Date = new Date(),
                       endDate: Date = new Date(),
                       incomes: Income[] = [],
                       bills: Bill[] = [],
                       totalIncome: number = 0.0,
                       totalBills: number = 0.0,
                       leftOverIncome: number = 0.0) {
        this.startDate = startDate;
        this.endDate = endDate;
        this.incomes = incomes;
        this.bills = bills;
        this.totalIncome = totalIncome;
        this.totalBills = totalBills;
        this.leftOverIncome = leftOverIncome;
    }
}