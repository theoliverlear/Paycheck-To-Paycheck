export function convertToDate(object: any): any {
    let isInvalidObject: boolean = !object || typeof object !== 'object';
    if (isInvalidObject) {
        return object;
    }
    for (const key of Object.keys(object)) {
        const value = object[key];
        if (typeof value === 'string' || typeof value === 'number') {
            const isDateKey: boolean = key.includes('date') ||
                                       key.includes('Date') ||
                                       key.includes('day');
            if (isDateKey) {
                const date = new Date(`${value}T00:00:00`);
                if (!isNaN(date.valueOf())) {
                    object[key] = date;
                }
            }
        } else if (typeof value === 'object') {
            convertToDate(value);
        }
    }
    return object;
}