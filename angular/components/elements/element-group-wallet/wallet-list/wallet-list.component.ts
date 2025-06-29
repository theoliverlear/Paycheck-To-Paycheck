// wallet-list.component.ts 
import { Component, Input } from "@angular/core";
import {TagType} from "../../../../models/html/TagType";
import {ElementSize} from "../../../../models/ElementSize";
import {
    ButtonText
} from "../../element-group-native/ss-button/models/ButtonText";
import {Wallet} from "../../../../models/wallet/types";
import {emptyWallet} from "../../../../assets/walletAssets";

@Component({
    selector: 'wallet-list',
    templateUrl: './wallet-list.component.html',
    styleUrls: ['./wallet-list.component.css']
})
export class WalletListComponent {
    @Input() wallet: Wallet = emptyWallet;
    constructor() {
        
    }

    protected readonly TagType = TagType;
    protected readonly ElementSize = ElementSize;
    protected readonly ButtonText = ButtonText;
}
