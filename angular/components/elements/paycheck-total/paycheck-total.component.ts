// paycheck-total.component.ts
import {
    ChangeDetectionStrategy,
    Component,
    HostBinding,
    Input
} from "@angular/core";
import {PaycheckTotalType} from "./models/PaycheckTotalType";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'paycheck-total',
    templateUrl: './paycheck-total.component.html',
    styleUrls: ['./paycheck-total.component.css'],
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class PaycheckTotalComponent {
    @Input() totalAmount: number;
    @Input() totalType: PaycheckTotalType;
    @HostBinding('class.income') protected get isIncome(): boolean {
        return this.totalType === PaycheckTotalType.INCOME;
    }
    @HostBinding('class.bill') protected get isBill(): boolean {
        return this.totalType === PaycheckTotalType.BILL;
    }
    @HostBinding('class.leftover') protected get isLeftover(): boolean {
        return this.totalType === PaycheckTotalType.LEFTOVER;
    }
    @HostBinding('class.negative-leftover') protected get isNegativeLeftover(): boolean {
        return this.totalAmount < 0 && this.totalType === PaycheckTotalType.LEFTOVER;
    }
    constructor() {
        
    }
    public getTotalTypeLabel(): string {
        return `${this.totalType}:`;
    }

    public getPaycheckTotalAmount(): string {
        return `$${this.totalAmount.toFixed(2)}`;
    }

    protected readonly TagType = TagType;
}
