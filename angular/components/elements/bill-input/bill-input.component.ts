// bill-input.component.ts
import {Component, HostBinding, Input} from "@angular/core";
import {InputTimeType} from "../../../models/input/InputTimeType";
import {
    closeIconImageAsset
} from "../../../assets/imageAssets";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'bill-input',
    templateUrl: './bill-input.component.html',
    styleUrls: ['./bill-input.component.css']
})
export class BillInputComponent {
    @Input() inputTimeType: InputTimeType = InputTimeType.ONE_TIME;
    protected shown: boolean = true;
    constructor() {
        
    }

    public close(): void {
        this.shown = false;
    }
    protected readonly closeIconImageAsset = closeIconImageAsset;
    protected readonly TagType = TagType;
}
