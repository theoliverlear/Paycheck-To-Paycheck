export enum RecurringBillTimeInterval {
    MONTHLY = 'Monthly',
    YEARLY = 'Yearly',
    BI_WEEKLY = 'Bi-Weekly',
    WEEKLY = 'Weekly',
    QUARTERLY = 'Quarterly',
    DAILY = 'Daily'
}
export namespace RecurringBillTimeInterval {
    export function values(): string[] {
        return [
            RecurringBillTimeInterval.MONTHLY,
            RecurringBillTimeInterval.YEARLY,
            RecurringBillTimeInterval.BI_WEEKLY,
            RecurringBillTimeInterval.WEEKLY,
            RecurringBillTimeInterval.QUARTERLY,
            RecurringBillTimeInterval.DAILY
        ];
    }
    export function from(value: string): RecurringBillTimeInterval {
        switch (value) {
            case RecurringBillTimeInterval.DAILY:
                return RecurringBillTimeInterval.DAILY;
            case RecurringBillTimeInterval.WEEKLY:
                return RecurringBillTimeInterval.WEEKLY;
            case RecurringBillTimeInterval.MONTHLY:
                return RecurringBillTimeInterval.MONTHLY;
            case RecurringBillTimeInterval.QUARTERLY:
                return RecurringBillTimeInterval.QUARTERLY;
            case RecurringBillTimeInterval.YEARLY:
                return RecurringBillTimeInterval.YEARLY;
            case RecurringBillTimeInterval.BI_WEEKLY:
                return RecurringBillTimeInterval.BI_WEEKLY;
            default:
                throw new Error(`Invalid value: ${value}`);
        }
    }
}