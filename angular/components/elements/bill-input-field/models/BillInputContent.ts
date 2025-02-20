import {BillInputFieldType} from "./BillInputFieldType";

export class BillInputContent {
    public fieldType: BillInputFieldType;
    public value: string | number;
    public constructor(fieldType: BillInputFieldType = BillInputFieldType.TITLE,
                       value: string | number = '') {
        this.fieldType = fieldType;
        this.value = value;
    }
}