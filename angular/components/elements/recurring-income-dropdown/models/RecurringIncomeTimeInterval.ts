export enum RecurringIncomeTimeInterval {
    SALARY = 'Salary',
    HOURLY_WAGE = 'Hourly Wage',
    PAYCHECK = 'Paycheck',
    MONTHLY = 'Monthly',
}
export namespace RecurringIncomeTimeInterval {
    export function values(): string[] {
        return [
            RecurringIncomeTimeInterval.SALARY,
            RecurringIncomeTimeInterval.HOURLY_WAGE,
            RecurringIncomeTimeInterval.PAYCHECK,
            RecurringIncomeTimeInterval.MONTHLY,
        ];
    }
    export function from(value: string): RecurringIncomeTimeInterval {
        switch (value) {
            case RecurringIncomeTimeInterval.SALARY:
                return RecurringIncomeTimeInterval.SALARY;
            case RecurringIncomeTimeInterval.HOURLY_WAGE:
                return RecurringIncomeTimeInterval.HOURLY_WAGE;
            case RecurringIncomeTimeInterval.PAYCHECK:
                return RecurringIncomeTimeInterval.PAYCHECK;
            case RecurringIncomeTimeInterval.MONTHLY:
                return RecurringIncomeTimeInterval.MONTHLY;
            default:
                throw new Error(`Invalid value: ${value}`);
        }
    }
}