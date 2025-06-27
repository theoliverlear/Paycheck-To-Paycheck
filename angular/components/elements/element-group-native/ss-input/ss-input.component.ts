// ss-input.component.ts
import {
    Component,
    EventEmitter,
    HostListener,
    Input,
    Output
} from "@angular/core";
import {InputType} from "./models/InputType";

@Component({
    selector: 'ss-input',
    templateUrl: './ss-input.component.html',
    styleUrls: ['./ss-input.component.css']
})
export class SsInputComponent {
    @Input() inputType: InputType;
    @Output() inputEvent: EventEmitter<string> = new EventEmitter<string>();
    @Input() max: string | number;
    @Input() min: string | number;
    @Input() value: string | number;
    @Input() placeholder: string;
    constructor() {

    }
    @HostListener('input', ['$event.target.value'])
    onInput(value: string) {
        this.inputEvent.emit(value);
    }
    isCheckbox(): boolean {
        return this.inputType === InputType.CHECKBOX;
    }
    isRange(): boolean {
        return this.inputType === InputType.RANGE;
    }
    protected getDefaultValue(): string | number | null {
        return this.value || null;
    }
}
