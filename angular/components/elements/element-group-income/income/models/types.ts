import { EventEmitter } from '@angular/core';
import { OneTimeIncome, RecurringIncome, WageIncome } from '../../../../../models/paycheck/types';

export type IncomeEmitter = EventEmitter<OneTimeIncome | RecurringIncome | WageIncome>;