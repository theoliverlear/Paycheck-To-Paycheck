// budget.component.ts 
import { Component } from "@angular/core";
import {
    fadeInOutAnimation
} from "../../animations/animations";

@Component({
    selector: 'budget',
    templateUrl: './budget.component.html',
    styleUrls: ['./budget.component.css'],
    animations: [
        fadeInOutAnimation
    ]
})
export class BudgetComponent {
    constructor() {
        
    }
}
