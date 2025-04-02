// paycheck-bill-list.component.ts 
import {Component, Input} from "@angular/core";
import {Bill} from "../../../models/bill/Bill";

@Component({
    selector: 'paycheck-bill-list',
    templateUrl: './paycheck-bill-list.component.html',
    styleUrls: ['./paycheck-bill-list.component.css']
})
export class PaycheckBillListComponent {
    @Input() protected bills: Bill[];
    constructor() {
        
    }
}
