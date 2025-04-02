// paycheck-bill-field.component.ts
import {Component, HostBinding, Input} from "@angular/core";
import {PaycheckFieldType} from "../paycheck/models/PaycheckFieldType";
import {Bill} from "../../../models/bill/Bill";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'paycheck-bill-field',
    templateUrl: './paycheck-bill-field.component.html',
    styleUrls: ['./paycheck-bill-field.component.css']
})
export class PaycheckBillFieldComponent {
    @Input() protected fieldType: PaycheckFieldType;
    @Input() protected bill: Bill;
    @HostBinding('class.bill-text') get isAmount(): boolean {
        return this.fieldType === PaycheckFieldType.AMOUNT;
    }
    constructor() {
        
    }
    protected getFieldValue(): string {
        switch (this.fieldType) {
            case PaycheckFieldType.AMOUNT:
                return `-$${this.bill.amount}`;
            case PaycheckFieldType.DATE:
                return this.bill.date.toDateString();
            case PaycheckFieldType.TIME_TYPE:
                return this.bill.timeType;
            default:
                return '';
        }
    }

    protected readonly TagType = TagType;
}
