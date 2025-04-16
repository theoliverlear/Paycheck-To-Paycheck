// paycheck-income-field.component.ts
import {Component, HostBinding, Input} from "@angular/core";
import {Income} from "../../../models/income/Income";
import {PaycheckFieldType} from "../paycheck/models/PaycheckFieldType";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'paycheck-income-field',
    templateUrl: './paycheck-income-field.component.html',
    styleUrls: ['./paycheck-income-field.component.css']
})
export class PaycheckIncomeFieldComponent {
    @Input() protected fieldType: PaycheckFieldType
    @Input() protected income: Income;
    @HostBinding('class.income-text') get isAmount(): boolean {
        return this.fieldType === PaycheckFieldType.AMOUNT;
    }
    constructor() {
        
    }
    protected getFieldValue(): string {
        switch (this.fieldType) {
            case PaycheckFieldType.AMOUNT:
                return `+$${this.income.amount}`;
            case PaycheckFieldType.DATE:
                return this.income.dateReceived.toDateString();
            case PaycheckFieldType.TIME_TYPE:
                return this.income.timeType;
            default:
                return '';
        }
    }

    protected readonly TagType = TagType;
}
