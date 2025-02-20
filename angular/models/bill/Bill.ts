import {InputTimeType} from "../input/InputTimeType";

export class Bill {
    public title: string;
    public amount: number;
    public date: Date;
    public timeType: InputTimeType;
    public constructor(title: string = '',
                       amount: number = 0,
                       date: Date = new Date(),
                       timeType: InputTimeType = InputTimeType.ONE_TIME) {
        this.title = title;
        this.amount = amount;
        this.date = date;
        this.timeType = timeType;
    }
}