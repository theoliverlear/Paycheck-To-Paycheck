-- Recurring Dates
CREATE INDEX idx_recurring_dates_day ON recurring_dates (day);
CREATE INDEX idx_recurring_dates_interval ON recurring_dates (interval);
CREATE INDEX idx_recurring_dates_day_interval ON recurring_dates (day, interval);

-- Recurring Incomes
CREATE INDEX idx_recurring_incomes_income_history_recurring_date ON recurring_incomes (income_history_id, recurring_date_id);
CREATE INDEX idx_recurring_incomes_amount_recurring_date ON recurring_incomes (amount, recurring_date_id);

-- Wage Incomes
CREATE INDEX idx_wage_incomes_income_history_recurring_date ON wage_incomes (income_history_id, recurring_date_id);
CREATE INDEX idx_wage_incomes_income_history_weekly_hours ON wage_incomes (income_history_id, weekly_hours);
CREATE INDEX idx_wage_incomes_amount ON wage_incomes (amount);

-- Users
CREATE UNIQUE INDEX idx_users_username ON users (username);
CREATE UNIQUE INDEX idx_users_email ON users (email);
CREATE INDEX idx_users_income_history_bill_history ON users (income_history_id, bill_history_id);
CREATE INDEX idx_users_payday_id ON users (payday_id);

-- Django Session
CREATE UNIQUE INDEX idx_django_session_session_key ON django_session (session_key);
CREATE INDEX idx_django_session_expire_date ON django_session (expire_date);

-- Income Histories & Bill Histories
CREATE INDEX idx_income_histories_id ON income_histories (id);
CREATE INDEX idx_bill_histories_id ON bill_histories (id);

-- One-Time Bills
CREATE INDEX idx_one_time_bills_history_due_date ON one_time_bills (bill_history_id, due_date_id);
CREATE INDEX idx_one_time_bills_amount ON one_time_bills (amount);

-- One-Time Incomes
CREATE INDEX idx_one_time_incomes_history_date ON one_time_incomes (income_history_id, date_received);
CREATE INDEX idx_one_time_incomes_amount ON one_time_incomes (amount);

-- Recurring Bills
CREATE INDEX idx_recurring_bills_history_recurring_date ON recurring_bills (bill_history_id, recurring_date_id);
CREATE INDEX idx_recurring_bills_amount ON recurring_bills (amount);