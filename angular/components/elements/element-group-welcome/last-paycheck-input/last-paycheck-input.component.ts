// last-paycheck-input.component.ts 
import {Component, Output, EventEmitter} from "@angular/core";
import {TagType} from "../../../../models/html/TagType";
import {
    InputType
} from "../../element-group-native/ss-input/models/InputType";
import {LastPaycheck} from "./models/LastPaycheck";

@Component({
    selector: 'last-paycheck-input',
    templateUrl: './last-paycheck-input.component.html',
    styleUrls: ['./last-paycheck-input.component.css']
})
export class LastPaycheckInputComponent {
    @Output() confirmEvent: EventEmitter<LastPaycheck> = new EventEmitter<LastPaycheck>();
    lastPaycheck: LastPaycheck = new LastPaycheck();
    constructor() {
        
    }

    emitConfirm(): void {
        this.confirmEvent.emit(this.lastPaycheck);
    }

    setDate(date: string): void {
        this.lastPaycheck.lastPaycheckDate = new Date(date);
    }

    setPaycheckAmount(amount: string): void {
        this.lastPaycheck.paycheckAmount = parseFloat(amount);
    }

    setCheckingAccountAmount(amount: string): void {
        this.lastPaycheck.checkingAccountAmount = parseFloat(amount);
    }

    protected readonly TagType = TagType;
    protected readonly InputType = InputType;
}
