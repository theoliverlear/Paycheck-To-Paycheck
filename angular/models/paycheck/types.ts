export type DateRange = {
    id: number;
    endDate: Date;
    startDate: Date;
};

export type DueDate = {
    id: number;
    name: string;
    dueDate: Date;
};

export type RecurringDate = {
    id: number;
    day: Date;
    interval: number;
}

export type OneTimeBill = {
    id: number;
    amount: number;
    dueDate: DueDate;
    name: string;
    type: 'OneTimeBill';
};

export type RecurringBill = {
    id: number;
    amount: number;
    recurringDate: RecurringDate;
    name: string;
    type: 'RecurringBill';
};

export type OneTimeIncome = {
    id: number;
    amount: number;
    dateReceived: Date;
    name: string;
    type: 'OneTimeIncome';
};

export type RecurringIncome = {
    id: number;
    amount: number;
    recurringDate: RecurringDate;
    name: string;
    yearlyIncome: number;
    type: 'RecurringIncome';
};

export type WageIncome = {
    id: number;
    amount: number;
    recurringDate: RecurringDate;
    name: string;
    yearlyIncome: number;
    weeklyHours: number;
    type: 'WageIncome';
};

export type Income = OneTimeIncome | RecurringIncome | WageIncome;
export type Bill = OneTimeBill | RecurringBill;

export type WebSocketOneTimeBill = {
    message: OneTimeBill,
    type: 'OneTimeBill';
};

export type WebSocketRecurringBill = {
    message: RecurringBill,
    type: 'RecurringBill';
};

export type WebSocketBill = WebSocketOneTimeBill | WebSocketRecurringBill;

export type Bills = {
    oneTimeBills: OneTimeBill[];
    recurringBills: RecurringBill[];
};

export type Incomes = {
    oneTimeIncomes: OneTimeIncome[];
    recurringIncomes: RecurringIncome[];
    wageIncomes: WageIncome[];
};

export type Paycheck = {
    dateRange: DateRange;
    leftOverIncome: number;
    oneTimeBills: OneTimeBill[];
    oneTimeIncomes: OneTimeIncome[];
    recurringBills: RecurringBill[];
    recurringIncomes: RecurringIncome[];
    wageIncomes: WageIncome[];
    totalBills: number;
    totalIncome: number;
};