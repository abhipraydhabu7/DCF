def calculate_dcf(fcf_forecast, wacc, terminal_growth_rate, final_year):
    """
    Parameters:
    - fcf_forecast: List of projected Free Cash Flows (FCF) for each year.
    - wacc: Weighted Average Cost of Capital (decimal, e.g., 0.10 for 10%).
    - terminal_growth_rate: Growth rate after final year (decimal, e.g., 0.03 for 3%).
    - final_year: Final forecast year (int).

    Returns:
    - DCF value (Net Present Value of the firm)
    """
    dcf_value = 0
    for i, fcf in enumerate(fcf_forecast):
        year = i + 1
        discounted_fcf = fcf / ((1 + wacc) ** year)
        dcf_value += discounted_fcf

    # Terminal value calculation
    terminal_value = fcf_forecast[-1] * (1 + terminal_growth_rate) / (wacc - terminal_growth_rate)
    discounted_terminal_value = terminal_value / ((1 + wacc) ** final_year)

    return dcf_value + discounted_terminal_value

# --- Example usage ---

# Forecasted Free Cash Flows for 5 years (in millions)
fcf_forecast = [100, 110, 120, 130, 140]

# WACC = 10%, Terminal Growth Rate = 3%
wacc = 0.10
terminal_growth_rate = 0.03
final_year = 5

dcf_result = calculate_dcf(fcf_forecast, wacc, terminal_growth_rate, final_year)
print(f"Intrinsic Value of the firm: ${dcf_result:.2f} million")


#$######################
# UYtttttttttttttttttt