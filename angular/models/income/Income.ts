import {InputTimeType} from "../input/InputTimeType";
import {
    RecurringIncomeTimeInterval
} from "../../components/elements/recurring-income-dropdown/models/RecurringIncomeTimeInterval";

export class Income {
    public title: string;
    public amount: number;
    public date: Date;
    public timeType: InputTimeType;
    public incomeInterval?: RecurringIncomeTimeInterval;
    public hours?: number;
    public constructor(title: string = '',
                       amount: number = 0,
                       date: Date = new Date(),
                       timeType: InputTimeType = InputTimeType.ONE_TIME,
                       incomeInterval?: RecurringIncomeTimeInterval,
                       hours?: number) {
        this.title = title;
        this.amount = amount;
        this.date = date;
        this.timeType = timeType;
        this.incomeInterval = incomeInterval;
        this.hours = hours;
    }
}