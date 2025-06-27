// paycheck-bill-fields.component.ts 
import {Component, Input} from "@angular/core";
import {Bill} from "../../../../models/bill/Bill";
import {PaycheckFieldType} from "../paycheck/models/PaycheckFieldType";
import {OneTimeBill, RecurringBill} from "../../../../models/paycheck/types";

@Component({
    selector: 'paycheck-bill-fields',
    templateUrl: './paycheck-bill-fields.component.html',
    styleUrls: ['./paycheck-bill-fields.component.css']
})
export class PaycheckBillFieldsComponent {
    @Input() protected bill: OneTimeBill | RecurringBill;
    constructor() {
        
    }

    protected readonly PaycheckFieldType = PaycheckFieldType;
}
