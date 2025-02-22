import {InputTimeType} from "../input/InputTimeType";
import {
    RecurringBillTimeInterval
} from "../../components/elements/recurring-bill-dropdown/models/RecurringBillTimeInterval";

export class Bill {
    public title: string;
    public amount: number;
    public date: Date;
    public timeType: InputTimeType;
    public billInterval?: RecurringBillTimeInterval;
    public constructor(title: string = '',
                       amount: number = 0,
                       date: Date = new Date(),
                       timeType: InputTimeType = InputTimeType.ONE_TIME,
                       billInterval?: RecurringBillTimeInterval) {
        this.title = title;
        this.amount = amount;
        this.date = date;
        this.timeType = timeType;
        this.billInterval = billInterval;
    }
}