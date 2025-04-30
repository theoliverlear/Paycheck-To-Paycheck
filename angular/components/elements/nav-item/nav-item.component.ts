// nav-item.component.ts 
import {Component, HostListener, Input, ViewChild} from "@angular/core";
import {TextElementLink} from "../../../models/link/TextElementLink";
import {SsAnchorComponent} from "../ss-anchor/ss-anchor.component";
import {navBarHomeElementLink} from "../../../assets/elementLinkAssets";

@Component({
    selector: 'nav-item',
    templateUrl: './nav-item.component.html',
    styleUrls: ['./nav-item.component.css']
})
export class NavItemComponent {
    @Input() elementLink: TextElementLink;
    @ViewChild(SsAnchorComponent) anchorComponent: SsAnchorComponent;
    constructor() {

    }

    public setText(text: string) {
        this.elementLink.text = text;
    }

    @HostListener('click')
    onClick() {
        this.anchorComponent.onClick();
    }
}
