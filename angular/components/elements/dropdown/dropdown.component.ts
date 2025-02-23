// dropdown.component.ts 
import {Component, EventEmitter, Input, Output} from "@angular/core";

@Component({
    selector: 'dropdown',
    templateUrl: './dropdown.component.html',
    styleUrls: ['./dropdown.component.css']
})
export class DropdownComponent {
    @Output() dropdownSelected: EventEmitter<string> = new EventEmitter<string>();
    @Input() dropdownItems: string[];
    @Input() title: string;
    constructor() {
        
    }
    emitDropdownSelected(item: string) {
        this.dropdownSelected.emit(item);
    }
}
