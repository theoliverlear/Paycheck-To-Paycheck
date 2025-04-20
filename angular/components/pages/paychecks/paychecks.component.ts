// paychecks.component.ts 
import {Component, Input, OnInit} from "@angular/core";

@Component({
    selector: 'paychecks',
    templateUrl: './paychecks.component.html',
    styleUrls: ['./paychecks.component.css']
})
export class PaychecksComponent implements OnInit {
    @Input() numPaychecks: number = 5;
    @Input() paycheckIds: number[] = [];
    constructor() {
        
    }

    ngOnInit(): void {
        for (let i = 0; i < this.numPaychecks; i++) {
            this.paycheckIds.push(i);
        }
    }
}
