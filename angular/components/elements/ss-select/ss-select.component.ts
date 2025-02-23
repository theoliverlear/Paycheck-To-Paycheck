// ss-select.component.ts 
import {Component, EventEmitter, Input, OnInit, Output} from "@angular/core";

@Component({
    selector: 'ss-select',
    templateUrl: './ss-select.component.html',
    styleUrls: ['./ss-select.component.css']
})
export class SsSelectComponent implements OnInit {
    @Input() dropdownItems: string[];
    @Input() title: string;
    selectedItem: string;
    @Output() selectedItemChange: EventEmitter<string> = new EventEmitter<string>();
    constructor() {
        
    }
    ngOnInit() {
        this.selectedItem = this.dropdownItems[0];
    }

    emitItemChange(item: string) {
        this.selectedItem = item;
        this.selectedItemChange.emit(item);
    }
}
