// paycheck-income.component.ts
import {Component, Input} from "@angular/core";
import {Income} from "../../../models/income/Income";
import {InputTimeType} from "../../../models/input/InputTimeType";
import {TagType} from "../../../models/html/TagType";
import {
    PaycheckIncomeFieldType
} from "../paycheck-income-field/models/PaycheckIncomeFieldType";

@Component({
    selector: 'paycheck-income',
    templateUrl: './paycheck-income.component.html',
    styleUrls: ['./paycheck-income.component.css']
})
export class PaycheckIncomeComponent {
    @Input() protected income: Income;
    constructor() {

    }
    protected getIncomeAmount(): string {
        return `$${this.income.incomeAmount}`;
    }
    protected readonly TagType = TagType;
    protected readonly String = String;
    protected readonly PaycheckIncomeFieldType = PaycheckIncomeFieldType;
}
