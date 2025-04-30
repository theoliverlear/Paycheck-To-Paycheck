export type DateRange = {
    endDate: Date;
    startDate: Date;
};

export type DueDate = {
    name: string;
    dueDate: Date;
};

export type RecurringDate = {
    day: Date;
    interval: number;
}

export type OneTimeBill = {
    amount: number;
    dueDate: DueDate;
    name: string;
};

export type RecurringBill = {
    amount: number;
    recurringDate: RecurringDate;
    name: string;
};

export type OneTimeIncome = {
    amount: number;
    dateReceived: Date;
    name: string;
};

export type RecurringIncome = {
    amount: number;
    recurringDate: RecurringDate;
    name: string;
    yearlyIncome: number;
};

export type WageIncome = {
    amount: number;
    recurringDate: RecurringDate;
    name: string;
    yearlyIncome: number;
    weeklyHours: number;
};

export type Income = OneTimeIncome | RecurringIncome | WageIncome;
export type Bill = OneTimeBill | RecurringBill;

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