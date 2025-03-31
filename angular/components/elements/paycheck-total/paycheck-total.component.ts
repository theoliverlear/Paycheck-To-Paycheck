// paycheck-total.component.ts 
import {Component, Input} from "@angular/core";
import {PaycheckTotalType} from "./models/PaycheckTotalType";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'paycheck-total',
    templateUrl: './paycheck-total.component.html',
    styleUrls: ['./paycheck-total.component.css']
})
export class PaycheckTotalComponent {
    @Input() protected totalAmount: number;
    @Input() protected totalType: PaycheckTotalType;
    constructor() {
        
    }
    public getTotalTypeLabel(): string {
        return `${this.totalType}:`;
    }

    public getPaycheckTotalAmount(): string {
        return `$${this.totalAmount}`;
    }

    protected readonly TagType = TagType;
}
