// home.component.ts 
import { Component } from "@angular/core";
import {TagType} from "../../../models/html/TagType";

@Component({
    selector: 'home',
    templateUrl: './home.component.html',
    styleUrls: ['./home.component.css']
})
export class HomeComponent {
    constructor() {
        
    }

    protected readonly TagType = TagType;
}
