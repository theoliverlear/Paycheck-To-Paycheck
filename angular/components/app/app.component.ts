import {Component} from "@angular/core";

@Component({
    selector: 'app',
    templateUrl: './app.component.html',
    styleUrls: ['./app-style.component.css']
})
export class AppComponent {
    constructor() {
        console.log('AppComponent loaded');
    }
}