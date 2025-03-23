// paycheck-income-list.component.ts 
import {Component, Input} from "@angular/core";
import {Income} from "../../../models/income/Income";
import {InputTimeType} from "../../../models/input/InputTimeType";

@Component({
    selector: 'paycheck-income-list',
    templateUrl: './paycheck-income-list.component.html',
    styleUrls: ['./paycheck-income-list.component.css']
})
export class PaycheckIncomeListComponent {
    @Input() protected incomes: Income[] = [new Income(
        "Job at Target",
        540,
        new Date(),
        InputTimeType.ONE_TIME
    )];
    constructor() {
        
    }
}
