import {InputTimeType} from "../input/InputTimeType";
import {
    RecurringIncomeTimeInterval
} from "../../components/elements/recurring-income-dropdown/models/RecurringIncomeTimeInterval";

export class Income {
    public name: string;
    public amount: number;
    public date: Date;
    public timeType: InputTimeType;
    public incomeInterval?: RecurringIncomeTimeInterval;
    public hours?: number;
    public constructor(name: string = '',
                       amount: number = 0,
                       date: Date = new Date(),
                       timeType: InputTimeType = InputTimeType.ONE_TIME,
                       incomeInterval?: RecurringIncomeTimeInterval,
                       hours?: number) {
        this.name = name;
        this.amount = amount;
        this.date = date;
        this.timeType = timeType;
        this.incomeInterval = incomeInterval;
        this.hours = hours;
    }
}