import {InputTimeType} from "../input/InputTimeType";
import {
    RecurringIncomeTimeInterval
} from "../../components/elements/recurring-income-dropdown/models/RecurringIncomeTimeInterval";

export class Income {
    public name: string;
    public incomeAmount: number;
    public dateReceived: Date;
    public timeType: InputTimeType;
    public incomeInterval?: RecurringIncomeTimeInterval;
    public hours?: number;
    public constructor(name: string = '',
                       incomeAmount: number = 0,
                       dateReceived: Date = new Date(),
                       timeType: InputTimeType = InputTimeType.ONE_TIME,
                       incomeInterval?: RecurringIncomeTimeInterval,
                       hours?: number) {
        this.name = name;
        this.incomeAmount = incomeAmount;
        this.dateReceived = dateReceived;
        this.timeType = timeType;
        this.incomeInterval = incomeInterval;
        this.hours = hours;
    }
}