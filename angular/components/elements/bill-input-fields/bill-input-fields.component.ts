// bill-input-fields.component.ts 
import { Component } from "@angular/core";
import {
    BillInputFieldType
} from "../bill-input-field/models/BillInputFieldType";

@Component({
    selector: 'bill-input-fields',
    templateUrl: './bill-input-fields.component.html',
    styleUrls: ['./bill-input-fields.component.css']
})
export class BillInputFieldsComponent {
    constructor() {
        
    }

    protected readonly BillInputFieldType = BillInputFieldType;
}
