export function convertToDate(object: any): any {
    if (!object || typeof object !== 'object') {
        return object;
    }
    for (const key of Object.keys(object)) {
        const value = object[key];
        if (typeof value === 'string' || typeof value === 'number') {
            if (key.includes('date') || key.includes('Date') || key.includes('day')) {
                const date = new Date(value);
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