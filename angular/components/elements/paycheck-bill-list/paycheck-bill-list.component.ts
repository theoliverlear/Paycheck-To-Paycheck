// paycheck-bill-list.component.ts 
import {Component, Input} from "@angular/core";
import {OneTimeBill, RecurringBill} from "../../../models/paycheck/types";

@Component({
    selector: 'paycheck-bill-list',
    templateUrl: './paycheck-bill-list.component.html',
    styleUrls: ['./paycheck-bill-list.component.css']
})
export class PaycheckBillListComponent {
    @Input() bills: (OneTimeBill | RecurringBill)[];
    constructor() {
        
    }
}
