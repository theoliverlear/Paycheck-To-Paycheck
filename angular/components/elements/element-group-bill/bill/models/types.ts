import {EventEmitter} from "@angular/core";
import {OneTimeBill, RecurringBill} from "../../../../../models/paycheck/types";

export type BillEmitter = EventEmitter<OneTimeBill | RecurringBill>;