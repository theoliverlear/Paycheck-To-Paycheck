// budget.component.ts 
import {Component, OnInit} from "@angular/core";
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
export class BudgetComponent implements OnInit {
    constructor() {
        
    }
    ngOnInit() {
        fetch('http://localhost:8000/api/paycheck/get/0', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: 'include'
        }).then(
            (response) => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Network response was not ok');
                }
            }
        ).then(
            (data) => {
                console.log(data);
            }
        ).catch(
            (error) => {
                console.error('There was a problem with the fetch operation:', error);
            }
        )
    }
}
