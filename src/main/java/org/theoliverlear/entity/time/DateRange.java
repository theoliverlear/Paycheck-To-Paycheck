package org.theoliverlear.entity.time;

import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;
@Getter
@Setter
public class DateRange {
    private LocalDate startDate;
    private LocalDate endDate;
    public DateRange(LocalDate startDate, LocalDate endDate) {
        this.startDate = startDate;
        this.endDate = endDate;
    }
    public boolean inRange(LocalDate date) {
        return !date.isBefore(this.startDate) && !date.isAfter(this.endDate);
    }
    public static DateRange paycheckPeriod(LocalDate startDate) {
        return new DateRange(startDate, startDate.plusDays(14));
    }
    @Override
    public String toString() {
        return this.startDate + " to " + this.endDate;
    }
    @Override
    public boolean equals(Object object) {
        if (this == object) return true;
        if (object instanceof DateRange comparedDateRange) {
            return this.startDate.equals(comparedDateRange.startDate) && this.endDate.equals(comparedDateRange.endDate);
        } else {
            return false;
        }
    }
}
