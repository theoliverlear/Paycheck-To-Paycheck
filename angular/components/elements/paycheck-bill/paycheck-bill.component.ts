// paycheck-bill.component.ts 
import {Component, Input} from "@angular/core";
import {Bill} from "../../../models/bill/Bill";
import {TagType} from "../../../models/html/TagType";
import {OneTimeBill, RecurringBill} from "../../../models/paycheck/types";

@Component({
    selector: 'paycheck-bill',
    templateUrl: './paycheck-bill.component.html',
    styleUrls: ['./paycheck-bill.component.css']
})
export class PaycheckBillComponent {
    @Input() protected bill: OneTimeBill | RecurringBill;
    constructor() {
        
    }

    protected readonly TagType = TagType;
}
