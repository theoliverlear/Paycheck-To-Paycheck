// wallet.component.ts 
import {Component, Input} from "@angular/core";
import {Debt, Saving, Wallet} from "../../../../models/wallet/types";
import {TagType} from "../../../../models/html/TagType";
import {emptySaving} from "../../../../assets/walletAssets";

@Component({
    selector: 'wallet',
    templateUrl: './wallet.component.html',
    styleUrls: ['./wallet.component.css']
})
export class WalletComponent {
    @Input() walletItem: Saving | Debt = emptySaving;
    constructor() {
        
    }

    getAmountString(): string {
        return this.walletItem.amount.toLocaleString('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        });
    }

    getTypeString(): string {
        return this.walletItem.type;
    }

    protected readonly TagType = TagType;
}
