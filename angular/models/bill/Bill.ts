import {InputTimeType} from "../input/InputTimeType";
import {
    RecurringBillTimeInterval
} from "../../components/elements/element-group-bill/recurring-bill-dropdown/models/RecurringBillTimeInterval";

export class Bill {
    public name: string;
    public amount: number;
    public date: Date;
    public timeType: InputTimeType;
    public billInterval?: RecurringBillTimeInterval;
    public constructor(name: string = '',
                       amount: number = 0,
                       date: Date = new Date(),
                       timeType: InputTimeType = InputTimeType.ONE_TIME,
                       billInterval?: RecurringBillTimeInterval) {
        this.name = name;
        this.amount = amount;
        this.date = date;
        this.timeType = timeType;
        this.billInterval = billInterval;
    }
}