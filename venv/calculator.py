# Financial calculator utilities

import numpy as np
from typing import Dict, Union

class RealEstateCalculator:
    def calculate_roi(self, 
                     total_investment: float,
                     annual_rental_income: float,
                     annual_expenses: float,
                     property_appreciation: float = 0) -> Dict[str, Union[float, str]]:
        """
        Calculate Return on Investment (ROI) for a real estate investment
        
        Parameters:
        -----------
        total_investment: Initial cost including purchase price, repairs, closing costs
        annual_rental_income: Total yearly rental income
        annual_expenses: Total yearly expenses (maintenance, taxes, insurance, etc.)
        property_appreciation: Estimated yearly appreciation value
        
        Returns:
        --------
        Dictionary containing ROI percentage and component breakdown
        """
        # Calculate net operating income
        net_operating_income = annual_rental_income - annual_expenses
        
        # Calculate total return (cash flow + appreciation)
        total_return = net_operating_income + property_appreciation
        
        # Calculate ROI percentage
        roi_percentage = (total_return / total_investment) * 100
        
        return {
            "roi_percentage": round(roi_percentage, 2),
            "net_operating_income": round(net_operating_income, 2),
            "cash_flow_roi": round((net_operating_income / total_investment) * 100, 2),
            "appreciation_roi": round((property_appreciation / total_investment) * 100, 2)
        }

    def calculate_mortgage_payment(self,
                                 loan_amount: float,
                                 annual_interest_rate: float,
                                 loan_term_years: int) -> Dict[str, float]:
        """
        Calculate monthly mortgage payment and loan details
        
        Parameters:
        -----------
        loan_amount: Total amount borrowed
        annual_interest_rate: Annual interest rate (in percentage)
        loan_term_years: Length of loan in years
        
        Returns:
        --------
        Dictionary containing monthly payment and loan details
        """
        # Convert annual rate to monthly rate
        monthly_rate = annual_interest_rate / 12 / 100
        
        # Calculate number of payments
        num_payments = loan_term_years * 12
        
        # Calculate monthly payment using the mortgage payment formula
        monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate)**num_payments) / \
                         ((1 + monthly_rate)**num_payments - 1)
        
        # Calculate total interest paid
        total_paid = monthly_payment * num_payments
        total_interest = total_paid - loan_amount
        
        return {
            "monthly_payment": round(monthly_payment, 2),
            "total_interest": round(total_interest, 2),
            "total_paid": round(total_paid, 2)
        }

    def calculate_cap_rate(self,
                          property_value: float,
                          gross_income: float,
                          operating_expenses: float) -> Dict[str, float]:
        """
        Calculate Capitalization Rate (Cap Rate) for a property
        
        Parameters:
        -----------
        property_value: Current market value of the property
        gross_income: Annual gross income from the property
        operating_expenses: Annual operating expenses
        
        Returns:
        --------
        Dictionary containing cap rate and NOI
        """
        # Calculate Net Operating Income (NOI)
        noi = gross_income - operating_expenses
        
        # Calculate Cap Rate
        cap_rate = (noi / property_value) * 100
        
        return {
            "cap_rate": round(cap_rate, 2),
            "noi": round(noi, 2)
        }

    def calculate_cash_on_cash(self,
                              annual_cash_flow: float,
                              total_cash_invested: float) -> float:
        """
        Calculate Cash-on-Cash Return
        
        Parameters:
        -----------
        annual_cash_flow: Annual pre-tax cash flow
        total_cash_invested: Total cash invested (down payment, closing costs, repairs)
        
        Returns:
        --------
        Cash-on-Cash return percentage
        """
        return round((annual_cash_flow / total_cash_invested) * 100, 2)