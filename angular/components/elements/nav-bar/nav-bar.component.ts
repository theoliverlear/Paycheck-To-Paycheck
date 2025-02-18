// nav-bar.component.ts 
import { Component } from "@angular/core";
import {
    navBarBudgetElementLink,
    navBarMyAccountElementLink, navBarPaychecksElementLink
} from "../../../assets/elementLinkAssets";

@Component({
    selector: 'nav-bar',
    templateUrl: './nav-bar.component.html',
    styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent {
    constructor() {
        
    }

    protected readonly navBarMyAccountElementLink = navBarMyAccountElementLink;
    protected readonly navBarPaychecksElementLink = navBarPaychecksElementLink;
    protected readonly navBarBudgetElementLink = navBarBudgetElementLink;
}
