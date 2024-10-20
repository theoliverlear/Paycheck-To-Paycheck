import {platformBrowserDynamic} from "@angular/platform-browser-dynamic";
import {
    PaycheckToPaycheckAppModule
} from "./modules/paycheck-to-paycheck-app.module";

console.log('main.ts loaded');

platformBrowserDynamic().bootstrapModule(PaycheckToPaycheckAppModule)
    .catch(error => console.error(error));