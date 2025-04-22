import streamlit as st
from datetime import date

def calculate_age(birth_date, current_date):
    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    if days < 0:
        months -= 1
        days += (date(current_date.year, current_date.month, 1) - date(current_date.year, current_date.month - 1, 1)).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def main():
    st.title("🧮 Age Calculator")

    st.write("Enter your date of birth to calculate your age.")

    birth_date = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())

    if st.button("Calculate Age"):
        today = date.today()
        years, months, days = calculate_age(birth_date, today)
        st.success(f"You are {years} years, {months} months, and {days} days old.")

if __name__ == "__main__":
    main()
