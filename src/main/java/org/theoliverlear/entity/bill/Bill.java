package org.theoliverlear.entity.bill;

import lombok.Getter;
import lombok.Setter;
import org.theoliverlear.entity.time.DueDay;

@Getter
@Setter
public class Bill {
    private int amount;
    private DueDay dueDay;
}
