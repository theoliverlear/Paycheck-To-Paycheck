// input-popup.component.ts 
import {Component, Input} from "@angular/core";
import {TagType} from "../../../models/html/TagType";
import {BillInputPopupType} from "../bill-input/models/BillInputPopupType";
import {IncomeInputPopupType} from "../income-input/models/IncomeInputPopupType";

@Component({
    selector: 'input-popup',
    templateUrl: './input-popup.component.html',
    styleUrls: ['./input-popup.component.css']
})
export class InputPopupComponent {
    @Input() protected popup: BillInputPopupType | IncomeInputPopupType;
    constructor() {
        
    }

    protected readonly TagType = TagType;
}
