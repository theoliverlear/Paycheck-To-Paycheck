export enum RecurringBillTimeInterval {
    MONTHLY = 'Monthly',
    YEARLY = 'Yearly',
    WEEKLY = 'Weekly',
    QUARTERLY = 'Quarterly',
    DAILY = 'Daily'
}
export namespace RecurringBillTimeInterval {
    export function values(): string[] {
        return [
            RecurringBillTimeInterval.MONTHLY,
            RecurringBillTimeInterval.YEARLY,
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
            default:
                throw new Error(`Invalid value: ${value}`);
        }
    }
}