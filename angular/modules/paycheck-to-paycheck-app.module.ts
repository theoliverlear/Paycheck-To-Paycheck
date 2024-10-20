import {NgModule} from "@angular/core";
import {AppComponent} from "../components/app/app.component";

@NgModule({
    declarations: [AppComponent],
    imports: [],
    providers: [],
    bootstrap: [AppComponent],
    exports: [],
    schemas: []
})
export class PaycheckToPaycheckAppModule {
    constructor() {
        console.log('PaycheckToPaycheckModule loaded');
    }
}