// nav-bar.component.ts 
import { Component } from "@angular/core";
import {
    navBarHomeElementLink,
    navBarMyAccountElementLink, navBarPaychecksElementLink
} from "../../../assets/elementLinkAssets";

@Component({
    selector: 'nav-bar',
    templateUrl: './nav-bar.component.html',
    styleUrls: ['./nav-bar-style.component.css']
})
export class NavBarComponent {
    constructor() {
        
    }

    protected readonly navBarHomeElementLink = navBarHomeElementLink;
    protected readonly navBarMyAccountElementLink = navBarMyAccountElementLink;
    protected readonly navBarPaychecksElementLink = navBarPaychecksElementLink;
}
