import {Route, Routes} from "@angular/router";
import {HomeComponent} from "../../components/pages/home/home.component";

const isDevelopment = true;

export const homeRoute: Route = {
    path: '',
    component: HomeComponent,
    data: {
        meta: {
            title: 'Paycheck to Paycheck'
        },
    }
}
export const routes: Routes = [
    homeRoute
];