// paycheck-income-field.component.ts
import {Component, HostBinding, Input} from "@angular/core";
import {Income} from "../../../models/income/Income";
import {PaycheckIncomeFieldType} from "./models/PaycheckIncomeFieldType";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'paycheck-income-field',
    templateUrl: './paycheck-income-field.component.html',
    styleUrls: ['./paycheck-income-field.component.css']
})
export class PaycheckIncomeFieldComponent {
    @Input() protected fieldType: PaycheckIncomeFieldType
    @Input() protected income: Income;
    @HostBinding('class.income-text') get isAmount() {
        return this.fieldType === PaycheckIncomeFieldType.AMOUNT;
    }
    constructor() {
        
    }
    protected getFieldValue() {
        switch (this.fieldType) {
            case PaycheckIncomeFieldType.AMOUNT:
                return `+$${this.income.incomeAmount}`;
            case PaycheckIncomeFieldType.DATE_RECEIVED:
                return this.income.dateReceived.getDate();
            case PaycheckIncomeFieldType.TIME_TYPE:
                return this.income.timeType;
            default:
                return '';
        }
    }

    protected readonly TagType = TagType;
}
