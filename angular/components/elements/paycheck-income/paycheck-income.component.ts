// paycheck-income.component.ts
import {Component, Input} from "@angular/core";
import {Income} from "../../../models/income/Income";
import {TagType} from "../../../models/html/TagType";

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
        return `$${this.income.amount}`;
    }
    protected readonly TagType = TagType;
}
