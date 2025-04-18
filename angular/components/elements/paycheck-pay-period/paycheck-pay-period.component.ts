// paycheck-pay-period.component.ts 
import {Component, Input} from "@angular/core";
import {TagType} from "../../../models/html/TagType";
import {DateRange} from "../../../models/paycheck/types";

@Component({
    selector: 'paycheck-pay-period',
    templateUrl: './paycheck-pay-period.component.html',
    styleUrls: ['./paycheck-pay-period.component.css']
})
export class PaycheckPayPeriodComponent {
    @Input() dateRange: DateRange;
    constructor() {
        
    }

    protected getPayPeriodText(): string {
        if (!this.dateRange) {
            return '';
        }
        return this.dateRange.startDate.toDateString() + ' - ' + this.dateRange.endDate.toDateString();
    }
    protected readonly TagType = TagType;
}
