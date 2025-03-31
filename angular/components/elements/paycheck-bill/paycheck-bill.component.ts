// paycheck-bill.component.ts 
import {Component, Input} from "@angular/core";
import {Bill} from "../../../models/bill/Bill";

@Component({
    selector: 'paycheck-bill',
    templateUrl: './paycheck-bill.component.html',
    styleUrls: ['./paycheck-bill.component.css']
})
export class PaycheckBillComponent {
    @Input() protected bill: Bill;
    constructor() {
        
    }
}
