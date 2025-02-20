// bill-input.component.ts
import {Component, HostBinding, Input, OnInit} from "@angular/core";
import {InputTimeType} from "../../../models/input/InputTimeType";
import {
    closeIconImageAsset, confirmIconImageAsset
} from "../../../assets/imageAssets";
import {TagType} from "../../../models/html/TagType";
import {fadeInOutAnimation} from "../../animations/animations";
import {
    quickFadeInAnimationProperties
} from "../../animations/animationProperties";
import {Bill} from "../../../models/bill/Bill";

@Component({
    selector: 'bill-input',
    templateUrl: './bill-input.component.html',
    styleUrls: ['./bill-input.component.css'],
    animations: [
        fadeInOutAnimation
    ]
})
export class BillInputComponent implements OnInit {
    @Input() inputTimeType: InputTimeType = InputTimeType.ONE_TIME;
    protected shown: boolean = true;
    bill: Bill = new Bill();
    constructor() {
        
    }

    ngOnInit() {
        this.bill.timeType = this.inputTimeType;
        console.log(this.bill);
    }

    public clearInputs(): void {

    }

    public updateBill(billContent: Bill | InputTimeType): void {
        if (billContent instanceof Bill) {
            const originalTimeType = this.bill.timeType;
            this.bill = billContent;
            this.bill.timeType = originalTimeType;

        } else {
            this.bill.timeType = billContent;
        }
        console.log(this.bill);
    }

    public confirm(): void {
        // TODO: Add services to send Bill.ts to back-end.
        this.shown = false;
    }

    public close(): void {
        this.shown = false;
    }

    public getAnimationProperties() {
        return {
            value: '',
            params: {
                fadeInDuration: quickFadeInAnimationProperties.duration,
                fadeOutDuration: quickFadeInAnimationProperties.duration,
                waitDuration: quickFadeInAnimationProperties.delay
            }
        }
    }
    protected readonly closeIconImageAsset = closeIconImageAsset;
    protected readonly TagType = TagType;
    protected readonly confirmIconImageAsset = confirmIconImageAsset;
}
