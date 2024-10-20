package org.theoliverlear.entity.paycheck;

import org.junit.jupiter.api.Test;
import org.theoliverlear.entity.time.DateRange;

import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class DateRangeTest {
    @Test
    public void testPaycheckPeriod() {
        LocalDate currentDate = LocalDate.now();
        LocalDate twoWeeksAfterCurrentDate = currentDate.plusDays(14);
        DateRange constructedDateRange = new DateRange(currentDate, twoWeeksAfterCurrentDate);
        DateRange actualPaycheckPeriod = DateRange.paycheckPeriod(currentDate);
        System.out.println("actualPaycheckPeriod = " + actualPaycheckPeriod);
        assertTrue(constructedDateRange.equals(actualPaycheckPeriod));
    }
}
