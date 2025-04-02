// paycheck-bill.component.ts 
import {Component, Input} from "@angular/core";
import {Bill} from "../../../models/bill/Bill";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'paycheck-bill',
    templateUrl: './paycheck-bill.component.html',
    styleUrls: ['./paycheck-bill.component.css']
})
export class PaycheckBillComponent {
    @Input() protected bill: Bill;
    constructor() {
        
    }

    protected readonly TagType = TagType;
}
