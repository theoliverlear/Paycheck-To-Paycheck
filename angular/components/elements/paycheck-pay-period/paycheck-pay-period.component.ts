// paycheck-pay-period.component.ts 
import {Component, Input} from "@angular/core";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'paycheck-pay-period',
    templateUrl: './paycheck-pay-period.component.html',
    styleUrls: ['./paycheck-pay-period.component.css']
})
export class PaycheckPayPeriodComponent {
    @Input() protected startDate: Date;
    @Input() protected endDate: Date;
    constructor() {
        
    }

    protected getPayPeriodText(): string {
        return this.startDate.toDateString() + ' - ' + this.endDate.toDateString();
    }
    protected readonly TagType = TagType;
}
