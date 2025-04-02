// paycheck-income-fields.component.ts 
import {Component, Input} from "@angular/core";
import {Income} from "../../../models/income/Income";
import {
    PaycheckFieldType
} from "../paycheck/models/PaycheckFieldType";

@Component({
    selector: 'paycheck-income-fields',
    templateUrl: './paycheck-income-fields.component.html',
    styleUrls: ['./paycheck-income-fields.component.css']
})
export class PaycheckIncomeFieldsComponent {
    @Input() protected income: Income;
    constructor() {
        
    }

    protected readonly PaycheckFieldType = PaycheckFieldType;
}
