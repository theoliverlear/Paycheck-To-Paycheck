import {Route, Routes} from "@angular/router";
import {HomeComponent} from "../../components/pages/home/home.component";
import {AuthGuard} from "../../services/guard/auth.guard";
import {
    AuthorizeComponent
} from "../../components/pages/authorize/authorize.component";
import {
    PaychecksComponent
} from "../../components/pages/paychecks/paychecks.component";
import {
    AccountComponent
} from "../../components/pages/account/account.component";
import {AccountGuard} from "../../services/guard/account.guard";
import {
    BudgetComponent
} from "../../components/pages/budget/budget.component";

const isDevelopment = false;
export const accountRoute: Route = {
    path: 'account',
    component: AccountComponent,
    canActivate: isDevelopment ? [] : [AuthGuard],
    data: {
        meta: {
            title: 'Account | Paycheck to Paycheck'
        }
    }
};
export const authorizeRoute: Route = {
    path: 'authorize',
    component: AuthorizeComponent,
    canActivate: isDevelopment ? [] : [],
    data: {
        meta: {
            title: 'Authorize | Paycheck to Paycheck'
        }
    }
};
export const budgetRoute: Route = {
    path: 'budget',
    component: BudgetComponent,
    canActivate: isDevelopment ? [] : [AuthGuard],
    data: {
        meta: {
            title: 'Budget | Paycheck to Paycheck'
        }
    }
};
export const homeRoute: Route = {
    path: '',
    component: HomeComponent,
    data: {
        meta: {
            title: 'Paycheck to Paycheck'
        },
    }
};
export const paychecksRoute: Route = {
    path: 'paychecks',
    component: PaychecksComponent,
    canActivate: isDevelopment ? [] : [AuthGuard],
    data: {
        meta: {
            title: 'Paychecks | Paycheck to Paycheck',
        }
    }
};
export const welcomeRoute: Route = {
    path: 'welcome',
    component: HomeComponent,
    canActivate: isDevelopment ? [] : [AuthGuard],
    data: {
        meta: {
            title: 'Welcome | Paycheck to Paycheck',
        }
    }
};
export const routes: Routes = [
    accountRoute,
    authorizeRoute,
    budgetRoute,
    homeRoute,
    paychecksRoute,
    welcomeRoute
];