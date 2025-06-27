// paycheck-bill-field.component.ts
import {Component, HostBinding, Input} from "@angular/core";
import {PaycheckFieldType} from "../paycheck/models/PaycheckFieldType";
import {Bill} from "../../../../models/bill/Bill";
import {TagType} from "../../../../models/html/TagType";
import {OneTimeBill, RecurringBill} from "../../../../models/paycheck/types";
import {InputTimeType} from "../../../../models/input/InputTimeType";

@Component({
    selector: 'paycheck-bill-field',
    templateUrl: './paycheck-bill-field.component.html',
    styleUrls: ['./paycheck-bill-field.component.css']
})
export class PaycheckBillFieldComponent {
    @Input() protected fieldType: PaycheckFieldType;
    @Input() protected bill: OneTimeBill | RecurringBill;
    @HostBinding('class.bill-text') get isAmount(): boolean {
        return this.fieldType === PaycheckFieldType.AMOUNT;
    }
    constructor() {
        
    }
    protected getFieldValue(): string {
        switch (this.fieldType) {
            case PaycheckFieldType.AMOUNT:
                const amountFormatted: string = new Intl.NumberFormat('en-US', {
                        style: 'currency',
                        currency: 'USD',
                        minimumFractionDigits: 2
                    }).format(this.bill.amount);
                return `-${amountFormatted}`;
            case PaycheckFieldType.DATE:
                if ('dueDate' in this.bill) {
                    if (this.bill.dueDate) {
                        return this.bill.dueDate.dueDate.toDateString();
                    }
                } else {
                    if (this.bill.recurringDate) {
                        return this.bill.recurringDate.day.toDateString();
                    }
                }
                return 'N/A';
            case PaycheckFieldType.TIME_TYPE:
                if ('recurringDate' in this.bill) {
                    return InputTimeType.RECURRING;
                } else {
                    return InputTimeType.ONE_TIME;
                }
            default:
                return '';
        }
    }

    protected readonly TagType = TagType;
}
