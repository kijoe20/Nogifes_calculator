import streamlit as st
from datetime import datetime, timedelta

# Function to calculate recovery time
def calculate_recovery_time(max_LP, current_LP):
    recover_time = (max_LP - current_LP) * 4  # 4 minutes per LP
    hours = recover_time // 60
    minutes = recover_time % 60
    return hours, minutes

# Function to update current time
# Main app logic
def main():
    # Streamlit app layout
    st.write("### LP Recovery Calculator")

    max_LP = st.number_input("Maximum LP", min_value=0, value=80, help="Enter the maximum LP achievable.")
    current_LP = st.number_input("Current LP", min_value=0, value=0, help="Enter your current LP.")

    # Calculate Button
    if st.button("Calculate"):
        calculate_recovery_time(max_LP, current_LP)

    # Initialize session state
    current_time = datetime.now()
    
    #display current time
    st.write("Current time:", current_time.strftime("%H:%M"))
    
    # LP recovery time calculation
    if current_LP < 0 or max_LP < 0:
        st.error("LP values cannot be negative.")
    elif current_LP > max_LP:
        st.error("Current LP cannot be greater than Maximum LP.")
    else:
        hours, minutes = calculate_recovery_time(max_LP, current_LP)
        recover_time_str = f"{hours}h {minutes}m"
        st.write("LP Recover time:", recover_time_str)

        # Estimated time of LP full recovery
        recover_time = timedelta(hours=hours, minutes=minutes)
        estimated_finish_time = current_time + recover_time
        st.write("Estimated time of LP full recovery:", estimated_finish_time.strftime("%H:%M"))

# Run the app
if __name__ == "__main__":
    main()
